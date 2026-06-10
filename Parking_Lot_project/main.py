from entry_of_veicle import Vehicle_entry
from exit_vehicle import exit_of_vehicle
from show_data import Show_Data
def Main(): 
    print("WELCOME TO THE PARKING SERVICE")
    print("1: TO PARK VEHICLE || 2: TO TAKE VECHICLE  || 3: PRINT DATA")
    ch=0
    while (True):
        try:
            ch=int(input("\tEnter your choice: "))
            if ch==1:
                vehicle_type=input("Enter vehicle type \ncar || bike : ").lower().strip()
                Vehicle_entry(vehicle_type)
            elif ch==2: 
                total_mins=int(input("Entert total mins: "))  
                code=input("Enter code:  ")           
                exit_of_vehicle(total_mins,code)
            elif ch==3:
                Show_Data()
        except ValueError:
            print("OOPS SOME ERROR OCCURED")
Main()