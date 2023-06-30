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
driver.get("https://www.ukr.net/")
time.sleep(2)
input_element = driver.find_element(By.XPATH, '//*[@id="search-input"]')
input_element.send_keys("новини")
assert driver.find_element(By.XPATH, '//*[@id="search-input"]')
time.sleep(2)
driver.close()
