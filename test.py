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
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")

time.sleep(1)

# 2. 아이디 입력
pyperclip.copy(id)
driver.find_element(By.ID, "id").send_keys(Keys.COMMAND, "v")
time.sleep(1)

# 3. 비밀번호 입력
pyperclip.copy(pw)
driver.find_element(By.ID, "pw").send_keys(Keys.COMMAND, "v")
time.sleep(1)

# 4. 로그인 버튼 클릭
driver.find_element(By.ID, "log.login").click()

time.sleep(7)
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
