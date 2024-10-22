from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyperclip
from dotenv import load_dotenv
import os
import time
import schedule
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


option = Options()

# 알림창 끄기
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2 # 알림 차단
})


# 1. 브라우저 열기
# driver = webdriver.Chrome()
driver = webdriver.Chrome(option)
driver.get("https://www.ekmtc.com/index.html#/main")

# def postLogin():
#     load_dotenv()
#     id = os.environ.get('ID')
#     pw = os.environ.get('PW')
#     print(id, pw)
#     time.sleep(3)
    
#     data={
#         "email":id,
#         "pass":pw,
#         "token":'recapcha_token',
#         'webtoken': 'cbnwTENL5z7tDDeHT6yNEK:APA91bHYL4P1JIhmqMQImr9-NUDOzp04XrFeVhPDhky4mgXq27lH3rmhwplw7LoELyRWHSG9BRzsafG2wJ1Vpv515TXxKuennsMWn_O0O_u281EEVhR84VLBVzg3FspKjVJUT5mTAXFk',
#         "device" : 'pc',
#         'language': 'kr'
#     }
#     session = requests.session()
#     response=session.post("https://www.yolcargo.com/signin", data=data)
    
#     print(response.json())

#     resHTML = session.get("https://www.yolcargo.com/login")
#     print(resHTML.text)
# postLogin()

def findNextMonth():
    driver.find_element(By.CSS_SELECTOR, '#frmLeg > div:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(2) > span:nth-child(1) > div > div > input').click()

    calendar_visible = driver.find_element(By.ID, "MonthPicker_").is_displayed()

    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "MonthPicker_")))

    if calendar_visible:
        driver.find_element(By.CLASS_NAME, 'button-11').click()
    #     for i in range(1, 5):
    #         for j in range(1, 4):
    #             css = f"#MonthPicker_ > div:nth-child(2) > table > tbody > tr:nth-child({j}) > td:nth-child({j}) > a"
    #             month = driver.find_element(By.CSS_SELECTOR, css)

    #             if month.text == '11월':
    #                 month.click()
                    #MonthPicker_ > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(1) > a
                    #MonthPicker_ > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(1) > a
            # element를 사용하여 필요한 작업 수행, 예를 들어 텍스트를 출력
                # print(month.text)


    #MonthPicker_ > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(1) > a > span
    #MonthPicker_ > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(2) > a > span
    #MonthPicker_ > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(3) > a > span
    #MonthPicker_ > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(1) > a > span
    #MonthPicker_ > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(1) > a > span

