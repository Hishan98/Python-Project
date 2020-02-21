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
                    import Facebook_Gmail as fg
                    fg.facebook()

                if "Google" in text:
                    import Facebook_Gmail as fg
                    fg.google()
                    
                if "eBay" in text:
                    vv.talk()
                    print("Thank You For using Ebay")  

            except:
                print("Sorry could not recognize what you said")
    
talk()