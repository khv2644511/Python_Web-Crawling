# from selenium import webdriver
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
import requests
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='khv032900!', db='pythonDB', charset='utf8')


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

    def set_port_export(self):
        cur = conn.cursor()

        sql = "SELECT ctrCd,plcCd,plcEnm FROM portTable pt WHERE ctrCd = 'kr'"
        cur.execute(sql)
        result = cur.fetchall()
        for item in result:

            ctrCd, plcCd, plcName = item
            # 문자열 공백을 +로 채워서 params를 보내야함
            if isinstance(plcName, str):
                plcName = plcName.replace(" ", "+")
            
            # print((ctrCd, plcCd, plcName))
            param = {
                "startPlcCd": plcCd, # "PUS"
                "searchMonth": "11", #
                "startPlcName": plcName, #"Busan, Korea (PUS)"
                "destPlcCd": "HKG", #
                "searchYear": "2024", #
                "startCtrCd": ctrCd, #"KR"
                "destCtrCd": "HK", #
                "destPlcName": "Hong Kong (HKG)", #
            }
            reqRno_value = self.set_port(param)
            time.sleep(2)  
            self.get_freight_data(reqRno_value)
        
    def set_port(self, param):
        try:
            time.sleep(5)

            self.driver.get("https://www.ekmtc.com/index.html#/schedule/leg")
            time.sleep(5)

            def interceptor(request):
                token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZXNzSWQiOiJBZDBpRVBwZ19WY0tkTUhxcXdLaVFmUEZRMENFQWJsaGtEaUZwNmhyLTEzNDU0OCIsInVzZXJJZCI6IllPTDAwM18wMDEiLCJvcmdVc2VySWQiOiJZT0xDQVJHTyIsInVzZXJOYW1lIjoi6rCV7J246recIiwidXNlckVuYW1lIjoiWU9MIElOQyIsImNzdENhdENkIjoiMDEiLCJ1c2VyVHlwZSI6IjkiLCJjc3RDZCI6IllPTDAwMyIsInN0YWZmRmxhZyI6Ik4iLCJ1c2VyQ3RyQ2QiOiJLUiIsImFkbWluIjpmYWxzZSwicm9sZSI6Ik1FTUJFUiIsInNlcnZpY2VMYW5nIjoiS09SIiwiaWF0IjoxNzI5NzQ1MTQ4LCJleHAiOjE3MzI0MjM1NDh9.JACVS2Ki0YukSEM3QCwgutyESKNrK6mK9ww5yEb8w2I'
                request.headers['Authorization'] = f'Bearer {token}'

            self.driver.request_interceptor = interceptor

            print('param', param.get('startPlcCd'))

            self.driver.get(f"https://api.ekmtc.com/schedule/schedule/leg/search-schedule?startPlcCd={param.get('startPlcCd')}&searchMonth={param.get('searchMonth')}&pointChangeYN=&bound=O&filterPolCd=&pointLength=&startPlcName={param.get('startPlcName')}&destPlcCd={param.get('destPlcCd')}&searchYear=2024&filterYn=N&searchYN=Y&filterPodCd=&hiddestPlcCd=&startCtrCd=KR&destCtrCd=HK&polTrmlStr=&podTrmlStr=&rteCd=&filterTs=Y&filterDirect=Y&filterTranMax=0&filterTranMin=0&hidstartPlcCd=&destPlcName=Hong+Kong+(HKG)&main=N&legIdx=0&vslType01=01&vslType03=03&unno=&commodityCd=&eiCatCd=O&calendarOrList=C&cpYn=N&promotionChk=N&vslCd=&voyNo=")
            
            # self.driver.get(f'https://api.ekmtc.com/schedule/schedule/leg/search-schedule?startPlcCd={param.get("startPlcCd")}&searchMonth={param.get("searchMonth")}&startPlcName={param.get("startPlcName")}&destPlcCd={param.get("destPlcCd")}&searchYear={param.get("searchYear")}')
            time.sleep(5)

            # 스케줄 검색 응답 결과 저장
            elements = self.driver.find_element(By.XPATH, '/html/body/pre')
            # print(elements.text)

            json_data = json.loads(elements.text)
            time.sleep(5)
            with open('schedule.json', 'w') as f:
                json.dump(json_data, f)

            #   schedule.json의 polEtd1 날짜
            print("port selected")

            time.sleep(5)
            
            # https://api.ekmtc.com/schedule/schedule/leg/pop-fre-app-no?porCtrCd=KR&porPlcCd=PUS&dlyCtrCd=HK&dlyPlcCd=HKG&eiCatCd=O&logYn=N&etd=20241122&promotionChk=N&vslCd=JSOR&voyNo=2415S&rteCd=KTS&hotDealYn=N&hotDealReqRno=&raTsParam=

            self.driver.get('https://api.ekmtc.com/schedule/schedule/leg/pop-fre-app-no?porCtrCd=KR&porPlcCd=PUS&dlyCtrCd=HK&dlyPlcCd=HKG&eiCatCd=O&logYn=N&etd=20241112&promotionChk=N&vslCd=&voyNo=&rteCd=KTS&hotDealYn=N&hotDealReqRno=&raTsParam=')
            getReqNo = self.driver.find_element(By.XPATH, '/html/body/pre')
            # print(elements.text)

            getReqNo_json_data = json.loads(getReqNo.text)

            reqRno_value = getReqNo_json_data.get("reqRno")
            print(reqRno_value)

            print('success')
            return reqRno_value
        except Exception as e:
            print(f"Error selecting set port: {str(e)}")

    # def set_next_month(self):
    #     try: 
    #         self.driver.find_element(By.CSS_SELECTOR, '#frmLeg > div:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(2) > span:nth-child(1) > div > div > input').click()


    #         WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.ID, "MonthPicker_")))

    #         time.sleep(4)
    #         self.driver.find_element(By.CLASS_NAME, 'button-11').click()
    #         time.sleep(3)
    #         self.driver.find_element(By.CSS_SELECTOR, '#frmLeg > div.position_relative > span > a').click()
    #         print("set_next_month successfully")

    #     except Exception as e:
    #         print(f"Error set next month: {str(e)}")
   

    # def check_freight(self):
    #     try:
    #         # Implementation to select the specific date and check freight rates
    #         self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[3]/td[3]/div/div/div[24]/div/div/p/a').click()
    #         time.sleep(3)

    #         # 운임확인 버튼 클릭
    #         self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[4]/div/a[1]').click()
    #         print("Freight checked")

    #     except Exception as e:
    #         print(f"Error checking freight: {str(e)}")

    def get_freight_data(self, reqRno_value):
        # 선사 스케줄 클릭
        try:
            # # 운임 확인 api 요청 url
            token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZXNzSWQiOiJBZDBpRVBwZ19WY0tkTUhxcXdLaVFmUEZRMENFQWJsaGtEaUZwNmhyLTEzNDU0OCIsInVzZXJJZCI6IllPTDAwM18wMDEiLCJvcmdVc2VySWQiOiJZT0xDQVJHTyIsInVzZXJOYW1lIjoi6rCV7J246recIiwidXNlckVuYW1lIjoiWU9MIElOQyIsImNzdENhdENkIjoiMDEiLCJ1c2VyVHlwZSI6IjkiLCJjc3RDZCI6IllPTDAwMyIsInN0YWZmRmxhZyI6Ik4iLCJ1c2VyQ3RyQ2QiOiJLUiIsImFkbWluIjpmYWxzZSwicm9sZSI6Ik1FTUJFUiIsInNlcnZpY2VMYW5nIjoiS09SIiwiaWF0IjoxNzI5NzQ1MTQ4LCJleHAiOjE3MzI0MjM1NDh9.JACVS2Ki0YukSEM3QCwgutyESKNrK6mK9ww5yEb8w2I'

            header = {
                'Authorization': f'Bearer {token}'
            }
            # requests.get(f'https://api.ekmtc.com/schedule/schedule/leg/pop-fre-surcharge?porCtrCd=KR&porPlcCd=PUS&dlyCtrCd=HK&dlyPlcCd=HKG&polNm=BUSAN,KOREA&podNm=HONG+KONG&etd=20241115&frtAppNo=&vslCd=JSKC&vslNm=SKY+CHALLENGE&voyNo=2408&reqRno_value={reqRno_value}', headers=header)

            def interceptor(request):
                token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZXNzSWQiOiJBZDBpRVBwZ19WY0tkTUhxcXdLaVFmUEZRMENFQWJsaGtEaUZwNmhyLTEzNDU0OCIsInVzZXJJZCI6IllPTDAwM18wMDEiLCJvcmdVc2VySWQiOiJZT0xDQVJHTyIsInVzZXJOYW1lIjoi6rCV7J246recIiwidXNlckVuYW1lIjoiWU9MIElOQyIsImNzdENhdENkIjoiMDEiLCJ1c2VyVHlwZSI6IjkiLCJjc3RDZCI6IllPTDAwMyIsInN0YWZmRmxhZyI6Ik4iLCJ1c2VyQ3RyQ2QiOiJLUiIsImFkbWluIjpmYWxzZSwicm9sZSI6Ik1FTUJFUiIsInNlcnZpY2VMYW5nIjoiS09SIiwiaWF0IjoxNzI5NzQ1MTQ4LCJleHAiOjE3MzI0MjM1NDh9.JACVS2Ki0YukSEM3QCwgutyESKNrK6mK9ww5yEb8w2I'
                request.headers['Authorization'] = f'Bearer {token}'

            self.driver.request_interceptor = interceptor
            self.driver.get(f'https://api.ekmtc.com/schedule/schedule/leg/pop-fre-surcharge?porCtrCd=KR&porPlcCd=PUS&dlyCtrCd=HK&dlyPlcCd=HKG&polNm=BUSAN,KOREA&podNm=HONG+KONG&etd=20241112&frtAppNo=&vslCd=KSG&vslNm=KMTC+SINGAPORE&voyNo=2415S&rteCd=KTS&eiCatCd=O&frtResult=&reqRno={reqRno_value}&bkgClose=N&raTsParam=&promotionChk=N&scenarioCd=&promoNo=&kmtcSpotYn=Y&kmtcPremiumNegoYn=Y&etaBookingMsg=&hongkongTsYn=&hongkongTsMsg=&detailResp2=%7B%22tsDegree%22:%220%22,%22vslNm1%22:%22KMTC+SINGAPORE%22,%22voyNo%22:%222415S%22,%22rteCd%22:%22KTS%22,%22polNm%22:%22BUSAN,KOREA%22,%22podNm%22:%22HONG+KONG%22,%22pod1Nm%22:%22HONG+KONG%22,%22transitTime%22:%223%EC%9D%BC+5%EC%8B%9C%EA%B0%84+30%EB%B6%84%22,%22transitTime1%22:%223%EC%9D%BC+5%EC%8B%9C%EA%B0%84+30%EB%B6%84%22,%22polEtbDT%22:%222024.11.11+14:00%22,%22etdDT%22:%222024.11.12+15:00%22,%22polTml%22:%22HBGT+(HUTCHISON+GAMMAN+TMNL(%231))%22,%22polTmlCd%22:%22HBGT%22,%22etaDT%22:%222024.11.15+20:30%22,%22podTml%22:%22HIT+(Hongkong+International+Terminal)%22,%22vslNm2%22:%22%22,%22voyNo2%22:%22%22,%22rteCd2%22:%22%22,%22pod2Nm%22:%22%22,%22transitTime2%22:%22%22,%22polEtbDT2%22:%22%22,%22polTml2%22:%22%22,%22etaDT2%22:%22%22,%22podTml2%22:%22%22,%22vslNm3%22:%22%22,%22voyNo3%22:%22%22,%22rteCd3%22:%22%22,%22pod3Nm%22:%22%22,%22transitTime3%22:%22%22,%22polEtbDT3%22:%22%22,%22polTml3%22:%22%22,%22etaDT3%22:%22%22,%22podTml3%22:%22%22,%22vslNm4%22:%22%22,%22voyNo4%22:%22%22,%22rteCd4%22:%22%22,%22pod4Nm%22:%22%22,%22transitTime4%22:%22%22,%22polEtbDT4%22:%22%22,%22polTml4%22:%22%22,%22etaDT4%22:%22%22,%22podTml4%22:%22%22,%22bkgDocCls%22:%222024.11.08+15:00%22,%22bkgCgoCls%22:%222024.11.11+06:00%22,%22bkgMfCls%22:%222024.11.08+15:00%22,%22cfsCls%22:%222024.11.08+12:00%22,%22mrnNo%22:%2224KMTC4656E%22,%22apoTcnt%22:%2214%22,%22callSign%22:%22DSOA9%22,%22ts%22:%22N%22,%22vslCd%22:%22KSG%22,%22pol%22:%22PUS%22,%22pod%22:%22HKG%22,%22bkgClose%22:%22N%22,%22dtBkgYn%22:%22N%22,%22bkgVslCd%22:%22KSG%22,%22bkgVoyNo%22:%222415S%22,%22kmtcSpotLineYn%22:%22Y%22,%22kmtcSpotUserYn%22:%22Y%22,%22kmtcSpotClosYn%22:%22N%22,%22etd%22:%2220241112%22,%22etdTm%22:%221500%22,%22eta%22:%2220241115%22,%22etaTm%22:%222030%22,%22vslNm%22:%22KMTC+SINGAPORE%22,%22polEta%22:%22202411111400%22,%22polEtd%22:%22202411121500%22,%22podTmlCd%22:%22HIT%22,%22polCtrCd%22:%22KR%22,%22podCtrCd%22:%22HK%22,%22vgmDocCls%22:%222024.11.08+15:00%22,%22frtResult%22:%22A%22,%22frtAppNo%22:%22%22,%22reqRno%22:%22000000473452%22%7D&urlOrNot=false&cntrTypCd=GP')

            time.sleep(5)

            # 스케줄 검색 응답 결과 저장
            elements = self.driver.find_element(By.XPATH, '/html/body/pre')
            # print(elements.text)

            json_data = json.loads(elements.text)
            time.sleep(5)
            with open('freight_data2.json', 'w') as f:
                json.dump(json_data, f)

            print("get_freight_data successfully")
            return json_data
        except Exception as e:
            print(f"Error get_freight_data: {str(e)}")

    def logout(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'logout_button_selector').click()
            print("Logged out successfully")
        except Exception as e:
            print(f"Logout failed: {str(e)}")

    def close(self):
        self.driver.quit()
        print("Driver closed")

if __name__ == "__main__":
    bot = FreightAutomation()

    bot.login()
    time.sleep(3)
    # reqRno_value = bot.set_port()
    bot.set_port_export()
    # time.sleep(2)
    # bot.set_next_month() 
    # time.sleep(3)
    # bot.check_freight()
    # bot.get_freight_data(reqRno_value)
    # time.sleep(3)
    # bot.insert_data_into_db(freight_data)
    # bot.check_freight()
    # bot.logout()
    # bot.close()