def findFreight():
    # date15 = driver.find_element(By.CSS_SELECTOR, 'body > div:nth-child(1) > div.wrap.wrap_KOR > div.container_ekmtc > div.content > div > div.tabs-details > div:nth-child(1) > div > div:nth-child(2) > div > div.sc_calender_type > table > tbody > tr:nth-child(3) > td:nth-child(3)')

    # 첫번째 선사 선택
    # ship = date15.find_element(By.CLASS_NAME, 'finish')
    # ship.click()

    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/table/tbody/tr[3]/td[3]/div/div/div[27]/div/div/p/a').click()
    time.sleep(3)

    # 운임확인 버튼 클릭
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[4]/div/a[1]').click()

    time.sleep(3)

    headers = {
        'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZXNzSWQiOiJCZExuOWoyc3BkY1AzaWNfSHRtWUhocnRUR1VFS2t3cFdxUGNuUzc0LTExMjAyMyIsInVzZXJJZCI6IllPTDAwM18wMDEiLCJvcmdVc2VySWQiOiJZT0xDQVJHTyIsInVzZXJOYW1lIjoi6rCV7J246recIiwidXNlckVuYW1lIjoiWU9MIElOQyIsImNzdENhdENkIjoiMDEiLCJ1c2VyVHlwZSI6IjkiLCJjc3RDZCI6IllPTDAwMyIsInN0YWZmRmxhZyI6Ik4iLCJ1c2VyQ3RyQ2QiOiJLUiIsImFkbWluIjpmYWxzZSwicm9sZSI6Ik1FTUJFUiIsInNlcnZpY2VMYW5nIjoiS09SIiwiaWF0IjoxNzI5NTYzNjIzLCJleHAiOjE3MzIyNDIwMjN9.dA2zge3Sna-9ryzbVFVWFrGcfG3vOG-SGCEXoiE3x1c',
        # 'User-Agent': 'MyUserAgent/1.0',
        }
    
    session = requests.session()

    res = session.get('https://api.ekmtc.com/schedule/schedule/leg/pop-fre-surcharge?porCtrCd=KR&porPlcCd=PUS&dlyCtrCd=HK&dlyPlcCd=HKG&polNm=BUSAN,KOREA&podNm=HONG+KONG&etd=20241112&frtAppNo=&vslCd=JTGZ&vslNm=TS+GUANGZHOU&voyNo=24019S&rteCd=KTH&eiCatCd=O&frtResult=&reqRno=000000473452&bkgClose=N&raTsParam=&promotionChk=N&scenarioCd=&promoNo=&kmtcSpotYn=Y&kmtcPremiumNegoYn=Y&etaBookingMsg=&hongkongTsYn=&hongkongTsMsg=&detailResp2=%7B%22tsDegree%22:%220%22,%22vslNm1%22:%22TS+GUANGZHOU%22,%22voyNo%22:%2224019S%22,%22rteCd%22:%22KTH%22,%22polNm%22:%22BUSAN,KOREA%22,%22podNm%22:%22HONG+KONG%22,%22pod1Nm%22:%22HONG+KONG%22,%22transitTime%22:%226%EC%9D%BC+4%EC%8B%9C%EA%B0%84+%22,%22transitTime1%22:%226%EC%9D%BC+4%EC%8B%9C%EA%B0%84+%22,%22polEtbDT%22:%222024.11.12+08:00%22,%22etdDT%22:%222024.11.12+19:00%22,%22polTml%22:%22BPTG+(Busan+Port+Terminal+(GAMMAN))%22,%22polTmlCd%22:%22BPTG%22,%22etaDT%22:%222024.11.18+23:00%22,%22podTml%22:%22HIT+(Hongkong+International+Terminal)%22,%22vslNm2%22:%22%22,%22voyNo2%22:%22%22,%22rteCd2%22:%22%22,%22pod2Nm%22:%22%22,%22transitTime2%22:%22%22,%22polEtbDT2%22:%22%22,%22polTml2%22:%22%22,%22etaDT2%22:%22%22,%22podTml2%22:%22%22,%22vslNm3%22:%22%22,%22voyNo3%22:%22%22,%22rteCd3%22:%22%22,%22pod3Nm%22:%22%22,%22transitTime3%22:%22%22,%22polEtbDT3%22:%22%22,%22polTml3%22:%22%22,%22etaDT3%22:%22%22,%22podTml3%22:%22%22,%22vslNm4%22:%22%22,%22voyNo4%22:%22%22,%22rteCd4%22:%22%22,%22pod4Nm%22:%22%22,%22transitTime4%22:%22%22,%22polEtbDT4%22:%22%22,%22polTml4%22:%22%22,%22etaDT4%22:%22%22,%22podTml4%22:%22%22,%22bkgDocCls%22:%222024.11.08+11:00%22,%22bkgCgoCls%22:%222024.11.12+02:00%22,%22bkgMfCls%22:%222024.11.08+11:00%22,%22cfsCls%22:%222024.11.08+16:00%22,%22mrnNo%22:%22%22,%22apoTcnt%22:%22%22,%22callSign%22:%22V7A5825%22,%22ts%22:%22N%22,%22vslCd%22:%22JTGZ%22,%22pol%22:%22PUS%22,%22pod%22:%22HKG%22,%22bkgClose%22:%22N%22,%22dtBkgYn%22:%22N%22,%22bkgVslCd%22:%22JTGZ%22,%22bkgVoyNo%22:%2224019S%22,%22kmtcSpotLineYn%22:%22Y%22,%22kmtcSpotUserYn%22:%22Y%22,%22kmtcSpotClosYn%22:%22N%22,%22etd%22:%2220241112%22,%22etdTm%22:%221900%22,%22eta%22:%2220241118%22,%22etaTm%22:%222300%22,%22vslNm%22:%22TS+GUANGZHOU%22,%22polEta%22:%22202411120800%22,%22polEtd%22:%22202411121900%22,%22podTmlCd%22:%22HIT%22,%22polCtrCd%22:%22KR%22,%22podCtrCd%22:%22HK%22,%22vgmDocCls%22:%222024.11.08+11:00%22,%22frtResult%22:%22A%22,%22frtAppNo%22:%22%22,%22reqRno%22:%22000000473452%22%7D&urlOrNot=false&cntrTypCd=GP', headers=headers)
    print(res.json())




