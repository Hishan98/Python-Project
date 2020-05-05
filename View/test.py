from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from word2number import w2n

import sys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
global driver

driver = webdriver.Chrome('C:\Windows\chromedriver.exe', options=chrome_options)
wait = WebDriverWait(driver, 10)
def test():
    try:
        url='https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20200505061252&isPremium=y&SearchText=sticker+pack'
        driver.get(url)
        
        closead='/html/body/div[6]/div[2]/div/a'
        wait.until(EC.element_to_be_clickable((By.XPATH,closead))).click()
    
        mainlink='//*[@id="root"]/div/div/div[2]/div[2]/div/div[2]/ul/div[1]/li[1]/div/div[2]/div/div[1]/a'
        wait.until(EC.element_to_be_clickable((By.XPATH,mainlink))).click()

        getlist='//*[@id="root"]/div/div[2]/div/div[2]/div[7]/div/div[1]/ul'
        gettagname='sku-property-item'
        Selection=1
        getitem='//*[@id="root"]/div/div[2]/div/div[2]/div[7]/div/div/ul/li['+str(Selection)+']/div/img'

        wait.until(EC.element_to_be_clickable((By.XPATH,getitem)))

        html_list = driver.find_element_by_xpath(getlist)
        items = html_list.find_elements_by_class_name(gettagname)
        count =len(items)
        print("There are "+ str(count) +" items in this list")

        if Selection in range (count):
            try:
                driver.find_element_by_xpath(getitem).click()

            except Exception as identifier:
                print('Error occoured :' ,format(identifier))
        else:
            print("There is no such an item on this list")

    except Exception as e:
        print('error',format(e))
test()