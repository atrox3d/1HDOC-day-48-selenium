import os
import glob
import pathlib
import time
from pprint import pprint

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_latestdriverpath(path):
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


if __name__ == '__main__':
    # CHROME_DRIVER_PATH = "../chromedriver.92"  # .exe
    # driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    CHROME_DRIVER_PATH = get_latestdriverpath("../chromedrivers")
    print(CHROME_DRIVER_PATH)