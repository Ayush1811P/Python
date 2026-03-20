# import os
# names=["ayush","babbu","singh","bhardwaj"]

# with open("Data.txt","w")as file:
#     file=file.write("Ayush")


# with open ("Data.txt","r")as file:
#     data=file.readline()
#     print(data)

# with open("Data.txt","a") as file:
#     for name in names:
#         file.write(name)

# with open("Data.txt","r")as file:
#     print(file.readlines())


# if os.path.exists("Data.txt"):
#     os.remove("Data.txt")
#     print("Removed")
# else:
#     print("Not found!!")


# with open("Data.txt","w")as file:
#     for name in names:
#         file.write(name)

# with open ("Data.txt","r")as file:
#     print(file.readlines())

# with open("Data.txt","w")as file:
#     file.write("AYUSH")    


# with open("favorite_color.txt","w")as file:
#     file.write("BLUE")

# with open("favorite_color.txt","r")as file:
#     print(file.readline())
     
# with open("about_me.txt","w")as file:
#     file.write("Ayush")    
#     file.write("20")
#     file.write("Noida") 

# with open("about_me.txt","r")as file:
#     for line in file:
#         print(line.strip())

with open("fruits.txt","w")as file:
    file.write("Apple")

with open("fruit.txt","a")as file:
    file.write("Banana")
    
with open("fruit.txt","r")as file:
    for f in file:
        print(f.strip())    
    
        
            