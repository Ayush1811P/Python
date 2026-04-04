import webbrowser
import time
from email1 import email_verification
from password1 import pass_verification
from details1 import details

def main():
    if details():
        if email_verification():
            if pass_verification():
                print("Redierecting to the webpage....")
                print("please wait")
                time.sleep(3)
                URL="https://www.linkedin.com/feed/"
                webbrowser.open(URL)
    
if __name__ =="__main__":
    main()        