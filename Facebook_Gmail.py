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


def google():
    driver.get("https://www.google.com")
    driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys('w3school')
    driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)

def facebook():
    driver.get("https://www.facebook.com/")
    driver.find_element_by_xpath('//*[@id="email"]').send_keys('harlyrox3333@gmail.com')
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys('40322386h')
    driver.find_element_by_xpath('//*[@id="u_0_b"]').click()
