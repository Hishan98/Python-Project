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
    
    #  _____________________________________________sign in Form______________________________________________

def page_load(url):
    try:
        driver.get(url) 
    except Exception as identifier:
        print("Connection Error: "+identifier)

def Help(url):
    try:
        driver.get(url)
        driver.execute_script("window.scrollBy(0,1650)","") 
    except Exception as identifier:
        print("Connection Error: "+identifier)
        
def newtab(url):
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
        # import eBay_Controller as eBay
        # eBay.commands("login")
        

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
        # import eBay_Controller as eBay
        # eBay.commands("login")
        


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
        print("There are "+str(count)+" items in this list")
        
        if setnumber in range (count):
            try:
                sp.speak("Opening " + str(setnumber) + " link") 
                driver.find_element_by_xpath(getitem).click()
            except:
                sp.speak("sorry.you cannot open that link") 
                print ("Unexpected error")
    except Exception as ee:
        print (ee)

# Item selections (select/list)

def drop_down_list(drop_list):
    try:
        sp.speak("Opening style list") 
        driver.find_element_by_xpath(drop_list).click()
    except:
        print("there is no style list under this item")
        sp.speak("sorry.there is no style list under this item") 

def click_sub_list(getlist,gettagname,getitem,Selection):
    try:
        html_list = driver.find_element_by_xpath(getlist)
        items = html_list.find_elements_by_tag_name(gettagname)
        count =len(items)
        print("There are "+ str(count) +" items in this list")
        if Selection in range (count):
            try:
                driver.find_element_by_xpath(getitem).click()

            except Exception as identifier:
                print('Error occoured :' ,format(identifier))
                sp.speak("Cannot click the element") 
        else:
            print("There is no such an item on this list")
            sp.speak("cannot buy that item") 

    except Exception as identifier:
        print('Error occoured :' ,format(identifier))


def quantity(statement,txt_quantity):
    try:
        import common as com
        qty = com.talk(statement)
        
        wait.until(EC.element_to_be_clickable((By.XPATH,txt_quantity))).clear()
        if type(qty)==type(2):
            sp.speak("setting " +str(qty)+ " items") 
            wait.until(EC.element_to_be_clickable((By.XPATH,txt_quantity))).send_keys(qty)
        else:           
            qun = w2n.word_to_num(qty)
            sp.speak("setting " +qty+ " items") 
            wait.until(EC.element_to_be_clickable((By.XPATH,txt_quantity))).send_keys(qun)
    except Exception as e:
        sp.speak("cannot identify the number") 
        print ("Unidentifyied number type",format(e))


def search(url,txt_searchbar):
        try:
            import speechRecognizer as recog
            print('What you want to buy....')
            sp.speak("What you want to buy....") 
            text = recog.talk()
            if not text:
                print('Cannot search Emphty values. Please try Again by saying "search" command')
                sp.speak("Cannot search Emphty value.")
            else:   
                sp.speak("say OK confirm search for" +text) 
                driver.get(url)
                wait.until(EC.element_to_be_clickable((By.XPATH,txt_searchbar))).send_keys(text)    

        except Exception as e:
            print('Fail Page' ,format(e))

            
def okay(btn_search_ok):
    try:
        sp.speak("Searching..") 
        driver.find_element_by_xpath(btn_search_ok).click()
    except Exception as identifier:
        print('Fail Page' ,format(identifier))

# --------------------------------------------------------------------------------------------------------------
# Buying Options

def buy_it_now(btn_buy_it_now):
    try:
        driver.find_element_by_xpath(btn_buy_it_now).click()
        sp.speak("Redirecting to the Payment options") 
    except Exception as identifier:
        print('Unexpected error occored :' ,format(identifier))
        sp.speak("cannot use buy it now command in this page") 

def add_to_cart(btn_add_to_cart):
    try:
        driver.find_element_by_xpath(btn_add_to_cart).click()
        sp.speak("successfully added to cart") 

    except Exception as identifier:
        print('Unexpected error occored :' ,format(identifier))
        sp.speak("cannot use add to cart command in this page") 

def watch_list(btn_watch_list):
    try:
        driver.find_element_by_xpath(btn_watch_list).click()
        sp.speak("Opening the watch list..") 

    except Exception as identifier:
        print('Unexpected error occored :' ,format(identifier))
        sp.speak("cannot use watch list command in this page") 

