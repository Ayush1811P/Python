
floor1={
        "bike":0,
        "car":0
    }
floor2={
    "bike":0,
    "car":0}
floor3={
    "bike":0,
    "car":0}
   
def Parking_space(vehicle_type):
    is_available=False
    if floor1[vehicle_type]!=1:
        floor1[vehicle_type]+=1
        
        #print(F"Your {vehicle_type} is parked at floor 1")
        #print(floor1)
        is_available=True   
    elif floor2[vehicle_type]!=1:
        floor2[vehicle_type]+=1
        #print(F"Your {vehicle_type} is parked at floor 2")
        #print(floor2)
        is_available=True  
    elif floor3[vehicle_type]!=1:
        floor3[vehicle_type]+=1
        #print(F"Your {vehicle_type} is parked at floor 3")
        #print(floor3)
        is_available=True
    return is_available   

    #TESTED
# while(True):
#     vehicle=input("Enter vehicle type car || bike : ").lower().strip()
#     Parking_space(vehicle)
    