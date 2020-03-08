import speech_recognition as sr
import playsound
from gtts import gTTS


condition = ""
def talk(condition):
    text=""   
    while text!="exit":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)      
            try:  
                text = r.recognize_google(audio)
                print("You said : {}".format(text))

                if condition=="eBay":
                    import ebay as ebay
                    ebay.commands(text)

                elif condition=="Facebook":
                    print("condition")
                    import Facebook_Gmail as fg
                    fg.facebook()
                    
                elif condition=="Google":
                    import Facebook_Gmail as fg
                    fg.google(text)
               
            except:
                print("Sorry could not recognize what you said")
    