from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyperclip
from dotenv import load_dotenv
import os
import time
import schedule


option = Options()

# 알림창 끄기
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2 # 알림 차단
})


# 1. 브라우저 열기
# driver = webdriver.Chrome()
driver = webdriver.Chrome(option)
driver.get("https://www.yolcargo.com/login")

def login():

    print("로그인 실행중...")
            # load .env
    load_dotenv()
    id = os.environ.get('ID')
    pw = os.environ.get('PW')
    print(id, pw)
    
    try:  
        # 2. 아이디 입력
        pyperclip.copy(id)
        id_input = driver.find_element(By.CSS_SELECTOR, "#input-23")
        # time.sleep(1)
        # id_input.send_keys(Keys.COMMAND, "v")
        id_input.send_keys(id)

        # 3. 비밀번호 입력
        pyperclip.copy(pw)
        pw_input = driver.find_element(By.CSS_SELECTOR, "#input-25")
        time.sleep(1)

        # pw_input.send_keys(Keys.COMMAND, "v")
        pw_input.send_keys(pw)
        time.sleep(2)

        # 4. 로그인 버튼 클릭
        driver.find_element(By.CSS_SELECTOR, "#app > div > div > div.login_wrap > div.v-card.v-card--flat.v-theme--light.v-card--density-default.v-card--variant-elevated.login > button").click()
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
