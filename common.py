

def talk(condition):
    statement="ok"
    text="" 
    while text != statement:
        try:
            import speechRecognizer as recog 
            text = recog.talk()

            if condition == "quentity":
                print("How many items do you want?")
                if text != statement:
                    usrpss = text
                # import Engine as eng
                # eng.quantity(text)
                # break
            
            elif condition == "email":
                print("enter your E-mail")
                if text != statement:
                    usrpss = text

            elif condition == "password":
                print("Enter your Password")
                if text != statement:
                    usrpss = text

            elif condition == "firstname":
                print("Enter your firstname")
                if text != statement:
                    usrpss = text

            elif condition == "lastname":
                print("Enter your lastname")
                if text != statement:
                    usrpss = text

            elif condition == "address":
                print("Enter your address")
                if text != statement:
                    usrpss = text

            elif condition == "city":
                print("Enter your city")
                if text != statement:
                    usrpss = text

            elif condition == "state":
                print("Enter your state")
                if text != statement:
                    usrpss = text

            elif condition == "zip":
                print("Enter your zip(postal) Code")
                if text != statement:
                    usrpss = text

            elif condition == "phone":
                print("Enter your phone Number")
                if text != statement:
                    usrpss = text

            elif text == "back":
                import Engine as eng
                eng.back()

            elif text == "otp":
                print("Enter The OTP code")
                if text != statement:
                    usrpss = text

            elif text == "card name":
                print("Enter your card name")
                if text != statement:
                    usrpss = text

            elif text == "card number":
                print("Enter your card number")
                if text != statement:
                    usrpss = text
        except:
            print("Unknown Command !!!")

    return usrpss
