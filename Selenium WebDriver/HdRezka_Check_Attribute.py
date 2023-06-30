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
driver.get("https://rezka.ag/films/best/")
time.sleep(2)
input_element = driver.find_element(By.XPATH, '//*[@id="search-field"]')
input_element.send_keys("во все тяжкие")
input_element.send_keys(Keys.RETURN)
time.sleep(2)
assert "во все тяжкие" in driver.page_source
driver.close()
