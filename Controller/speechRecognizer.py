import speech_recognition as sr
import speech as sp

def talk():
    r = sr.Recognizer()       
    with sr.Microphone() as source:
        audio = r.listen(source)             
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))               
            return text

        except:
            sp.speak("Sorry could not recognize what you said")