from vehicle_code_generator import code_generator 
from space import Parking_space

import json
import os
record=[]

def Vehicle_entry(vehicle_type):

    is_entered=False
    P=Parking_space(vehicle_type)
    if P==True:
        floor=Parking_space(vehicle_type)
        code=code_generator()
        print(f"Your code is: {code}")
        data={
        "Vehicle":vehicle_type,
        "Vehicle Code":code
            }
        record.append(data)
        is_entered=True
    elif P==False:
        print("Sorry we are full \n You cannot park here")
        is_entered=False
    return is_entered


#TESTCASE 1
# print(Vehicle_entry())



#TESTCASE 2    
# ch=1   
# while (True):
#     v=input("enter your vehicle type: car || bike:  ")
#     Vehicle_entry(v)
#     ch=int(input("want to add more\n1:YES || 0:NO  ") )
#     if ch==0:
#         for i in record:
#             print(i)
#         break



  
