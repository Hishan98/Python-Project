condition=""
def count(condition):
    statement = 0
    text = 10
    while text != statement:
        try:
        #     import speechRecognizer as recog
        #     text = recog.talk()
                
            if condition == "First":
                if text != statement:
                    usrpss = 1

            elif condition == "Second":
                if text != statement:
                    usrpss = 2

            elif condition == "Third":
                if text != statement:
                    usrpss = 3

            elif condition == "Fourth":
                if text != statement:
                    usrpss = 4

            elif condition == "Fifth":
                if text != statement:
                    usrpss = 5

            elif condition == "Sixth":
                if text != statement:
                    usrpss = 6

            elif condition == "Seventh":
                if text != statement:
                    usrpss = 7
                    
            elif condition == "Eighth":
                if text != statement:
                    usrpss = 8
                    
            elif condition == "Ninth":
                if text != statement:
                    usrpss = 9
                    statement=statement+1
                    
            elif condition == "Tenth":
                if text != statement:
                    usrpss = 10
        except Exception as ee:
            print("Unknown Command !!!"+ee)

    return usrpss

def main():
        num=count("Ninth")
        print(num)
main()
