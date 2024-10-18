from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
from dotenv import load_dotenv
import os

# load .env
load_dotenv()

id = os.environ.get('ID')
pw = os.environ.get('PW')

# 1. 브라우저 열기
driver = webdriver.Chrome()
driver.get("https://www.yolcargo.com/login")

def login():
    # 2. 아이디 입력
    pyperclip.copy(id)

    # elements = driver.find_element(By.CSS_SELECTOR, "#input-23")
    # print(elements)
    driver.find_element(By.CSS_SELECTOR, "#input-23").send_keys(Keys.COMMAND, "v")
    time.sleep(1)

    # 3. 비밀번호 입력
    pyperclip.copy(pw)
    driver.find_element(By.CSS_SELECTOR, "#input-25").send_keys(Keys.COMMAND, "v")
    time.sleep(1)

    # 4. 로그인 버튼 클릭
    driver.find_element(By.CSS_SELECTOR, "#app > div > div > div.login_wrap > div.v-card.v-card--flat.v-theme--light.v-card--density-default.v-card--variant-elevated.login > button").click()
    time.sleep(7)

login()
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
