from time import *
import random
def mistakes(para,User_string):
    errors=0
    Words_left=len(para)-len(User_string)
    for ch in range(len(User_string)):
            if User_string[ch]!=para[ch]:
                errors+=1
    print("\tTOTAL ERRORS: ",errors)
    print("\tWORDS LEFT: ",Words_left)        
    return 

def total_time(start,end,user_string):
    calc_time=end-start
    calc_time=round(calc_time,2)
    speed=len(user_string)/calc_time
    return round(speed)

strings = [
    "The quick brown fox jumps over the lazy dog.",
    "Practice typing every day to improve your speed and accuracy.",
    "Programming requires patience, logic, and constant practice.",
    "Technology is best when it brings people together.",
    "Learning to code is like learning a new language.",
    "Small improvements every day lead to big results.",
    "A good developer always tests and debugs their code carefully.",
    "Typing speed improves with consistent practice and focus.",
    "Success comes from discipline, curiosity, and hard work.",
    "Computer science students often spend hours solving problems."
]
paragraph=random.choice(strings)
print("\tWELCOME TO TYPING SPEED TEST\n")
print("\t",paragraph)
print()
time_1=time()
user_input=input("\tStart: ")
time_2=time()
speed=total_time(time_1,time_2,user_input)
print()
errors=mistakes(paragraph,user_input)
print(f"\tSpeed is: {speed} w/s")



# username=[
#         "ayush1811@gmail.com",
#         "amansi0300@gmail.com",
#         "awsmsi0300@gmail.com"
#     ]

# def pass_auth(user_pass,stored_passw):
#     user_pass=int(input("Enter password: "))
#     if user_pass is None:
#         print("ENTER PASSWORD")
#     if len(user_pass)<6:
#         print("password too short")  