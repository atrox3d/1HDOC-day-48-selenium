import os
import glob
import pathlib
import time
from pprint import pprint

import selenium
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

DEFAULT_CHROMEDRIVER_PATH = "../chromedrivers"


def get_latestdriverpath(path=DEFAULT_CHROMEDRIVER_PATH):
    """get the most recent driver path, based on filename, ie. chrome.82.exe, chrome.92.exe"""
    path = os.path.abspath(path)
    if not os.path.isdir(path):
        raise SystemExit(f"path does not exist: {path}")
    try:
        pwd = os.getcwd()
        os.chdir(path)
        files = glob.glob(f"*.exe")
        # print(sorted(files))
        os.chdir(pwd)
        return os.path.join(path, sorted(files).pop())
    except OSError as e:
        print(repr(e))
        raise SystemExit(e)


def get_chromedriver(path=DEFAULT_CHROMEDRIVER_PATH, options=None):
    """gets last chromedriver"""
    try:
        driver_path = get_latestdriverpath(path)
        driver = webdriver.Chrome(executable_path=driver_path, options=options)
        return driver
    except Exception as e:
        raise SystemExit(repr(e))


def create_detached_browser(url):
    """creates a detached browser session, returns and prints _url, session_id"""
    options = Options()
    options.add_experimental_option("detach", True)
    driver = get_chromedriver(options=options)
    try:
        print(f"apertura {url} ...")
        driver.get(url)
        _url = driver.command_executor._url  # "http://127.0.0.1:60622/hub"
        session_id = driver.session_id  # '4e167f26-dc1d-4f51-a207-f761eaf73c31'
        # print(f"{_url       = }")
        # print(f"{session_id = }")
        return _url, session_id
    except WebDriverException as wde:
        print(wde)


def attach_session(url, _url, session_id):
    """attach to detached session"""
    driver = webdriver.Remote(command_executor=_url, desired_capabilities={})
    driver.close()  # this prevents the dummy browser
    driver.session_id = session_id

    driver.get(url)
    return driver


if __name__ == '__main__':
    # CHROME_DRIVER_PATH = "../chromedriver.92"  # .exe
    CHROME_DRIVER_PATH = get_latestdriverpath()
    print(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.get("https://www.ilpiemontetivaccina.it")
    time.sleep(10)
    driver.close()
