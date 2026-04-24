"""
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




                        # types 
                        # PCB DIAGRAM 
                        # SCHEDYULING ALGORITHMS(SJF,RR,PRIORITY )
                        # DEAD LOCK 
                        # PREVENSION AND AVOIDANCE ()
"""

import time
import random

def calculate_metrics(original, user_input, duration):
    # Standard WPM calculation: (characters / 5) / minutes
    # One 'word' is traditionally defined as 5 characters including spaces
    minutes = duration / 60
    words = len(user_input) / 5
    wpm = round(words / minutes) if minutes > 0 else 0
    
    # Calculate errors and accuracy
    errors = 0
    # Use zip to compare only up to the shortest string length to avoid IndexErrors
    for char_orig, char_user in zip(original, user_input):
        if char_orig != char_user:
            errors += 1
            
    # Add extra characters as errors if user typed more than original
    errors += max(0, len(user_input) - len(original))
    
    # Add missing characters as errors if user typed less than original
    errors += max(0, len(original) - len(user_input))
    
    accuracy = 0
    if len(original) > 0:
        # Accuracy relative to the original length
        accuracy = round(((len(original) - min(errors, len(original))) / len(original)) * 100, 2)
    
    return wpm, errors, max(0, accuracy)

def main():
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
    
    target_text = random.choice(strings)
    
    print("\n" + "="*50)
    print("           TYPING SPEED TEST  ")
    print("="*50)
    print(f"\nType the following sentence exactly:\n")
    print(f"  \"{target_text}\"\n")
    
    input("Press Enter when you are ready to start...")
    
    print("\nGO!")
    start_time = time.time()
    user_text = input("> ")
    end_time = time.time()
    
    duration = end_time - start_time
    wpm, errors, accuracy = calculate_metrics(target_text, user_text, duration)
    
    print("\n" + "-"*50)
    print(f"{'RESULTS':^50}")
    print("-"*50)
    print(f"  Time Taken  : {round(duration, 2)} seconds")
    print(f"  Typing Speed: {wpm} WPM (Words Per Minute)")
    print(f"  Total Errors: {errors}")
    print(f"  Accuracy    : {accuracy}%")
    print("-"*50)
    
    if accuracy == 100:
        print("  Perfect! You're a pro.")
    elif accuracy > 90:
        print("  Great job! Very accurate.")
    else:
        print("  Keep practicing to improve your accuracy.")
    print("="*50 + "\n")


main()

# 25.4K
