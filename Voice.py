import speech_recognition as sr
#import selinium_test as gg
import playsound
from gtts import gTTS


# def speak(text):
#         tts = gTTS(text=text, lang='en')
#         filename = "voice.mp3"
#         tts.save(filename)
#         playsound.playsound(filename)
# speak("Hi Guys")

condition = ""
def talk(condition):
    text=""   
    while text!="exit":
        print(condition)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)      
            try:  
                text = r.recognize_google(audio)
                print("You said : {}".format(text))

                if condition=="eBay":
                    import ebay as ebay
                    ebay.commands(text)

                if condition=="Facebook":
                    print("condition")
                    import Facebook_Gmail as fg
                    fg.facebook()
                    
                if condition=="Google":
                    import Facebook_Gmail as fg
                    fg.google(text)                   
            except:
                print("Sorry could not recognize what you said")
    