# import random
# def otp_generator():
#     OTP=random.randint(1000,9999)
#     return OTP

# def otp_verification (OTP):
#     chances=0
#     while chances < 5:
#         if chances==4:
#             print("this is your last chance!")
#         user_OTP=int(input("enter otp: "))
#         if user_OTP==OTP:
#             print("OTP verified")
#             return
#         else:
#             print("try again")
#             chances=chances+1
#     print("OTP bloced Too many attempts!")


# def main():
#     OTP=otp_generator()     
#     print("Generated OTP: ",OTP)   
#     otp_verification(OTP)
# main()    

import random
import time
def otp_generator():
        OTP=random.randint(1000,9999)
        gen_time=time.time()
        return OTP, gen_time
def otp_verification(OTP,gen_time):
        expiry_time=30
        chance=0

        while chance <3:
                current_time=time.time()
                elpased = current_time-gen_time
                remaining = int(expiry_time-elpased)
                if remaining<=0:
                    print("'OTP EXPIRED")
                    return
                
                print(f"\nTime left: {remaining} seconds")

                if chance ==2:
                       print("this is your last chance!")
                user_otp=int(input("Enter otp: "))

                if user_otp==OTP:
                       print("OTP Verified!")
                       return       
                else:
                       print("try again!")
        print("otp verification failed!")               
def main():
       OTP,gen_time=otp_generator()
       print("Generated OTP: ",OTP)
       otp_verification(OTP,gen_time)

main()       