from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

try:
        # Connect
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        global browser # this will prevent the browser variable from being garbage collected
        browser = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
        browser.set_window_size(1800, 900)
        browser.get("https://www.instagram.com/accounts/login/?hl=de")
        browser.find_element(By.NAME, 'username').send_keys('MYEMAIL', Keys.TAB, 'MYPW', Keys.ENTER)
except Exception as e:
        print (e, 'Instagram')

open_instagram()