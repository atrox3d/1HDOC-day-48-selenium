from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "c:/Users/nigga/code/python/100-days-of-code/chromedriver"  # .exe
driver = webdriver.Chrome(CHROME_DRIVER_PATH)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_css_selector("#cookie")
while True:
    time.sleep(1)
    cookie.click()
