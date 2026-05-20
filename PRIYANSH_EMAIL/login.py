from email import mail
import webbrowser
from password import PASS
def login():
    try:
        E=input("Enter email:  ")
        try:
            P=int(input("Enter 6 DIGIT PIN: "))
            email=mail(E)
            passs=PASS(P)
            if email ==True and passs == True:
                return print("System login Success!")
                 
            else:
                return print("System login failed\nWrong Credentials")  
        except ValueError:
            return print("WRONG CREDENTIALS")
        
    except ValueError:
        return print("WRONG CREDENTIALS")
    finally:
            print("PROGRAM EXECUTED")
login()
    