def feedbacks(btn_feedbacks):
    try:
        driver.find_element_by_xpath(btn_feedbacks).click()
        sp.speak("Opening Feedbacks") 
    except Exception as identifier:
        print('Unexpected error occored :' ,format(identifier))
        sp.speak("cannot use feedback command in this page") 

def confirm_pay(btn_confirm_pay):
    try:        
        driver.find_element_by_xpath(btn_confirm_pay).click()
        sp.speak("your order was placed successfully") 

    except Exception as identifier:
        print('Unexpected error occored :' ,format(identifier))
        sp.speak("cannot use confirm pay command in this page") 

def scroll_down():
    try:
        sp.speak("Scrolling Down..") 
        driver.execute_script("window.scrollBy(0,500)","")

    except Exception as identifier:
        print('Unexpected error occored :' ,format(identifier))
        sp.speak("cannot use confirm pay command in this page") 

def scroll_up():
    try:
        sp.speak("Scrolling Up..") 
        driver.execute_script("window.scrollBy(0,-500)","")

    except Exception as identifier:
        print('Unexpected error occored :' ,format(identifier))
        sp.speak("cannot use confirm pay command in this page") 

def back():
    try:
        sp.speak("Stepping back")
        driver.execute_script("window.history.go(-1)")
        
    except Exception as identifier:
        print('Unexpected error occored :' ,format(identifier))
        sp.speak("cannot use confirm pay command in this page") 

def delete(txt_delete):
    try:
        sp.speak("Deleting search area text..") 
        wait.until(EC.element_to_be_clickable((By.XPATH,txt_delete))).clear()

    except Exception as identifier:
        print('Unexpected error occored :' ,format(identifier))
        sp.speak("cannot use confirm pay command in this page") 

def backspace(txt_backspace):
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,txt_backspace))).send_keys(Keys.BACK_SPACE)
        
    except Exception as identifier:
        print('Unexpected error occored :' ,format(identifier))
        sp.speak("cannot use confirm pay command in this page") 

def unknown_command():
    try:
        sp.speak("You entered an Unknown command...")   
    except Exception as identifier:
        print('Text to speech function not working correctly :' ,format(identifier))    

# _______________________________ali-Express Diffrent controllers________________________________

def ali_sign_up(statement,txt_email,txt_password,btn_show_password):

    try:

        import common as com
        print("enter your "+ statement +" !!!")
        user = com.talk(statement)
        values=user.replace(" ", "")

        if statement=="email":
            driver.find_element_by_xpath(txt_email).send_keys(values)

        elif statement=="password":
            driver.find_element_by_xpath(txt_password).send_keys(values)
            driver.find_element_by_xpath(btn_show_password).click()

    except Exception as e:
        print('Page Loading Failure' ,format(e))

def ali_signup_page(signup_page):
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,signup_page))).click()
    except:
        print('connot open register page')

def ali_signup(btn_signup):
    try:
        driver.find_element_by_xpath(btn_signup).click()
    except Exception as e:
        print('Sign up information error !!! plz retry ....' ,format(e))
        import aliExpress_Controller as ali
        ali.commands("login")
        
def ali_click_list(getlist,getclass,getitem,setnumber,try_getitem):
    try:
        html_list = driver.find_element_by_xpath(getlist)
        items = html_list.find_elements_by_class_name(getclass)
        count =len(items)
        print("There are "+str(count)+" items in this list")
        
        if setnumber in range (count):
            try:
                sp.speak("Opening link" + str(setnumber))
                try: 
                    driver.find_element_by_xpath(getitem).click()
                except:
                    driver.find_element_by_xpath(try_getitem).click()
            except Exception as e:
                sp.speak("sorry.you cannot open that link") 
                print ("Unexpected error :" ,format(e))
    except Exception as ee:
        print (ee)

def ali_click_sub_list(getlist,gettagname,getitem,Selection,trygetlist):
    try:
        # driver.switchTo().defaultContent()
        
        wait.until(EC.element_to_be_clickable((By.XPATH,getitem)))
        driver.find_element_by_xpath(getitem).click()

        # wait.until(EC.element_to_be_clickable((By.XPATH,getitem)))
        # html_list = driver.find_element_by_xpath(getlist)
        # items = html_list.find_elements_by_class_name(gettagname)
        # count =len(items)
        # print("There are "+ str(count) +" items in this list")

        # if Selection in range (count):
        #     try:
        #         driver.find_element_by_xpath(getitem).click()

        #     except Exception as identifier:
        #         print('Error occoured :' ,format(identifier))
        # else:
        #     print("There is no such an item on this list")

    except Exception as identifier:
        print('Error occoured :' ,format(identifier))
        
