import playsound
from gtts import gTTS
import os 

def speak(text):
        try:
                tts = gTTS(text=text, lang='en-uk')
                filename = "voice.mp3"
                tts.save(filename)
                playsound.playsound(filename)
                os.remove(filename)

        except Exception as identifier:
                print('Please Connect your device to the internet :' ,format(identifier))
