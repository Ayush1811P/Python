# name=input("Enter name: ")
# file=open("Names.txt","a")
# file.write(f"{name} \n")
# file.close()
# names=[]
# with open("Names.txt","r") as file:
#     for line in file:
#         names.append(line.rstrip())
# names=sorted(names,reverse=True)
# for _ in names:
#     print(f"hello,{_}")
# # for line in lines:
# #     print(f"Hello", line.rstrip())    

# password=int(input("Enter: "))
# digits=[int(d) for d in str(password)]
# for x in digits:
#     if x <0:
#         print("error")
#         break



user_password=input("Enter 6 Digit PIN: ")
P=[]
try:
    for s in user_password:
        if int(s)>=0:
            P.append(s)
    
except TypeError:
    print("Enter non-negative values")
print(P)

