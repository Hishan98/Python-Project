from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from word2number import w2n

import ebay_error as ee

    #  ______________________________________Detect user type (New / usual)________________________________________

def sell(wait,driver):
    url='https://my.ebay.com/ws/eBayISAPI.dll?MyEbay&gbh=1&CurrentPage=MyeBayAllSelling&ssPageName=STRK:ME:LNLK:MESX'
    driver.get(url)

    currentUrl=driver.current_url
    checkUrl="https://reg.ebay.com/reg/Upgrade"
    checkUrl1="https://signin.ebay.com/"
    try:
        if checkUrl in currentUrl:
            sell_begining_address(wait,driver,"address")
            sell_begining_address(wait,driver,"city")
            sell_begining_address(wait,driver,"state")
            sell_begining_address(wait,driver,"zip")
            sell_begining_address(wait,driver,"phone")
            sell_begining_address_submit(driver)
            
        elif checkUrl1 in currentUrl:
            import Engine as eng
            eng.ebay_sign_in("email")
            eng.ebay_sign_in("password")
            eng.signin()
            
        else:
            print("say list an item to list a item")
            sell_commands(wait,driver)          

    except Exception as identifier:
        print("failur !!!!!!!!!!" + identifier)

    #  _____________________________________________Selling Controller______________________________________________

text=""
def sell_commands(wait,driver):
    text=""
    while text!="exit":
        import speechRecognizer as recog 
        text = recog.talk()

        if text=="list an item":
            list_an_item(wait,driver)
        else:
            pass


    #  _____________________________________________Newbie billing______________________________________________


def sell_begining_address(wait,driver,statement):
    try:
        wait.until(EC.title_contains("Sign in or Register | eBay"))
        assert 'Sign in or Register | eBay' in driver.title

        import common as com
        print("enter your "+ statement +" !!!")
        user = com.talk(statement)
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
        print("Cannot click sell_begining_address_submit button : " ,format(e))


    #  _____________________________________________Usual billing______________________________________________

def list_an_item(wait,driver):
    try:
        driver.find_element_by_xpath('//*[@id="meb-items-cnt"]/section[2]/div/span[3]/a').click()
        find_similar_search(wait,driver)
    except Exception as identifier:
        print("list an item Error :" + identifier)

def find_similar_search(wait,driver):
    try:
        currentUrl=driver.current_url
        checkUrl="https://bulksell.ebay.com/ws"
        if checkUrl in currentUrl:
            text=""
            while text!="ok":
                import speechRecognizer as recog
                print("say similar product name and say ok to search it !!!") 
                text = recog.talk()
                if text!="ok":
                    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="w0-find-product-search-bar-search-field"]'))).send_keys(text)
                else:
                    break       
            driver.find_element_by_xpath('//*[@id="w0-find-product-search-bar-search-button"]').click()
        else:
            print("You are in a wrong site")
    except Exception as identifier:
        print("Search similar item Error :" + identifier)

    #   _____________________________________________END______________________________________________  
    #---------------------------------------------------------------------------------------------------  