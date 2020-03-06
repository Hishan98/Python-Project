import speech_recognition as sr

def talk(statement,condition):
    text=""
    #print("Please select your website")
    while text!=statement:

        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)                 
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                if condition=="quentity": 
                    print("How many items do you want?") 
                    import ebay as eb
                    eb.quantity(text)
                    break
                elif condition=="username":
                    print("enter your E-mail")
                    return text
                    
                elif condition=="password":
                    print("Enter your Password")
                    return text
                    break
                else:
                    print("Hi")
            except:
                print("Sorry could not recognize what you said")
