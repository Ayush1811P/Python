from entry_of_veicle import record
from bill import charges 
def exit_of_vehicle(total_mins,code):
    for vehicle in record:
        if vehicle["Vehicle Code"]==code:
            fee=charges(total_mins)
            record.remove(vehicle)
            print(f"YOUR TOTAL BILL IS: {fee}")
            return
    print("VEHICLE CODE INVALID")
