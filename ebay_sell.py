from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from word2number import w2n

import ebay_error as ee

def sell(wait,driver):
    currentUrl=driver.current_url
    checkUrl="https://reg.ebay.com/reg/Upgrade"
    try:
        if checkUrl in currentUrl:
            sell_begining_address(wait,driver,"address")
            sell_begining_address(wait,driver,"city")
            sell_begining_address(wait,driver,"state")
            sell_begining_address(wait,driver,"zip")
            sell_begining_address(wait,driver,"phone")
            sell_begining_address_submit(driver)
            
        else:
           driver.find_element_by_xpath('//*[@id="meb-items-cnt"]/section[2]/div/span[3]/a').click()
           wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="w0-find-product-search-bar-search-field"]'))).send_keys("similer products")

    except:
        print("failur !!!!!!!!!!")

def sell_begining_address(wait,driver,statement):
    try:
        wait.until(EC.title_contains("Sign in or Register | eBay"))
        assert 'Sign in or Register | eBay' in driver.title

        import common as com
        print("enter your "+ statement +" !!!")
        user = com.talk("ok",statement)
        values=user.replace(" ", "")

        if statement=="address":
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="address1"]'))).send_keys(values)

        elif statement=="city":
            driver.find_element_by_xpath('//*[@id="city"]').send_keys(values)

        elif statement=="state":
            driver.find_element_by_xpath('//*[@id="state"]').send_keys(values)

        elif statement=="zip":
            driver.find_element_by_xpath('//*[@id="zip"]').send_keys(values)

        elif statement=="phone":
            driver.find_element_by_xpath('//*[@id="phoneFlagComp1"]').send_keys(values)

    except Exception as e:
        print('Page Loading Failure' ,format(e))
        ee.check_error(wait,driver)

def sell_begining_address_submit(driver):
    try:
        driver.find_element_by_xpath('//*[@id="s0-0-17-2-meuiAppShell-20-2-welcome-screen-dialog-me-dialog-body"]/footer/button').click()

    except Exception as e:
        print("cannot click sell_begining_address_submit button : " ,format(e))