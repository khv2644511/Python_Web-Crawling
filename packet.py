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

class FreightAutomation:
    def __init__(self):
        self.driver = self.initialize_driver()
        self.login_url = "https://www.ekmtc.com"
        self.schedule_url = "https://www.ekmtc.com/index.html#/schedule/leg"
        load_dotenv()
        self.id = os.getenv('ID')
        self.pw = os.getenv('PW')

    # def initialize_driver(self):
    #     # options = Options()
    #     options = webdriver.ChromeOptions()
    #     options.add_argument('--no-sandbox')
    #     options.add_argument('--window-size=1280,920')
    #     options.add_argument('--disable-dev-shm-usage')
    #     # options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    #     chrome_driver_path = ChromeDriverManager().install()
    #     service = Service(chrome_driver_path)
    #     return webdriver.Chrome(service=service, options=options)

    def initialize_driver(self):

        options = {
            'disable_encoding': True  # This can help capture binary data without corruption
            # Add other necessary options
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

    def set_port(self):
        try:
            time.sleep(5)

            # self.driver.get(self.schedule_url)
            # self.schedule_url = "https://www.ekmtc.com/index.html#/schedule/leg"
            self.driver.get("https://www.ekmtc.com/index.html#/schedule/leg")
            time.sleep(5)

            def interceptor(request):
                token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZXNzSWQiOiJBZDBpRVBwZ19WY0tkTUhxcXdLaVFmUEZRMENFQWJsaGtEaUZwNmhyLTEzNDU0OCIsInVzZXJJZCI6IllPTDAwM18wMDEiLCJvcmdVc2VySWQiOiJZT0xDQVJHTyIsInVzZXJOYW1lIjoi6rCV7J246recIiwidXNlckVuYW1lIjoiWU9MIElOQyIsImNzdENhdENkIjoiMDEiLCJ1c2VyVHlwZSI6IjkiLCJjc3RDZCI6IllPTDAwMyIsInN0YWZmRmxhZyI6Ik4iLCJ1c2VyQ3RyQ2QiOiJLUiIsImFkbWluIjpmYWxzZSwicm9sZSI6Ik1FTUJFUiIsInNlcnZpY2VMYW5nIjoiS09SIiwiaWF0IjoxNzI5NzQ1MTQ4LCJleHAiOjE3MzI0MjM1NDh9.JACVS2Ki0YukSEM3QCwgutyESKNrK6mK9ww5yEb8w2I'
                request.headers['Authorization'] = f'Bearer {token}'

            self.driver.request_interceptor = interceptor
            # headers = {
            #     'Authorization': f'Bearer {token}'  # Ensure the token is prefixed with 'Bearer' if required by the API
            # }
            param = {
                "startPlcCd": "PUS",
                "searchMonth": "11",
                "bound": "O",
                "startPlcName": "Busan, Korea (PUS)",
                "destPlcCd": "HKG",
                "searchYear": "2024",
                "filterYn": "N",
                "searchYN": "Y",
                "startCtrCd": "KR",
                "destCtrCd": "HK",
                "destPlcName": "Hong Kong (HKG)",
                "main": "N",
                "legIdx": "0",
                "vslType01": "01",
                "vslType03": "03",
                "eiCatCd": "O",
                "calendarOrList": "C",
                "cpYn": "N",
                "promotionChk": "N",

            }
            
            self.driver.get('https://api.ekmtc.com/schedule/schedule/leg/search-schedule?startPlcCd=PUS&searchMonth=11&pointChangeYN=&bound=O&filterPolCd=&pointLength=&startPlcName=Busan,+Korea+(PUS)&destPlcCd=HKG&searchYear=2024&filterYn=N&searchYN=Y&filterPodCd=&hiddestPlcCd=&startCtrCd=KR&destCtrCd=HK&polTrmlStr=&podTrmlStr=&rteCd=&filterTs=Y&filterDirect=Y&filterTranMax=0&filterTranMin=0&hidstartPlcCd=&destPlcName=Hong+Kong+(HKG)&main=N&legIdx=0&vslType01=01&vslType03=03&unno=&commodityCd=&eiCatCd=O&calendarOrList=C&cpYn=N&promotionChk=N&vslCd=&voyNo=')
            # requests.get('https://api.ekmtc.com/schedule/schedule/leg/search-schedule', params=param)
            time.sleep(5)

            # 스케줄 검색 응답 결과 저장
            elements = self.driver.find_element(By.XPATH, '/html/body/pre')
            # print(elements.text)

            json_data = json.loads(elements.text)
            time.sleep(5)
            with open('schedule.json', 'w') as f:
                json.dump(json_data, f)

           
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
            # def interceptor(request):
            #     token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZXNzSWQiOiJBZDBpRVBwZ19WY0tkTUhxcXdLaVFmUEZRMENFQWJsaGtEaUZwNmhyLTEzNDU0OCIsInVzZXJJZCI6IllPTDAwM18wMDEiLCJvcmdVc2VySWQiOiJZT0xDQVJHTyIsInVzZXJOYW1lIjoi6rCV7J246recIiwidXNlckVuYW1lIjoiWU9MIElOQyIsImNzdENhdENkIjoiMDEiLCJ1c2VyVHlwZSI6IjkiLCJjc3RDZCI6IllPTDAwMyIsInN0YWZmRmxhZyI6Ik4iLCJ1c2VyQ3RyQ2QiOiJLUiIsImFkbWluIjpmYWxzZSwicm9sZSI6Ik1FTUJFUiIsInNlcnZpY2VMYW5nIjoiS09SIiwiaWF0IjoxNzI5NzQ1MTQ4LCJleHAiOjE3MzI0MjM1NDh9.JACVS2Ki0YukSEM3QCwgutyESKNrK6mK9ww5yEb8w2I'
            #     request.headers['Authorization'] = f'Bearer {token}'
            # # self.driver.get('https://api.ekmtc.com/schedule/schedule/leg/vsl-schedule-info-detail?bound=O&podPortCd=HKG&polPortCd=PUS&voyNo=2408S&vslCd=JSKC&polTrmlCd=HBGT')

            # # 운임 확인 api 요청 url
            # self.driver.request_interceptor = interceptor
            token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZXNzSWQiOiJBZDBpRVBwZ19WY0tkTUhxcXdLaVFmUEZRMENFQWJsaGtEaUZwNmhyLTEzNDU0OCIsInVzZXJJZCI6IllPTDAwM18wMDEiLCJvcmdVc2VySWQiOiJZT0xDQVJHTyIsInVzZXJOYW1lIjoi6rCV7J246recIiwidXNlckVuYW1lIjoiWU9MIElOQyIsImNzdENhdENkIjoiMDEiLCJ1c2VyVHlwZSI6IjkiLCJjc3RDZCI6IllPTDAwMyIsInN0YWZmRmxhZyI6Ik4iLCJ1c2VyQ3RyQ2QiOiJLUiIsImFkbWluIjpmYWxzZSwicm9sZSI6Ik1FTUJFUiIsInNlcnZpY2VMYW5nIjoiS09SIiwiaWF0IjoxNzI5NzQ1MTQ4LCJleHAiOjE3MzI0MjM1NDh9.JACVS2Ki0YukSEM3QCwgutyESKNrK6mK9ww5yEb8w2I'

            # request.headers['Authorization'] = f'Bearer {token}'
            header = {
                'Authorization': f'Bearer {token}'
            }
            requests.get(f'https://api.ekmtc.com/schedule/schedule/leg/pop-fre-surcharge?porCtrCd=KR&porPlcCd=PUS&dlyCtrCd=HK&dlyPlcCd=HKG&polNm=BUSAN,KOREA&podNm=HONG+KONG&etd=20241115&frtAppNo=&vslCd=JSKC&vslNm=SKY+CHALLENGE&voyNo=2408', headers=header)
            # self.driver.get(f'https://api.ekmtc.com/schedule/schedule/leg/pop-fre-surcharge?porCtrCd=KR&porPlcCd=PUS&dlyCtrCd=HK&dlyPlcCd=HKG&polNm=BUSAN,KOREA&podNm=HONG+KONG&etd=20241115&frtAppNo=&vslCd=JSKC&vslNm=SKY+CHALLENGE&voyNo=2408S&reqRno={reqRno_value}')
            # request = self.driver.wait_for_request('/schedule/schedule/leg/pop-fre-surcharge/*', timeout=30)
            # print('response =', response.status_code)
           
            time.sleep(5)

            # 스케줄 검색 응답 결과 저장
            elements = self.driver.find_element(By.XPATH, '/html/body/pre')
            # print(elements.text)

            json_data = json.loads(elements.text)
            time.sleep(5)
            with open('freight_data.json', 'w') as f:
                json.dump(json_data, f)

            print("get_freight_data successfully")

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
    reqRno_value = bot.set_port()
    time.sleep(2)
    # bot.set_next_month() 
    # time.sleep(3)
    # bot.check_freight()
    # time.sleep(3)
    bot.get_freight_data(reqRno_value)
    # bot.check_freight()
    # bot.logout()
    # bot.close()
