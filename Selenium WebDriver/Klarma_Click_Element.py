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
driver.get("https://klamra.com.ua/belt-buckles/")
time.sleep(2)
goButton = driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li[2]/a')
assert driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li[2]/a')
goButton.click()
time.sleep(4)

