from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import speech_recognition as sr
#import selinium_test as gg
import playsound
from gtts import gTTS

# def err(wait,driver):
#     wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="captcha-box"]/div/div[2]/div[1]/div[3]'))).click()
#     element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/div[6]/div[2]/div[1]/div/div[1]/div[2]/div[2]')))
#     action= ActionChains(driver)
#     action.click_and_hold(element)
#     action.move_by_offset(20, 0)
#     action.perform()


def err(wait, driver):
    text = ""
    print("Please say right to move element , say ok to place element.")
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="captcha-box"]/div/div[2]/div[1]/div[3]'))).click()
    element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="body"]/div[6]/div[2]/div[1]/div/div[1]/div[2]/div[2]')))
    action= ActionChains(driver)
    action.click_and_hold(element)
    while text != "exit":

        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))

                if "one" in text:                           
                    action.move_by_offset(10, 0)
                    action.perform()
                if "two" in text:                           
                    action.move_by_offset(20, 0)
                    action.perform()
                if "back" in text:                           
                    action.move_by_offset(-10, 0)
                    action.perform()
                if "ok" in text:
                    action.release(element)
                    action.perform()

            except:
                print("Sorry could not recognize what you said ( ebayerror page )")
