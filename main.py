from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from bs4 import BeautifulSoup as bs
from seleniumwire import webdriver
import os
import time
import json
import pymysql
from make_db import insert_data_into_db
import pandas as pd
from datetime import datetime


conn = pymysql.connect(host='127.0.0.1', user='root', password='khv032900!', db='pythonDB', charset='utf8')
isSchedule = True

class FreightAutomation:
    def __init__(self):
        self.driver = self.initialize_driver()
        self.login_url = "https://www.ekmtc.com"
        self.schedule_url = "https://www.ekmtc.com/index.html#/schedule/leg"
        load_dotenv()
        self.id = os.getenv('ID')
        self.pw = os.getenv('PW')

    def initialize_driver(self):

        options = {
            'disable_encoding': True  # This can help capture binary data without corruption
        }

        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("headless")
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1280,920')
        chrome_options.add_argument('--disable-dev-shm-usage')

        chrome_driver_path = ChromeDriverManager().install()
        service = Service(chrome_driver_path)

        return webdriver.Chrome(service=service, options=chrome_options, seleniumwire_options=options)


    def login(self):
        self.driver.get(self.login_url)
        try:
            # 로그인 버튼 클릭
            self.driver.find_element(By.CSS_SELECTOR, "body > div > div.wrap.wrap_KOR > div.header > div.inner_header > div.wrap_util > ul > li:nth-child(2) > a").click()

            id_input = self.driver.find_element(By.CSS_SELECTOR, "#id")
            id_input.send_keys(self.id)
            pw_input = self.driver.find_element(By.CSS_SELECTOR, "#pw")
            pw_input.send_keys(self.pw)

            # 로그인 버튼 클릭
            self.driver.find_element(By.CSS_SELECTOR, "body > div > div.wrap.wrap_KOR > div.header > div.inner_header > div.wrap_util > div.loginLayer_wrap > fieldset > div.btnarea > a.button.blue.sm").click()

            # 프로필 선택
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#profile_pop > div > div.content_box > ul > li:nth-child(2) > p.img > img")))
            self.driver.find_element(By.CSS_SELECTOR, '#profile_pop > div > div.content_box > ul > li:nth-child(2) > p.img > img').click()
            print("Login successful")
        except Exception as e:
            print(f"Login failed: {str(e)}")


    # 출발항을 한국에 있는 모든 항구로 설정해서 각 수출 경로별 데이터 운임을 받아오도록 하는 함수
    def set_port_export(self):
        cur = conn.cursor()

        selec_korea_port_sql = "SELECT ctrCd,plcCd,plcEnm FROM portTable pt WHERE ctrCd = 'kr'"
        # select_abroad__port_sql = "SELECT ctrCd,plcCd,plcEnm FROM portTable pt WHERE ctrCd != 'kr' ORDER BY ctrCd ASC"
        select_abroad__port_sql = "SELECT ctrCd,plcCd,plcEnm FROM portTable pt WHERE plcCd != 'kr' ORDER BY ctrCd ASC"

        cur.execute(selec_korea_port_sql)
        kr_port_result = cur.fetchall()
        
        cur.execute(select_abroad__port_sql)
        abroad_port_result = cur.fetchall()

        try:
            for start in kr_port_result:
                for dest in abroad_port_result:
                    start_ctrCd, start_plcCd, start_plcName = start
                    dest_ctrCd, dest_plcCd, dsest_plcName = dest

                    # query = "SELECT * FROM freightTable"
                    # df = pd.read_sql(query, conn)
                    # if (df['destPort'] == dest_plcCd).any():
                    #     print('isdone?', dest_plcCd)
                    #     continue

                    # 문자열 공백을 +로 채워서 params를 보내야함
                    if isinstance(start_plcName, str):
                        start_plcName = start_plcName.replace(" ", "+")
                    if isinstance(dsest_plcName, str):
                        dsest_plcName = dsest_plcName.replace(" ", "+")
                    
                    month = datetime.today().month
                    year = datetime.today().year

                    param = {
                        "startPlcCd": start_plcCd, # "PUS"
                        "searchMonth": month, # "11"
                        "startPlcName": start_plcName, #"Busan, Korea (PUS)"
                        "destPlcCd": dest_plcCd, #HKG
                        "searchYear": year, #"2024"
                        "startCtrCd": start_ctrCd, #"KR"
                        "destCtrCd": dest_ctrCd, #HK
                        "destPlcName": dsest_plcName, #Hong Kong (HKG)
                    }

                    reqRno_value, schedule_param = self.set_port(param)
                    # reqRno_value 없으면 운임 받아올 수 없음
                    if reqRno_value and schedule_param:
                        print('if' ,reqRno_value,schedule_param )

                        time.sleep(2)
                        self.get_freight_data(reqRno_value, schedule_param)

                        with open(f'freight_data_{param.get("startPlcCd")}_{param.get("destPlcCd")}.json', "r") as f:
                            data = json.load(f)
                        insert_data_into_db(data, param.get('startPlcCd'), param.get('destPlcCd'))
                    else:
                        print('continue' ,reqRno_value,schedule_param )

                        continue
                print('one loop complete')
            
            # 테이블생성 후 csv파일 생성
            self.make_freightTable_to_csv()
        except Exception as e:
            print(f"set_port_export: {str(e)}")

            
    def set_port(self, param):
        try:
            time.sleep(5)

            self.driver.get("https://www.ekmtc.com/index.html#/schedule/leg")
            time.sleep(5)

            def interceptor(request):
                token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZXNzSWQiOiJfbW1xdmNlb3p4LVFQUE94Z0lsZEJqMUhieDFselZTNXQ4MTZZVzY5LTE1MjE1MiIsInVzZXJJZCI6IllPTDAwM18wMDEiLCJvcmdVc2VySWQiOiJZT0xDQVJHTyIsInVzZXJOYW1lIjoi6rCV7J246recIiwidXNlckVuYW1lIjoiWU9MIElOQyIsImNzdENhdENkIjoiMDEiLCJ1c2VyVHlwZSI6IjkiLCJjc3RDZCI6IllPTDAwMyIsInN0YWZmRmxhZyI6Ik4iLCJ1c2VyQ3RyQ2QiOiJLUiIsImFkbWluIjpmYWxzZSwicm9sZSI6Ik1FTUJFUiIsInNlcnZpY2VMYW5nIjoiS09SIiwiaWF0IjoxNzMyNTE1NzEyLCJleHAiOjE3MzUxMDc3MTJ9.grChgt6ek7Ouf7e8Vx1OH-YPI74gaK46tig9To8vsvo'
                request.headers['Authorization'] = f'Bearer {token}'

            self.driver.request_interceptor = interceptor

            print('param', param.get('startPlcCd'), param.get('destPlcCd'))


            # param = {
            #     "startPlcCd": start_plcCd, # "PUS"
            #     "searchMonth": get_next_month, # "11"
            #     "startPlcName": start_plcName, #"Busan, Korea (PUS)"
            #     "destPlcCd": dest_plcCd, #HKG
            #     "searchYear": year, #"2024"
            #     "startCtrCd": start_ctrCd, #"KR"
            #     "destCtrCd": dest_ctrCd, #HK
            #     "destPlcName": dsest_plcName, #Hong Kong (HKG)
            # }

            #  경로 스케줄 검색
            self.driver.get(f"https://api.ekmtc.com/schedule/schedule/leg/search-schedule?startPlcCd={param.get('startPlcCd')}&searchMonth={param.get('searchMonth')}&pointChangeYN=&bound=O&filterPolCd=&pointLength=&startPlcName={param.get('startPlcName')}&destPlcCd={param.get('destPlcCd')}&searchYear={param.get('searchYear')}&filterYn=N&searchYN=Y&filterPodCd=&hiddestPlcCd=&startCtrCd={param.get('startCtrCd')}&destCtrCd={param.get('destCtrCd')}&polTrmlStr=&podTrmlStr=&rteCd=&filterTs=Y&filterDirect=Y&filterTranMax=0&filterTranMin=0&hidstartPlcCd=&destPlcName={param.get('destPlcName')}&main=N&legIdx=0&vslType01=01&vslType03=03&unno=&commodityCd=&eiCatCd=O&calendarOrList=C&cpYn=N&promotionChk=N&vslCd=&voyNo=")
            print('스케줄 검색')
            time.sleep(5)

            # 스케줄 검색 응답 결과 저장
            elements = self.driver.find_element(By.XPATH, '/html/body/pre')

            json_data = json.loads(elements.text)
            print('listSchedule length', len(json_data.get('listSchedule')))

            # listSchedule이 빈 배열이면 스케줄이 없는 경우
            if len(json_data.get('listSchedule')) == 0:
                # isSchedule = False  
                print('no Schedule')
                return (None, None)
            
            time.sleep(5)

            # 각 경로별 스케줄 파일 생성
            start = param.get('startPlcCd')
            dest = param.get('destPlcCd')
            with open(f'schedule_{start}_{dest}.json', 'w') as f:
                json.dump(json_data, f)

            print("port selected")

            time.sleep(5)

            # 받아온 스케줄.json으로부터 pop-fre-app-no api에 reqNo 함께 보내기
            reqRno_value, schedule_param = self.get_available_ship(json_data) 
            return (reqRno_value, schedule_param)


        except Exception as e:
            print(f"Error selecting set port: {str(e)}")
    
    # 스케줄 json으로부터 마감이 되지 않은 이용가능한 선사 정보 가져오기
    def get_available_ship(self, schedule_json):
        try:
            # 현재 시간 가져오기
            now = datetime.now()
            date_str = now.strftime("%Y%m%d%H%M") # "YYYYMMDDHHMM"

            # 스케줄상 closeTime이 마감되지 않은 선사 중 첫 번째 객체 찾기
            first_valid_schedule = next(
                (schedule for schedule in schedule_json.get('listSchedule') if date_str < schedule.get('closeTime')),
                None
            )
            print('first_valid_schedule',first_valid_schedule)
            # startCtrCd = schedule_json.get('arrayStartCtrCd')[0] # KR
            # startPlcCd = schedule_json.get('arrayStartPlcCd')[0] # PUS
            # destCtrCd = schedule_json.get('arrayDestCtrCd')[0] # AE
            # destPlcCd = schedule_json.get('arrayDestPlcCd')[0] # JEA

            # polNm:BUSAN+NEW+PORT,+KOREA
            # podNm:JEBEL+ALI,UNITED+ARAB+EMIRATES
            # etd:20241206
            # frtAppNo:
            # vslCd:HKS
            # vslNm:HAKATA+SEOUL
            # reqRno:000000492801
            param_origin = {
                "startCtrCd" : schedule_json.get('arrayStartCtrCd')[0], # KR
                "startPlcCd" : schedule_json.get('arrayStartPlcCd')[0], # PUS
                "destCtrCd" : schedule_json.get('arrayDestCtrCd')[0], # AE
                "destPlcCd" : schedule_json.get('arrayDestPlcCd')[0], # JEA
                "polNm" : first_valid_schedule.get('polNm'), # "BUSAN NEW PORT, KOREA"
                "podNm" : first_valid_schedule.get('podNm'), # JEBEL+ALI,UNITED+ARAB+EMIRATES
                "etd" : first_valid_schedule.get("etd"), # etd: 20241206
                # "frtAppNo" : first_valid_schedule.get('frtAppNo'), # 
                "vslCd" : first_valid_schedule.get('vslCd'), # HKS
                "vslNm" : first_valid_schedule.get('vslNm'), # HAKATA+SEOUL
                "voyNo" : first_valid_schedule.get('voyNo'), # 
            }
            print("Vessel Name:", first_valid_schedule.get('vslNm'))

            param = self.replace_space_with_plus(param_origin)

            self.driver.get(f'https://api.ekmtc.com/schedule/schedule/leg/pop-fre-app-no?porCtrCd={param.get("startCtrCd")}&porPlcCd={param.get("startPlcCd")}&dlyCtrCd={param.get("destCtrCd")}&dlyPlcCd={param.get("destPlcCd")}&eiCatCd=O&logYn=N&etd={param.get("etd")}')
            # self.driver.get(f'https://api.ekmtc.com/schedule/schedule/leg/pop-fre-app-no?porCtrCd={startCtrCd}&porPlcCd={startPlcCd}&dlyCtrCd={destCtrCd}&dlyPlcCd={destPlcCd}&eiCatCd=O&logYn=N&etd={etd}')

            # Wait for the pre element and extract text
            getReqNo_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/pre'))
            )
            getReqNo_text = getReqNo_element.text
            getReqNo_json_data = json.loads(getReqNo_text)

            # 경로상 스케줄 없는 경우도 있음
            if getReqNo_json_data:

                # "frtAppNo","reqRno" 둘 중 하나를 가져와야 함
                reqRno_value = getReqNo_json_data.get("reqRno")
                print('reqRno_value', reqRno_value)

                print('success')
                return (reqRno_value, param)
            else:
                print('no schedule')
                return (None, None)
            
        except Exception as e:
            print(f"Error get_available_ship: {str(e)}")
   
   # 공백을 '+'로 대체하는 함수
    def replace_space_with_plus(self, param):
        for key, value in param.items():
            if isinstance(value, str):  # 값이 문자열인 경우에만 처리
                param[key] = value.replace(" ", "+")
        return param
    
    def get_freight_data(self, reqRno_value, schedule_param):
        print('schedule_param', schedule_param)
        # 선사 스케줄 클릭
        try:
            # 운임 확인 api 요청 url
            def interceptor(request):
                token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZXNzSWQiOiJfbW1xdmNlb3p4LVFQUE94Z0lsZEJqMUhieDFselZTNXQ4MTZZVzY5LTE1MjE1MiIsInVzZXJJZCI6IllPTDAwM18wMDEiLCJvcmdVc2VySWQiOiJZT0xDQVJHTyIsInVzZXJOYW1lIjoi6rCV7J246recIiwidXNlckVuYW1lIjoiWU9MIElOQyIsImNzdENhdENkIjoiMDEiLCJ1c2VyVHlwZSI6IjkiLCJjc3RDZCI6IllPTDAwMyIsInN0YWZmRmxhZyI6Ik4iLCJ1c2VyQ3RyQ2QiOiJLUiIsImFkbWluIjpmYWxzZSwicm9sZSI6Ik1FTUJFUiIsInNlcnZpY2VMYW5nIjoiS09SIiwiaWF0IjoxNzMyNTE1NzEyLCJleHAiOjE3MzUxMDc3MTJ9.grChgt6ek7Ouf7e8Vx1OH-YPI74gaK46tig9To8vsvo'
                request.headers['Authorization'] = f'Bearer {token}'

            # 보내야하는 param
            # porCtrCd:KR
            # porPlcCd:PNC
            # dlyCtrCd:AE
            # dlyPlcCd:JEA
            # polNm:BUSAN+NEW+PORT,+KOREA
            # podNm:JEBEL+ALI,UNITED+ARAB+EMIRATES
            # etd:20241206
            # frtAppNo:
            # vslCd:HKS
            # vslNm:HAKATA+SEOUL
            # reqRno:000000492801

            self.driver.request_interceptor = interceptor
            # cntrTypCd가 'GP', 'RF'에 따라 달라짐
            self.driver.get(f'https://api.ekmtc.com/schedule/schedule/leg/pop-fre-surcharge?porCtrCd={schedule_param.get("startCtrCd")}&porPlcCd={schedule_param.get("startPlcCd")}&dlyCtrCd={schedule_param.get("destCtrCd")}&dlyPlcCd={schedule_param.get("destPlcCd")}&polNm={schedule_param.get("polNm")}&podNm={schedule_param.get("podNm")}&etd={schedule_param.get("etd")}&frtAppNo={""}&vslCd={schedule_param.get("vslCd")}&vslNm={schedule_param.get("vslNm")}&voyNo={schedule_param.get("voyNo")}&reqRno={reqRno_value}&cntrTypCd=GP')
            # https://api.ekmtc.com/schedule/schedule/leg/pop-fre-surcharge?porCtrCd=KR&porPlcCd=PNC&dlyCtrCd=AE&dlyPlcCd=JEA&polNm=BUSAN+NEW+PORT,+KOREA&podNm=JEBEL+ALI,UNITED+ARAB+EMIRATES&etd=20241206&frtAppNo=&vslCd=HKS&vslNm=HAKATA+SEOUL&reqRno=000000492801

            time.sleep(5)

            # 스케줄 검색 응답 결과 저장
            elements = self.driver.find_element(By.XPATH, '/html/body/pre')

            json_data = json.loads(elements.text)
            time.sleep(5)
            if json_data:
                with open(f'freight_data_{schedule_param.get("startPlcCd")}_{schedule_param.get("destPlcCd")}.json', 'w') as f:
                    json.dump(json_data, f)
                print("get_freight_data successfully")
                return json_data
        
        except Exception as e:
            print(f"Error get_freight_data: {str(e)}")
            raise Exception("에러에러에러!!")

    def logout(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'logout_button_selector').click()
            print("Logged out successfully")
        except Exception as e:
            print(f"Logout failed: {str(e)}")

    def make_freightTable_to_csv(self):
        try:
            query = "SELECT * FROM freightTable"
            data = pd.read_sql(query, conn)
            conn.close()
            data.to_excel('output.xlsx', index=False)
            
        except Exception as e:
            print(f"failed to make csv file: {str(e)}")

    def close(self):
        self.driver.quit()
        print("Driver closed")

if __name__ == "__main__":
    bot = FreightAutomation()

    bot.login()
    time.sleep(3)
    bot.set_port_export()

