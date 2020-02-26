from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Voice as vv
import ebay_error as ee
import sys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

global driver

driver = webdriver.Chrome('C:\Windows\chromedriver.exe', options=chrome_options)
wait = WebDriverWait(driver, 10)
text=""
def commands(text):
    
    if "login" in text: 
        ebay_sign_in()
    elif "sign up" in text:  
        ebay_sign_up()
    elif "exit" in text: 
        url='chrome//newtab'
        driver.get(url)
    elif "back" in text:
        back()
    elif "scroll up" in text:
        scroll_up()  
    elif "scroll down" in text:
        scroll_down()
    elif "first link" in text: 
        click_list(1)
    elif "second link" in text: 
        click_list(2)
    elif "third link" in text:
        click_list(3) 
    elif "fourth link" in text:
        click_list(4) 
    elif "V link" in text: 
        click_list(5)    
    else:
        search(text)

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


def search(text):
        url='https://www.ebay.com/'
        driver.get(url)

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="gh-ac"]'))).send_keys(text)
            driver.find_element_by_xpath('//*[@id="gh-btn"]').click()

        except Exception as e:
            print('Fail Page' ,format(e))

def scroll_down():

    driver.execute_script("window.scrollBy(0,500)","")

def scroll_up():

    driver.execute_script("window.scrollBy(0,-500)","")

def back():

    driver.execute_script("window.history.go(-1)")

def click_list(Number):
    try:
        html_list = driver.find_element_by_xpath('//*[@id="srp-river-results"]/ul')
        items = html_list.find_elements_by_class_name('s-item   ')
        count =len(items)
        print(count)
        if Number in range (count):
            try:
                driver.find_element_by_xpath('//*[@id="srp-river-results-listing'+str(Number)+'"]/div/div[2]/a').click()
            except:
                print ("Unexpected error")
    except:
        print ("Unexpected error:", sys.exc_info()[0])

    

