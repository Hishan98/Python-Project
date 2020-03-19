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
        url='https://www.ebay.com/signin/'
        driver.get(url) 

        ebay_sign_in("email")
        ebay_sign_in("password")
        signin()
    elif "sign up" in text: 
        url='https://reg.ebay.com/reg/PartialReg'
        driver.get(url)

        ebay_sign_up("firstname")
        ebay_sign_up("lastname")
        ebay_sign_up("email")
        ebay_sign_up("password")
        signup()
    elif text=="exit": 
        driver.close()
    elif text=="back":
        back()
    elif "scroll up" in text:
        scroll_up()  
    elif "scroll down" in text:
        scroll_down()
    elif "delete" in text:
        delete()
    elif "backspace" in text:
        backspace()
    elif text=="ok":
        okay()
    # select an item form the search results

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

    # Item selections (Colors/Sizes & etc.)

    elif "select" in text:
        select()
    elif "first item" in text:
        click_sub_list(0)
    elif "second item" in text:
        click_sub_list(1)
    elif "third item" in text:
        click_sub_list(2)
    elif "fourth item" in text:
        click_sub_list(3)
    elif "V item" in text:
        click_sub_list(4)
    elif "set" in text:
        import common as com
        com.talk("quentity")

    # Buying Options

    elif "add to cart" in text:
        add_to_cart()
    elif "watch list" in text:
        watch_list()
    elif "feedback" in text:
        feedbacks()
    elif "buy it now" in text:
        buy_it_now()
    elif "pay" in text:
        confirm_pay()

    #Selling Options
    elif "sell" in text:
        import ebay_sell as eb
        eb.sell(wait,driver)

    else:
        search(text)

    
    #  _____________________________________________sign in Form______________________________________________


def ebay_sign_in(statement):  
 
    try:
        wait.until(EC.title_contains("Sign in or Register | eBay"))
        assert 'Sign in or Register | eBay' in driver.title
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="userid"]')))

        import common as com
        print("enter your "+ statement +" !!!")
        user = com.talk(statement)
        values=user.replace(" ", "")

        if statement=="email":
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="userid"]'))).send_keys(values)
        else:
            driver.find_element_by_xpath('//*[@id="pass"]').send_keys(values)

    except Exception as e:
        print('Page Loading Failure:  ' ,format(e))
        ee.check_error(wait,driver)

def signin():
    try:
        driver.find_element_by_xpath('//*[@id="sgnBt"]').click()
    except Exception as e:
        print('Sign in information error !!! plz Try Again....' ,format(e))
        commands("login")
        

    #   _____________________________________________END______________________________________________  
    #---------------------------------------------------------------------------------------------------    



    #  _____________________________________________Sign Up Form______________________________________________


def ebay_sign_up(statement):

    try:
        wait.until(EC.title_contains("Sign in or Register | eBay"))
        assert 'Sign in or Register | eBay' in driver.title

        import common as com
        print("enter your "+ statement +" !!!")
        user = com.talk(statement)
        values=user.replace(" ", "")

        if statement=="firstname":
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="firstname"]'))).send_keys(values)

        elif statement=="lastname":
            driver.find_element_by_xpath('//*[@id="lastname"]').send_keys(values)

        elif statement=="email":
            driver.find_element_by_xpath('//*[@id="email"]').send_keys(values)

        elif statement=="password":
            driver.find_element_by_xpath('//*[@id="PASSWORD"]').send_keys(values)
            driver.find_element_by_xpath('//*[@id="showPASSWORD"]/ul/li/span[2]').click()

    except Exception as e:
        print('Page Loading Failure' ,format(e))
        ee.check_error(wait,driver)
        
def signup():
    try:
        driver.find_element_by_xpath('//*[@id="ppaFormSbtBtn"]').click()
    except Exception as e:
        print('Sign up information error !!! plz retry ....' ,format(e))
        commands("sign up")
        


    #   _____________________________________________END______________________________________________  
    #---------------------------------------------------------------------------------------------------  


def search(text):
        url='https://www.ebay.com/'
        driver.get(url)

        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="gh-ac"]'))).send_keys(text)            
        except Exception as e:
            print('Fail Page' ,format(e))
def okay():
    try:
        driver.find_element_by_xpath('//*[@id="gh-btn"]').click()
    except Exception as identifier:
        print('Fail Page' ,format(identifier))

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
        print ("Unexpected error occored")

def delete():
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="gh-ac"]'))).clear()
def backspace():
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="gh-ac"]'))).send_keys(Keys.BACK_SPACE)
# Item selections (select/list)

def select():
    try:
        driver.find_element_by_xpath('//*[@id="msku-sel-1"]').click()
    except:
        print("there is no selection list in this item")

def click_sub_list(Selection):
    try:
        html_list = driver.find_element_by_xpath('//*[@id="msku-sel-1"]')
        items = html_list.find_elements_by_tag_name('option')
        count =len(items)
        print(count)
        if Selection in range (count):
            try:
                driver.find_element_by_xpath('//*[@id="msku-opt-'+str(Selection)+'"]').click()
            except:
                print ("Unexpected error")
        else:
            print("There is no "+str(Selection)+" item on list")
    except:
        print ("Unexpected error occored")

def quantity(qty):
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="qtyTextBox"]'))).clear()
        if type(qty)==type(2):
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="qtyTextBox"]'))).send_keys(qty)
        else:           
            qun = w2n.word_to_num(qty)
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="qtyTextBox"]'))).send_keys(qun)
    except:
        print ("Unidentifyied number type")

# --------------------------------------------------------------------------------------------------------------
# Buying Options

def buy_it_now():
    try:
        driver.find_element_by_xpath('//*[@id="binBtn_btn"]').click()
    except:
        print ("Unexpected error occored")

def add_to_cart():
    try:
        driver.find_element_by_xpath('//*[@id="isCartBtn_btn"]').click()
    except:
        print ("Unexpected error occored")

def watch_list():
    try:
        driver.find_element_by_xpath('//*[@id="vi-atl-lnk"]/a/span[2]').click()
    except:
        print ("Unexpected error occored")

def feedbacks():
    try:
        driver.find_element_by_xpath('//*[@id="byrfdbk_atf_lnk_sm"]').click()
    except:
        print ("Unexpected error occored")

def confirm_pay():
    try:
        driver.find_element_by_xpath('//*[@id="page-form"]/div/button').click()
    except:
        print ("Unexpected error occored")


