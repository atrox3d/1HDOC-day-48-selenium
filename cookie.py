import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "c:/Users/nigga/code/python/100-days-of-code/chromedriver"  # .exe
driver = webdriver.Chrome(CHROME_DRIVER_PATH)


def get_money_value(money_text: str):
    money_text = money_text.replace(",", "")
    return int(money_text)


def get_money():
    money_tag = driver.find_element_by_css_selector("#money")
    money_text = money_tag.text
    money_value = get_money_value(money_text)
    return money_value


def get_price(id):
    tag = driver.find_element_by_css_selector(id)
    text = tag.text.split(" - ")[1]
    value = get_money_value(text)
    return value


driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_css_selector("#cookie")

money = get_money()
buy_cursor = get_price("#buyCursor b")
buy_grandma = get_price("#buyGrandma b")
buy_factory = get_price("#buyFactory b")
buy_mine = get_price("#buyMine b")
buy_shipment = get_price("#buyShipment b")
buy_alchemylab = get_price("div[id='buyAlchemy lab'] b")
buy_portal = get_price("#buyPortal b")
buy_timemachine = get_price("div[id='buytime machine'] b")

driver.quit()
exit()
try:
    while True:
        time_start = time.time()
        while time.time() < time_start + 5:
            cookie.click()

        money = int(money_tag.text)
        cursor = int(buy_cursor.text.split(" - ")[1])
        time.sleep(2)
except selenium.common.exceptions.WebDriverException as wde:
    print(wde)
