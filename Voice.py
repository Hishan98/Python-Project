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


def talk():
    text=""
    print("Please select what you want to do in here..")
    while text!="exit":

        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)      
            try:  
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                import ebay as ebay
                ebay.commands(text) 
            except:
                print("Sorry could not recognize what you said")
    