def login():

    try:  
        driver.find_element(By.CSS_SELECTOR, "body > div > div.wrap.wrap_KOR > div.header > div.inner_header > div.wrap_util > ul > li:nth-child(2) > a").click()

        # print("로그인 실행중...")
            # load .env
        load_dotenv()
        id = os.environ.get('ID')
        pw = os.environ.get('PW')
        print(id, pw)
        # 2. 아이디 입력
        # pyperclip.copy(id)
        id_input = driver.find_element(By.CSS_SELECTOR, "#id")
        # time.sleep(1)
        # id_input.send_keys(Keys.COMMAND, "v")
        id_input.send_keys(id)

        # 3. 비밀번호 입력
        # pyperclip.copy(pw)
        pw_input = driver.find_element(By.CSS_SELECTOR, "#pw")
        time.sleep(1)

        # pw_input.send_keys(Keys.COMMAND, "v")
        pw_input.send_keys(pw)
        time.sleep(2)

        # 4. 로그인 버튼 클릭
        driver.find_element(By.CSS_SELECTOR, "body > div > div.wrap.wrap_KOR > div.header > div.inner_header > div.wrap_util > div.loginLayer_wrap > fieldset > div.btnarea > a.button.blue.sm").click()
        time.sleep(7)

        # 프로필 선택
        driver.find_element(By.CSS_SELECTOR, '#profile_pop > div > div.content_box > ul > li:nth-child(2) > p.img > img').click()
        time.sleep(5)


        driver.get('https://www.ekmtc.com/index.html#/schedule/leg')
        time.sleep(10)

        # 구간 선택
        departPort = driver.find_element(By.CSS_SELECTOR, '#autocomplete-form-input')
        # departPort.click()
        departPort.send_keys('Busan, Korea (PUS)')

        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/form/div[1]/table/tbody/tr[1]/td[1]/div/div[2]/button[1]")))

        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/form/div[1]/table/tbody/tr[1]/td[1]/div/div[2]/button[1]').click()
        time.sleep(3)

        # if btn:
        #     driver.find_element(By.CSS_SELECTOR, '#autocomplete_1729495963260_1570 > button').click()
        #     print('auto click')

        arrivePort = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/form/div[1]/table/tbody/tr[1]/td[2]/div/div[1]/input')
        arrivePort.send_keys('Hong Kong (HKG)')
        # arrivePort.click()
        # time.sleep(3)
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/form/div[1]/table/tbody/tr[1]/td[2]/div/div[2]/button[1]")))

        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/form/div[1]/table/tbody/tr[1]/td[2]/div/div[2]/button[1]').click()
        time.sleep(3)

        
        findNextMonth()
        
        # date.send_keys('2024.11')
        time.sleep(3)

        driver.find_element(By.CSS_SELECTOR, '#frmLeg > div.position_relative > span > a').click()

        time.sleep(3)

        findFreight()


    except Exception as e:
        print(f'{str(e)}')
    finally:
        print('login success')
login()


def logout():
    try: 
        print('로그아웃 실행중..')
        driver.find_element(By.CSS_SELECTOR, '#app > div > div > header > div > div.v-btn-group.v-theme--light.v-btn-group--density-default.header_submenu > div.v-btn-group.v-theme--light.v-btn-group--density-default.header_submenu_sign.hidden-sm-and-down > button').click()
    except Exception as e:
        print(f'{str(e)}')
    finally:
        print('logout success')
        
# schedule.every(10).seconds.do(login)

# step4.스캐쥴 시작
# while True:
#     schedule.run_pending()
#     time.sleep(1)
    # logout()    


# response = requests.get(url)

# if response.status_code == 200:
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     # print(soup.prettify())
#     # copy css selector
#     # select_one => html 요소 추출
#     title = soup.select_one('a.MyView-module__link_login___HpHMW')
#     print(title)
#     # print(title.get_text()) # get_text() text만 추출

# else : 
#     print(response.status_code)
