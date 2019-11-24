import speech_recognition as sr
#import selinium_test as gg
i=8
while i>6:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        # gg.facebook()
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
            if text == "exit":
                break
            if text == "good":
                print("Good mother fuckers")
        except:
            print("Sorry could not recognize what you said")
        
