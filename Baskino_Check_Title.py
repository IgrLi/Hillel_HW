from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("start-maximized")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service('"D:\chromedriver_win32\chromedriver.exe'), options=options)
driver.get("http://baskino.me/")
time.sleep(2)
assert "Онлайн фильмы в хорошем HD качестве бесплатно и без регистрации" in driver.title
time.sleep(3)
driver.close()