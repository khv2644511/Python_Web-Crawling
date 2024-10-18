import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://www.google.com'

driver.get(url)

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    # copy css selector
    # select_one => html 요소 추출
    title = soup.select_one('a.MyView-module__link_login___HpHMW')
    print(title)
    # print(title.get_text()) # get_text() text만 추출

else : 
    print(response.status_code)
