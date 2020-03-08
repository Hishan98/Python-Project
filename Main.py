import speech_recognition as sr
import playsound
import Voice as vv
import speech as sp



def talk():
    text=""   
    while text!="exit":

        r = sr.Recognizer()
        sp.speak("Please select your web site") 
        with sr.Microphone() as source:
            audio = r.listen(source)             
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))               
                #____Main Controllers___#  

                if "Facebook" in text:
                    condition = "Facebook"
                    print("Share/Like/Comment")
                    vv.talk(condition)
                    print("Thank You For using Facebook") 

                elif "Google" in text:
                    condition = "Google"
                    print("Search your content")
                    vv.talk(condition)
                    print("Thank You For using Google") 
                    
                elif "eBay" in text:
                    condition = "eBay"
                    sp.speak("eBay it is")  
                    print("Please select what you want to do in here..")
                    vv.talk(condition)
                    print("Thank You For using Ebay")  

            except:
                sp.speak("Sorry could not recognize what you said")
    
talk()