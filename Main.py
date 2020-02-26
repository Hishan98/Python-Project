import speech_recognition as sr
import playsound
import Voice as vv
from gtts import gTTS

# def speak(text):
#         tts = gTTS(text=text, lang='en')
#         filename = "voice.mp3"
#         tts.save(filename)
#         playsound.playsound(filename)
# speak("Hi Guys")


def talk():
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
                    print("Please select what you want to do in here..")
                    vv.talk(condition)
                    print("Thank You For using Ebay")  

            except:
                print("Sorry could not recognize what you said")
    
talk()