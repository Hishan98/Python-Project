import playsound
from gtts import gTTS
import os 

def speak(text):
        tts = gTTS(text=text, lang='en-uk')
        filename = "voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
