from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# browser = webdriver.Chrome(executable_path=os.path.abspath(os.getcwd()) + "/chromedriver")
driver = webdriver.Chrome('C:\Windows\chromedriver.exe', options=chrome_options)

link = 'https://www.ebay.com/'
driver.get(link)

# search keys
search = driver.find_element_by_xpath('//*[@id="gh-ac"]')
search.send_keys("car")
search.send_keys(Keys.RETURN)

# click second link
try:
    html_list = driver.find_element_by_xpath('//*[@id="srp-river-results"]/ul')
    items = html_list.find_elements_by_class_name('s-item   ')
    count =len(items)
    print(count)
    i=2
    if i in range (count):
        try:
            driver.find_element_by_xpath('//*[@id="srp-river-results-listing'+str(i)+'"]/div/div[2]/a').click()
            # print('//*[@id="srp-river-results-listing'+str(i)+'"]/div/div[2]/a/h3')
        except:
            print ("Unexpected error:", sys.exc_info()[0])
except:
    print ("Unexpected error:", sys.exc_info()[0])