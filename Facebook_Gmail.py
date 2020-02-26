import speech_recognition as sr

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

global driver
driver = webdriver.Chrome('C:\Windows\chromedriver.exe', options=chrome_options)
chrome_options.add_argument("--start-maximized")
wait = WebDriverWait(driver, 10)

def google(text): 
    if "scroll down" in text: 
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tsf"]/div[2]/div[1]/div[2]/button')))
        driver.execute_script("window.scrollBy(0,500)","")

    elif "back" in text: 
        driver.execute_script("window.history.go(-1)")

    elif "scroll up" in text: 
        wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tsf"]/div[2]/div[1]/div[2]/button')))
        driver.execute_script("window.scrollBy(0,-500)","")

    elif "first link" in text:
        for i in range(10):
            try:
                driver.find_element_by_xpath('//*[@id="rso"]/div['+str(i)+']/div/div/div/div/div[1]/a').click()           
                break
            except:
                pass
    elif "second link" in text:
        for i in range(10):
            try:
                driver.find_element_by_xpath('//*[@id="rso"]/div['+str(i)+']/div/div[2]/div/div/div[1]/a').click()
                break
            except:
                pass
    elif "third link" in text:
        for i in range(10):
            try:
                driver.find_element_by_xpath('//*[@id="rso"]/div['+str(i)+']/div/div[3]/div/div/div[1]/a').click()          
                break
            except:
                pass
    elif "fourth link" in text:
        for i in range(10):
            try:
                driver.find_element_by_xpath('//*[@id="rso"]/div['+str(i)+']/div/div[4]/div/div/div[1]/a').click()           
                break
            except:
                pass
    elif "V link" in text:
        for i in range(10):
            try:
                driver.find_element_by_xpath('//*[@id="rso"]/div['+str(i)+']/div/div[5]/div/div/div[1]/a').click()           
                break
            except:
                pass
    else:
        ggwp=text.replace(" ", "")
        driver.get("https://www.google.com")
        driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys(ggwp)
        driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)

def facebook():
    driver.get("https://www.facebook.com/")
    driver.find_element_by_xpath('//*[@id="email"]').send_keys('harlyrox3333@gmail.com')
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys('40322386h')
    driver.find_element_by_xpath('//*[@id="u_0_b"]').click()


def actions():
        text=""   
        while text!="exit":
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)      
                try:  
                    text = r.recognize_google(audio)
                    print("You said : {}".format(text))

                    if text=="eBay":
                        import ebay as ebay
                        ebay.commands(text) 
                    if text=="Facebook":
                        import Facebook_Gmail as fg
                        fg.facebook()
                    if text=="Google":
                        import Facebook_Gmail as fg
                        #fg.google()                   
                except:
                    print("Sorry could not recognize what you said")
