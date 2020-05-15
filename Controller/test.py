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
wait = WebDriverWait(driver, 50)

driver.get("https://www.aliexpress.com/item/32969951619.html?spm=a2g0o.productlist.0.0.10a027c9UKlAN8&s=p&ad_pvid=2020051005023912852232612020007719627_1&algo_pvid=ef0a37e9-0d95-4caa-8509-0aa59d969bae&algo_expid=ef0a37e9-0d95-4caa-8509-0aa59d969bae-0&btsid=0ab6f82c15891121589823537e2059&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_")
txt_quantity='//*[@id="root"]/div/div[2]/div/div[2]/div[8]/span/span/span[2]/input'
ad_close='/html/body/div[10]/div[2]/div/a'
try:
    
    wait.until(EC.element_to_be_clickable((By.XPATH,txt_quantity))).send_keys(Keys.CONTROL, 'a')
    wait.until(EC.element_to_be_clickable((By.XPATH,txt_quantity))).send_keys(5)
    # wait.until(EC.element_to_be_clickable((By.XPATH,ad_close))).click()
except Exception as identifier:
    print(identifier)