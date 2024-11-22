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
from make_db import insert_data_into_db
import pandas as pd
import pymysql



conn = pymysql.connect(host='127.0.0.1', user='root', password='khv032900!', db='pythonDB', charset='utf8')

query = "SELECT * FROM portTable"

data = pd.read_sql(query, conn)

conn.close()

data.to_excel('output.xlsx', index=False)