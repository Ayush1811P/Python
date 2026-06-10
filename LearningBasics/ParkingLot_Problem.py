"""
build a parking system 
rules:
0-30 min: 10 Rupees
31-120 mins: 35 Rupees
after that per 10 min 2 rupees

one floor an have 3 cars and 2 bikes at max total 5 vehicles
3 floors available
unique code for parking and taking out vehicle

"""

# pyrefly: ignore [missing-import]
import time 
def charges(entery_time ,exit_time):
   total_time= exit_time   - entery_time
   total_fee=0
   try:
    if total_time<=30:
        total_fee=10
    elif total_time>=31 and total_time<=120:
        total_fee=35
    elif total_time>120:
        temp_time= exit_time-entery_time 
        temp_time= temp_time-120
        temp_time= temp_time//10
        total_fee=temp_time*2+35    
   except ValueError:
        print("Some error occured we are sorry for Inconvineance ")
   return total_fee


print(charges(0,200))    
def space_for_parking():
    floors=3
    cars=0
    bikes=0
    

def code_for_vehicle():
    ...
def time_calculator():
    ...
def main():
    ...                
