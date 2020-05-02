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
    
    #  _____________________________________________sign in Form______________________________________________

def page_load(url):
    try:
        driver.get(url) 
    except Exception as identifier:
        print("Connection Error: "+identifier)

def ebay_sign_in(statement,txt_username,txt_password):  
 
    try:
        # wait.until(EC.title_contains("Sign in or Register | eBay"))
        # assert 'Sign in or Register | eBay' in driver.title
        wait.until(EC.element_to_be_clickable((By.XPATH,txt_username)))

        import common as com
        user = com.talk(statement)
        values=user.replace(" ", "")

        if statement=="email":
            wait.until(EC.element_to_be_clickable((By.XPATH,txt_username))).send_keys(values)
        else:
            driver.find_element_by_xpath(txt_password).send_keys(values)

    except Exception as e:
        print('Page Loading Failure:  ' ,format(e))
        ee.check_error(wait,driver)

def signin(btn_signin):
    try:
        driver.find_element_by_xpath(btn_signin).click()
        # updateinfo()

    except Exception as e:
        print('Sign in information error !!! plz Try Again....' ,format(e))
        import eBay_Controller as eBay
        eBay.commands("login")
        

    #   _____________________________________________END______________________________________________  
    #---------------------------------------------------------------------------------------------------    



    #  _____________________________________________Sign Up Form______________________________________________


def ebay_sign_up(statement,txt_firstname,txt_lastname,txt_email,txt_password,btn_show_password):

    try:
        wait.until(EC.title_contains("Sign in or Register | eBay"))
        assert 'Sign in or Register | eBay' in driver.title

        import common as com
        print("enter your "+ statement +" !!!")
        user = com.talk(statement)
        values=user.replace(" ", "")

        if statement=="firstname":
            wait.until(EC.element_to_be_clickable((By.XPATH,txt_firstname))).send_keys(values)

        elif statement=="lastname":
            driver.find_element_by_xpath(txt_lastname).send_keys(values)

        elif statement=="email":
            driver.find_element_by_xpath(txt_email).send_keys(values)

        elif statement=="password":
            driver.find_element_by_xpath(txt_password).send_keys(values)
            driver.find_element_by_xpath(btn_show_password).click()

    except Exception as e:
        print('Page Loading Failure' ,format(e))
        ee.check_error(wait,driver)
        
def signup(btn_signup):
    try:
        driver.find_element_by_xpath(btn_signup).click()
    except Exception as e:
        print('Sign up information error !!! plz retry ....' ,format(e))
        import eBay_Controller as eBay
        eBay.commands("login")
        


    #   _____________________________________________END______________________________________________  
    #---------------------------------------------------------------------------------------------------  


def updateinfo():
    try:
        currentUrl=driver.current_url
        checkUrl="https://reg.ebay.com/reg/UpdateContactInfo"
        if checkUrl in currentUrl:
            import common as com
            email=com.talk("email")
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="email"]'))).send_keys(email)
            phone=com.talk("phone")           
            wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="phoneFlagComp1"]'))).send_keys(phone)
            driver.find_element_by_xpath('//*[@id="sbtBtn"]').click()

    except Exception as identifier:
        print("Update infomation error :" + identifier)


def click_list(getlist,getclass,getitem,setnumber):
    try:
        html_list = driver.find_element_by_xpath(getlist)
        items = html_list.find_elements_by_class_name(getclass)
        count =len(items)
        print(count)
        
        if setnumber in range (count):
            try:
                driver.find_element_by_xpath(getitem).click()
            except:
                print ("Unexpected error")
    except Exception as ee:
        print (ee)

# Item selections (select/list)

def drop_down_list(drop_list):
    try:
        driver.find_element_by_xpath(drop_list).click()
    except:
        print("there is no style list in this item")

def click_sub_list(getlist,gettagname,getitem,Selection):
    try:
        html_list = driver.find_element_by_xpath(getlist)
        items = html_list.find_elements_by_tag_name(gettagname)
        count =len(items)
        print(count)
        if Selection in range (count):
            try:
                driver.find_element_by_xpath(getitem).click()
            except:
                print ("Unexpected error")
        else:
            print("There is no such an item on this list")
    except:
        print ("Unexpected error occored")


def quantity(statement,txt_quantity):
    try:
        import common as com
        qty = com.talk(statement)
        
        wait.until(EC.element_to_be_clickable((By.XPATH,txt_quantity))).clear()
        if type(qty)==type(2):
            wait.until(EC.element_to_be_clickable((By.XPATH,txt_quantity))).send_keys(qty)
        else:           
            qun = w2n.word_to_num(qty)
            wait.until(EC.element_to_be_clickable((By.XPATH,txt_quantity))).send_keys(qun)
    except Exception as e:
        print ("Unidentifyied number type",format(e))


def search(url,txt_searchbar):
        try:
            import speechRecognizer as recog
            print('What you want to buy....')
            text = recog.talk()
            driver.get(url)
            wait.until(EC.element_to_be_clickable((By.XPATH,txt_searchbar))).send_keys(text)    

        except Exception as e:
            print('Fail Page' ,format(e))

            
def okay(btn_search_ok):
    try:
        driver.find_element_by_xpath(btn_search_ok).click()
    except Exception as identifier:
        print('Fail Page' ,format(identifier))

# --------------------------------------------------------------------------------------------------------------
# Buying Options

def buy_it_now(btn_buy_it_now):
    try:
        driver.find_element_by_xpath(btn_buy_it_now).click()
    except:
        print ("Unexpected error occored")

def add_to_cart(btn_add_to_cart):
    try:
        driver.find_element_by_xpath(btn_add_to_cart).click()
    except:
        print ("Unexpected error occored")

def watch_list(btn_watch_list):
    try:
        driver.find_element_by_xpath(btn_watch_list).click()
    except:
        print ("Unexpected error occored")

def feedbacks(btn_feedbacks):
    try:
        driver.find_element_by_xpath(btn_feedbacks).click()
    except:
        print ("Unexpected error occored")

def confirm_pay(btn_confirm_pay):
    try:
        driver.find_element_by_xpath(btn_confirm_pay).click()
    except:
        print ("Unexpected error occored")

def scroll_down():

    driver.execute_script("window.scrollBy(0,500)","")

def scroll_up():

    driver.execute_script("window.scrollBy(0,-500)","")

def back():

    driver.execute_script("window.history.go(-1)")

def delete(txt_delete):
    wait.until(EC.element_to_be_clickable((By.XPATH,txt_delete))).clear()

def backspace(txt_backspace):
    wait.until(EC.element_to_be_clickable((By.XPATH,txt_backspace))).send_keys(Keys.BACK_SPACE)
