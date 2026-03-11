# name=input("Enter name: ")
# file=open("Names.txt","a")
# file.write(f"{name} \n")
# file.close()
names=[]
with open("Names.txt","r") as file:
    for line in file:
        names.append(line.rstrip())
names=sorted(names,reverse=True)
for _ in names:
    print(f"hello,{_}")
# for line in lines:
#     print(f"Hello", line.rstrip())    