def close_ads(btn_close):
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,btn_close))).click()
    except:
        print('connot close the ads')
        
# _______________________________Amazon Diffrent controllers________________________________

def enter_otp(statement,txt_OTP):
    try:
        import common as com
        print("enter your "+ statement +" !!!")
        user = com.talk(statement)
        values=user.replace(" ", "")

        driver.find_element_by_xpath(txt_OTP).send_keys(values)

    except Exception as identifier:
        print('Error occoured :' ,format(identifier))

def btn_otp(btn_OTP):
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,btn_OTP))).click()
    except Exception as identifier:
        print('Error occoured :' ,format(identifier))

def resend_otp(btn_resendOTP):
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,btn_resendOTP))).click()
    except Exception as identifier:
        print('Error occoured :' ,format(identifier))

def amazon_sign_in(statement,txt_username,txt_password):  
 
    try:
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


def amazon_sign_up(statement,txt_firstname,txt_email,txt_password,txt_re_password):

    try:
        import common as com
        print("enter your "+ statement +" !!!")
        user = com.talk(statement)
        values=user.replace(" ", "")

        if statement=="firstname":
            wait.until(EC.element_to_be_clickable((By.XPATH,txt_firstname))).send_keys(values)

        elif statement=="email":
            driver.find_element_by_xpath(txt_email).send_keys(values)

        elif statement=="password":
            driver.find_element_by_xpath(txt_password).send_keys(values)
            driver.find_element_by_xpath(txt_re_password).send_keys(values)

    except Exception as e:
        print('Page Loading Failure' ,format(e))

def amazon_signup(btn_signup):
    try:
        driver.find_element_by_xpath(btn_signup).click()
    except Exception as e:
        print('Sign up information error !!! plz retry ....' ,format(e))
        import Amazon_Controller as amazon
        amazon.commands("login")

def amazon_signin_continue(btn_continue):
    try:
        driver.find_element_by_xpath(btn_continue).click()
    except Exception as e:
        print('Sign in Continue button cannot click :' ,format(e))

def amazon_signin_auth(btn_auth):
    try:
        driver.find_element_by_xpath(btn_auth).click()
    except Exception as e:
        print('Sign in auth button cannot click' ,format(e))

def common_button_click(btn_id):
    try:
        driver.find_element_by_xpath(btn_id).click()
    except Exception as e:
        print('Sign in auth button cannot click' ,format(e))

def buyingopt_button_click(btn_id):
    add_to_cart2 ='//*[@id="a-autoid-4"]/span/input'
    try:
        driver.find_element_by_xpath(btn_id).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,add_to_cart2))).click()
    except Exception as e:
        print('Sign in auth button cannot click' ,format(e))

def add_a_card(statement,card_name,card_number):
    try:
        import common as com
        print("enter your "+ statement +" !!!")
        user = com.talk(statement)
        values=user.replace(" ", "")

        if statement=="card name":
            wait.until(EC.element_to_be_clickable((By.XPATH,card_name))).send_keys(values)

        elif statement=="card number":
            driver.find_element_by_xpath(card_number).send_keys(values)

    except Exception as e:
        print('Sign in auth button cannot click' ,format(e))

def enter_only_pw(statement,txt_only_password):
    try:
        btn_signin='//*[@id="signInSubmit"]'

        import common as com
        print("enter your "+ statement +" !!!")
        user = com.talk(statement)
        values=user.replace(" ", "")

        wait.until(EC.element_to_be_clickable((By.XPATH,txt_only_password))).send_keys(values)
        wait.until(EC.element_to_be_clickable((By.XPATH,btn_signin))).click()
    except Exception as e:
        print('Sign in auth button cannot click' ,format(e))

def amazon_click_list(getlist,getclass,getitem,setnumber):
    try:
        html_list = driver.find_element_by_xpath(getlist)
        items = html_list.find_elements_by_class_name(getclass)
        count =len(items)
        print("There are "+str(count)+" items in this list")
        
        if setnumber in range (count):
            try:
                sp.speak("Opening " + str(setnumber) + " link") 
                driver.find_element_by_xpath(getitem).click()
            except:
                sp.speak("sorry.you cannot open that link") 
                print ("Unexpected error")
    except Exception as ee:
        print (ee)