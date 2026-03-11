def email_validation(email):
    correct=False
    k,j,d=0,0,0
    if len(email)>6:
        if email[0].isalpha():
            if email[0]==email[0].lower():
                pass
            elif "@" in email and email.count("@")==1:
                if (email[-3]==".") ^ (email[-4]=="."):
                    for c in email:
                        if c == c.isspace():
                            print("Space Error")
                            k=1
                        elif c.isdigit():
                            continue
                        elif c=="@" or c=="_" or c==".":
                            continue
                        else:
                            print("Space Error")
                            d=1        
                    if c==1 or j==1 or d==1:
                        print("Error in phase 5")   
                    else:
                        print("correct Email")
                        correct=True         
                else:
                    print("Error in phase 4") 
            else:
                print("Error in phase 3")
        else:
            print("Error in phase 2")
    else:
        print("Error in phase 1")

print(email_validation("ayush1811@gmail.com") )       