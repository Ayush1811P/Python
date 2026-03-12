def email_verification(email):
    is_correct=False
    k,j,d=0,0,0
    if len(email)>6:#1
        if email[0].isalpha():#2
            if "@" in email and email.count("@")==1:#3
                if (email[-3]==".") ^ (email[-4]=="."):#4
                    for c in email:
                        if c == c.isspace():#5
                            #print("Space Error")
                            k=1
                        elif c.isalpha():
                            if c==c.upper():#5
                                #print("upper Error")
                                j=1
                        elif c.isdigit():
                            continue
                        elif c=="@" or c=="_" or c==".":
                            continue
                        else:#5
                            #print("Space Error")
                            d=1        
                    if c!=1 or j!=1 or d!=1:#5
                           is_correct=True   
                    #else:
                        #print("error phase 5")
                               
    return is_correct

#print(email_verification("ayush1811@gmail.com"))

def pass_verification(password,email):
    correct=False
    if email_verification(email):#1
        #print("correct email!")#keep it while the login system not prepared!
        list_password=[int(d) for d in str(password)]#converting into list to get length of total numbers present
        if len(list_password)==6:#2
            correct=True
    # else:
    #     print("Email verification failed at password verify")
    return correct
import time
def login():
    email=input("\tEnter Email: ")
    password=int(input("\tEnter 6 Digit PIN: "))  
    mail=email_verification(email)
    pin=pass_verification(password,email)
    
    if mail==True and pin==True:
        print("\tloging in....please wait...")
        time.sleep(2)
        print()
        print("**************WELCOME TO THE HOMEPAGE**************")

    else:
        print("\tWRONG CREDENTIALS")

login()