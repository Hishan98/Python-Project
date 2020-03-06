from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys
import speech_recognition as sr
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# browser = webdriver.Chrome(executable_path=os.path.abspath(os.getcwd()) + "/chromedriver")
driver = webdriver.Chrome('C:\Windows\chromedriver.exe', options=chrome_options)

link = 'https://www.ebay.com/itm/World-Map-Natural-Rubber-Extended-Gaming-Mouse-Pad-Desk-Keyboard-Mat-S-XL-NEW/312923051870?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D20160908105057%26meid%3D4f220f0b186d444d8fa46e6828defa44%26pid%3D100675%26rk%3D4%26rkt%3D15%26mehot%3Dnone%26sd%3D312883598409%26itm%3D312923051870%26pmt%3D0%26noa%3D1%26pg%3D2380057&_trksid=p2380057.c100675.m4236&_trkparms=pageci%3Af166b8b5-58b4-11ea-928c-74dbd1804818%7Cparentrq%3A825380fb1700aad6ed4019edfff56b30%7Ciid%3A1'
driver.get(link)

# search keys
text=""
    # print("Please select your website")
while text!="exit":

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source) 
        print("Please select your website")     
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))

            while text!="ok":
                try:
                    text = r.recognize_google(audio)
                    print("You said : {}".format(text))
                    print("what model you want")
                    driver.find_element_by_xpath('//*[@id="msku-opt-2"]').click()

                    while text!="ok":
                        try:
                            text = r.recognize_google(audio)
                            print("You said : {}".format(text))
                            print("How many items do you want?")
                            eb.quantity(int(text))
                            print("You said : {}".format(text))
                        except:
                            print("Sorry could not recognize what you said (Count)")                       
                except:
                    print("Sorry could not recognize what you said (Model)")
        except:
            print("Sorry could not recognize what you said")       



# click second link
# try:
#     html_list = driver.find_element_by_xpath('//*[@id="srp-river-results"]/ul')
#     items = html_list.find_elements_by_class_name('s-item   ')
#     count =len(items)
#     print(count)
#     i=2
#     if i in range (count):
#         try:
#             driver.find_element_by_xpath('//*[@id="srp-river-results-listing'+str(i)+'"]/div/div[2]/a').click()
#             # print('//*[@id="srp-river-results-listing'+str(i)+'"]/div/div[2]/a/h3')
#         except:
#             print ("Unexpected error:", sys.exc_info()[0])
# except:
#     print ("Unexpected error:", sys.exc_info()[0])