def email_verification():
    email=input("Enter email: ")
    k,j,d,z=0,0,0,0
    if len(email)>6:#1
        if email[0].isalpha():#2
            if "@" in email and email.count("@")==1:#3
                if (email[-3]==".") ^ (email[-4]=="."):#4
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
                            True                                
    return True

