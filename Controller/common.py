import speech as sp

def talk(condition):
    statement="ok"
    text=""
    count=0
    while text != statement:
        try:           
            if condition == "quentity":
                if(count==0):
                    print("How many items do you want?")
                    sp.speak("How many items do you want?")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text
                else:
                    print("Say ok for confirm quantity or say the count again")
                    sp.speak("Say ok for confirm quantity or say the count again")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text

            elif condition == "email":
                if(count==0):
                    print("enter your E-mail")
                    sp.speak("enter your E-mail")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text
                else:
                    print("Say ok for confirm quantity or say your email again")
                    sp.speak("Say ok for confirm quantity or say your email again")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text


            elif condition == "password":
                if(count==0):
                    print("Enter your Password")
                    sp.speak("Enter your Password")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text
                else:
                    print("Say ok for confirm quantity or say your Password again")
                    sp.speak("Say ok for confirm quantity or say your Password again")

            elif condition == "firstname":

                if(count==0):
                    print("Enter your firstname")
                    sp.speak("Enter your firstname")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text
                else:
                    print("Say ok for confirm quantity or say your firstname again")
                    sp.speak("Say ok for confirm quantity or say your firstname again")

            elif condition == "lastname":
                
                if(count==0):
                    print("Enter your lastname")
                    sp.speak("Enter your lastname")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text
                else:
                    print("Say ok for confirm quantity or say your lastname again")
                    sp.speak("Say ok for confirm quantity or say your lastname again")

            elif condition == "address":

                if(count==0):
                    print("Enter your address")
                    sp.speak("Enter your address")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text
                else:
                    print("Say ok for confirm quantity or say your address again")
                    sp.speak("Say ok for confirm quantity or say your address again")

            elif condition == "city":

                if(count==0):
                    print("Enter your city")
                    sp.speak("Enter your city")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text
                else:
                    print("Say ok for confirm quantity or say your city again")
                    sp.speak("Say ok for confirm quantity or say your city again")

            elif condition == "state":

                if(count==0):
                    print("Enter your state")
                    sp.speak("Enter your state")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text
                else:
                    print("Say ok for confirm quantity or say your state again")
                    sp.speak("Say ok for confirm quantity or say your state again")

            elif condition == "zip":

                if(count==0):
                    print("Enter your zip(postal) Code")
                    sp.speak("Enter your zip Code")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text
                else:
                    print("Say ok for confirm quantity or say your zip Code again")
                    sp.speak("Say ok for confirm quantity or say your zip Code again")

            elif condition == "phone":

                if(count==0):
                    print("Enter your phone Number")
                    sp.speak("Enter your phone Number")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text
                else:
                    print("Say ok for confirm quantity or say your phone Number again")
                    sp.speak("Say ok for confirm quantity or say your phone Number again")

            elif text == "back":
                import Engine as eng
                eng.back()

            elif text == "otp":

                if(count==0):
                    print("Enter The OTP code")
                    sp.speak("Enter The OTP code")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text
                else:
                    print("Say ok for confirm quantity or say your OTP code again")
                    sp.speak("Say ok for confirm quantity or say your OTP code again")

            elif text == "card name":

                if(count==0):
                    print("Enter your card name")
                    sp.speak("Enter your card name")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text
                else:
                    print("Say ok for confirm quantity or say your card name again")
                    sp.speak("Say ok for confirm quantity or say your card name again")

            elif text == "card number":

                if(count==0):
                    print("Enter your card number")
                    sp.speak("Enter your card number")
                    import speechRecognizer as recog 
                    text = recog.talk()
                    if text != statement:
                        usrpss = text
                else:
                    print("Say ok for confirm quantity or say your card number again")
                    sp.speak("Say ok for confirm quantity or say your card number again")

            elif text == "exit":
                break

        except:
            print("Unknown Command !!!")
        count=count+1
    return usrpss
