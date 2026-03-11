#✅MAKE A MINI LOGIN PROGRAM FUNCTION

# def login(username,passw):
#     homepage="Accessing...."
#     if username =="admin" and passw=="1811":
#         print("login successful")
#     else:
#         return print("wrongpassword")    
# def main():
#     username=input("enter the username: ")
#     passw=input("Enter the 4 digit password: ")
#     login(username,passw)
# if __name__ == "main":
#     main()



#MAKE THE LOGIN()FUNCTION MORE ADVANCED

# lets convert this into a full program 
# user came registered by name,username,pass 
# then options are simple just addBalance,checkBalance,sendMoney
# and lets store all this in json file  or dictionary or something like that so i can learn file handling with real life code example and whenever user want can login with credentials and do operations add,check,send 
# and we will save it for further






# def login():
#     usernameAttempt=1

#     while usernameAttempt<=3:
#         username=input("Enter username: ")
#         if usernameAttempt==2:
#             print("this is your last attemt: ")
#         if username=="admin":
#             break
#         else:
#             usernameAttempt+=1    
#     if usernameAttempt==4:
#         return print("wrong username Account Locked!")
                

#     passAttempt=1
#     while passAttempt<=3:
#         password=int(input("Enteryour 4 digit password: "))
#         if passAttempt==2:
#             print("this is your last chance!")
#         if password==1811:
#             break   
#         else:
#             passAttempt+=1

#     if passAttempt==4:
#         return print("Wrong password Account Locked!")
        
#     else:
#         return print("Account Login Successfull")
    

# login()












# def authentication():
#     user_auth=False
#     username_attempts=1
#     passw_attempts=1
#     username="Admin"
#     passw=1811
#     while username_attempts<=3:
#         username_input=input("Enter username: ")
#         if username_attempts==2:
#             print("this is your last chance!")
#         if username.lower()==username_input.lower():
#             user_auth=True
#             break
#         else:
#             username_attempts+=1
        
#     if user_auth==True:
#         while passw_attempts<4:
#             if passw_attempts==4:
#                 print("Wrong password!...")
#                 return
#             password=int(input("Enter password: "))
#             if passw==password:
#                 print("correct credentials\n Loging in....")
#                 return
#             if passw_attempts==2:
#                 print("This is your last chance!")
#             else:
#                 passw_attempts+=1

        
# def login()->None:
#     print("Welcome to HDFC Bank please enter your credentials")
#     authentication()
#     ...
    
# login()