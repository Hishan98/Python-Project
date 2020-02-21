from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Voice as vv
import ebay_error as ee

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

global driver

driver = webdriver.Chrome('C:\Windows\chromedriver.exe', options=chrome_options)
wait = WebDriverWait(driver, 10)
# text=""
def open():
    vv.talk()
def commands(text):
    
    if "login" in text: 
        ebay_sign_in()
    if "sign up" in text:  
        ebay_sign_up()
    if "search" in text: 
        search()
    if "exit" in text: 
        url='chrome//newtab'
        driver.get(url)

def ebay_sign_up():

    url='https://reg.ebay.com/reg/PartialReg'
    driver.get(url)

    try:
        wait.until(EC.title_contains("Sign in or Register | eBay"))
        assert 'Sign in or Register | eBay' in driver.title

        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="firstname"]'))).send_keys('harly')
        driver.find_element_by_xpath('//*[@id="lastname"]').send_keys('rox')
        driver.find_element_by_xpath('//*[@id="email"]').send_keys('harlyrox3333@gmail.com')
        driver.find_element_by_xpath('//*[@id="PASSWORD"]').send_keys('1385747h')
        driver.find_element_by_xpath('//*[@id="showPASSWORD"]/ul/li/span[2]').click()

    except Exception as e:
        ee.err(wait,driver)
        print('Fail Page' ,format(e))
    

def ebay_sign_in():
   
    url='https://www.ebay.com/signin/'
    driver.get(url)
    
    try:
        wait.until(EC.title_contains("Sign in or Register | eBay"))
        assert 'Sign in or Register | eBay' in driver.title
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="userid"]'))).send_keys('harly')
        driver.find_element_by_xpath('//*[@id="pass"]').send_keys('rox')
        driver.find_element_by_xpath('//*[@id="sgnBt"]').click()

    except Exception as e:
        ee.err(wait,driver)
        print('Fail Page' ,format(e))


def search():
        url='https://www.ebay.com/'
        driver.get(url)

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="gh-ac"]'))).send_keys('toy car')
            driver.find_element_by_xpath('//*[@id="gh-btn"]').click()

        except Exception as e:
            print('Fail Page' ,format(e))
        


    

