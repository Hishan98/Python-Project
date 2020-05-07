import playsound
import speech as sp
import speechRecognizer as recog

def site_selection():
    sp.speak("Welcome to the talk & shop Application...")
    sp.speak("If you are a new user please refer our user manual by simply saying help")   
    text=""
    while text!="exit":
        sp.speak("Please select your web site")
        try: 
            text=recog.talk()
            if "Google" in text:
                condition = "Google"
                print("Search your content")
                in_site_selection(condition)
                print("Thank You For using Google") 
                            
            elif "eBay" in text:
                condition = "eBay"
                sp.speak("You have selected eBay..")
                in_site_selection(condition)
                sp.speak("Thank You For using eBay")

            elif "aliexpress" in text:
                condition = "aliexpress"
                sp.speak("You have selected aliexpress..")
                in_site_selection(condition)
                sp.speak("Thank You For using aliexpress")

            elif "Amazon" in text:
                condition = "Amazon"
                sp.speak("You have selected Amazon..")
                in_site_selection(condition)
                sp.speak("Thank You For using Amazon")    

            elif "help" in text:
                import Engine as eng
                url='https://github.com/Hishan98/Python-Project/tree/master'
                eng.Help(url)
        except:
            print("Unknown Command (site_selection)") 

        import Engine as eng
        eng.driver.close()   

def in_site_selection(condition):
    text=""
    sp.speak("Please select what you want to do in here") 
    while text!="exit":    
        try:
            text=recog.talk()
            if condition=="eBay":
                import eBay_Controller as ebay
                ebay.commands(text)

            elif condition=="aliexpress":
                import aliExpress_Controller as aliexp
                aliexp.commands(text)
                
            elif condition=="Amazon":
                import Amazon_Controller as amazon
                amazon.commands(text)
                            
            elif condition=="Google":
                import GoogleBrows as gg
                gg.google(text)
        except:
            print("Unknown Command (in_site_selection)")   

site_selection()