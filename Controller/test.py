from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from word2number import w2n

import ebay_error as ee
import sys
import speech as sp

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

global driver

driver = webdriver.Chrome('C:\Windows\chromedriver.exe', options=chrome_options)
wait = WebDriverWait(driver, 10)


driver.get("http://google.com")
windowHandle  = driver.window_handles()
driver.find_element_by_css_selector("body").send_keys(Keys.CONTROL + "t")

ArrayList tabs = new ArrayList (driver.getWindowHandles());
System.out.println(tabs.size());
driver.switchTo().window(tabs.get(0)); 

driver.get("https://stackoverflow.com/questions/34948175/switching-and-focusing-a-newly-opened-tab-in-selenium");
driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[3]/a').click()