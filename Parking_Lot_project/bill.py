import time 
def charges(total_time):
   total_fee=0
   try:
    if total_time<=30:
        total_fee=10
    elif total_time>=31 and total_time<=120:
        total_fee=35
    elif total_time>120:
        temp_time= total_time
        temp_time= temp_time-120
        temp_time= temp_time//10
        total_fee=temp_time*2+35    
   except ValueError:
        print("Some error occured we are sorry for Inconvineance ")
   return total_fee

 #TESTED
# print(charges(200))  