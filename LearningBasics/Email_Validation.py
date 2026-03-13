# correct=True
# while correct==True:
#     email=input("Enter email:")
#     k,j,d=0,0,0
#     if len(email)>6:#1
#         if email[0].isalpha():#2
#             if "@" in email and email.count("@")==1:#3
#                 if (email[-3]==".") ^ (email[-4]=="."):#4
#                     for c in email:
#                         if c == c.isspace():#5
#                             print("Space Error")
#                             k=1
#                         elif c.isalpha():
#                             if c==c.upper():#5
#                                 print("upper Error")
#                                 j=1
#                         elif c.isdigit():
#                             continue
#                         elif c=="@" or c=="_" or c==".":
#                             continue
#                         else:#5
#                             print("Space Error")
#                             d=1        
#                     if c==1 or j==1 or d==1:#5
#                         print("Error in phase 5")   
#                     else:
#                         print("correct Email")
#                         correct=False         
#                 else:
#                     print("Error in phase 4") 
#             else:
#                 print("Error in phase 3")
#         else:
#             print("Error in phase 2")
#     else:
#         print("Error in phase 1")

def registration():
    """Collects and validates basic user registration information.

    Returns True when all inputs pass simple validation checks.
    """

    name = input("Enter your name: ").strip()
    if not name:
        print("Enter name first!")
        return False

    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Age must be a number")
        return False

    if age <= 10:
        print("Enter age > 10")
        return False

    email = input("Enter your email: ").strip()
    if not email:
        print("Enter email")
        return False

    try:
        password = int(input("SET 6 Digit PIN: "))
    except ValueError:
        print("PIN must be a number")
        return False

    if len(str(password)) != 6:
        print("PIN must be 6 digits")
        return False

    return True

