from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import speech_recognition as sr
import playsound
from gtts import gTTS

def check_error(wait,driver):
    currentUrl=driver.current_url
    checkUrl="https://www.ebay.com/distil_identify_cookie.html"
    try:
        if checkUrl in currentUrl:
            # url='https://www.ebay.com/signin/'
            # driver.get(url)

            # wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="userid"]')))
            import Engine as eng
            eng.commands("login")
        else:
            err(wait,driver)
            # driver.delete_all_cookies()
            # driver.get("chrome://settings/clearBrowserData")
            # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="clearBrowsingDataConfirm"]'))).click()
            # import Engine as engay
            # ebay.commands("login")
    except:
        print("Redirecting...")

def err(wait, driver):
    
    text = ""
    print("Please say right to move element , say ok to place element.")
    wait.until(EC.element_to_be_clickable(
         (By.XPATH, '//*[@id="captcha-box"]/div/div[2]/div[1]/div[3]'))).click()
    element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="body"]/div[6]/div[2]/div[1]/div/div[1]/div[2]/div[2]')))
    location=10
    while text != "exit":

        action = ActionChains(driver)
        action.click_and_hold(element)

        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))

                if "one" in text:
                    action.move_by_offset(location, 0)
                    action.perform()
                    location=location+10

                elif "two" in text:
                    location=location+10
                    action.move_by_offset(location, 0)
                    action.perform()
                    location=location+20

                elif "tree" in text:
                    location=location+20
                    action.move_by_offset(location, 0)
                    action.perform()
                    location=location+30

                elif "four" in text:
                    location=location+30
                    action.move_by_offset(location, 0)
                    action.perform()
                    location=location+40

                elif "5" in text:
                    location=location+40
                    action.move_by_offset(location, 0)
                    action.perform()
                    # location=location+50

                elif "back" in text:
                    location=location-10
                    action.move_by_offset(location, 0)
                    action.perform()
                    
                elif "ok" in text:
                    action.move_by_offset(location, 0)
                    action.release(element)
                    action.perform()
                    break
                elif "retry" in text:
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="captcha-box"]/div/div[2]/div[1]/div[3]/span[2]'))).click()
                    err(wait, driver)
                elif "exit" in text:
                    import ebay.search as ee
                    ee()
                else:
                    print("Not a valid command (Error)")

            except:
                print("Sorry could not recognize what you said ( error page )")
        action.reset_actions()
