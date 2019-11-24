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
def ebay_sign_up():

    driver.get("https://reg.ebay.com/reg/PartialReg")
    # driver.find_element_by_xpath('//*[@id="gh-eb-My"]/div/a[1]').click()
    # driver.find_element_by_xpath('//*[@id="InLineCreateAnAccount"]').click()

    driver.find_element_by_xpath('//*[@id="firstname"]').send_keys('harly')
    driver.find_element_by_xpath('//*[@id="lastname"]').send_keys('rox')
    driver.find_element_by_xpath('//*[@id="email"]').send_keys('harlyrox3333@gmail.com')
    driver.find_element_by_xpath('//*[@id="PASSWORD"]').send_keys('1385747h')

    # driver.find_element_by_xpath('//*[@id="showPASSWORD"]/ul/li/span[2]').click()
def test():
    url='https://reg.ebay.com/reg/PartialReg?siteid=0&co_partnerId=0&UsingSSL=1&rv4=1&pageType=3984&ru=https%3A%2F%2Fmy.ebay.com%2Fws%2FeBayISAPI.dll%3FMyEbayBeta%26MyEbay%3D%26gbh%3D1%26guest%3D1&signInUrl=https%3A%2F%2Fwww.ebay.com%2Fsignin%3Fsgn%3Dreg%26siteid%3D0%26co_partnerId%3D0%26UsingSSL%3D1%26rv4%3D1%26pageType%3D3984%26ru%3Dhttps%253A%252F%252Fmy.ebay.com%252Fws%252FeBayISAPI.dll%253FMyEbayBeta%2526MyEbay%253D%2526gbh%253D1%2526guest%253D1'
    driver.get(url)
    wait=WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="firstname"]'))).send_keys('harly')
    driver.find_element_by_xpath('//*[@id="lastname"]').send_keys('rox')
    driver.find_element_by_xpath('//*[@id="email"]').send_keys('harlyrox3333@gmail.com')
    driver.find_element_by_xpath('//*[@id="PASSWORD"]').send_keys('1385747h')

test()
    

