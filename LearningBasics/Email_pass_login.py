# def registration():
#     sahi_hai=False
#     name=input("Enter your name: ")
#     if name ==None:
#         sahi_hai=False
#         print("Enter name first!")
#     age=int(input("enter you age: "))
#     if age==None or age <=10:
#         print("enter age >10")
#         sahi_hai=False
#     email=input("Enter your email: ")
#     if email==None:
#         sahi_hai=False
#     password=int(input("SET 6 Digit PIN: "))
#     if password==None:
#         sahi_hai=False 
#     sahi_hai=True    
#     return sahi_hai
#DO NOT USE REGISTRATION IT IS  NOT COMPLETE YET

import webbrowser as web
def email_verification(email):
    is_correct=False
    k,j,d,z=0,0,0,0
    if len(email)>6:#1
        if email[0].isalpha():#2
            if "@" in email and email.count("@")==1:#3
                if (email[-3]==".") ^ (email[-4]=="."):
                    for c in email:
                        if c == c.isspace():                          
                            k=1
                        elif c.isalpha():
                            if c==c.upper():
                                
                                j=1
                        elif c.isdigit():
                            continue
                        elif c=="@" or c=="_" or c==".":
                            continue
                        else: 
                            d=1 
                    pos=email.find("@")
                    for x in range(pos+1,len(email)):
                        if email[x].isdigit():
                            z=1
                            break               
                    if c!=1 or j!=1 or d!=1 :
                           if z!=1:  
                            is_correct=True                                
    return is_correct

def pass_verification(password,email):
    correct=False
    if email_verification(email):
        
        list_password=[int(d) for d in str(password)]
        if len(list_password)==6:
            correct=True   
    return correct
import time
def login():
    email=input("\tEnter Email: ")
    mail=email_verification(email)
    if mail==False:
        print("\tWRONG EMAIL")
        return
    password=int(input("\tEnter 6 Digit PIN: "))  
    
    pin=pass_verification(password,email)
    
    if mail==True and pin==True:
        print("\tloging in....please wait...")
        time.sleep(2)
        print()
        print("**************WELCOME TO THE HOMEPAGE**************")
        url = "https://www.google.com"
        web.open(url)
    else:
        print("\tWRONG CREDENTIALS")

login()