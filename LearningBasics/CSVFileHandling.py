import csv
with open("studentData.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["name","age","course"])
    writer.writerow(["Pyush",23,"BCA"])
    writer.writerow(["Ayush",22,"BCA"])
    writer.writerow(["Abita",20,"BCA"])
    writer.writerow(["Babita",18,"BCA"])


# print("\nDisplay values with not Attributes")

# with open("studentData.csv","r")as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)    



# print("\nDisplay only values not Attributes")
# with open("studentData.csv","r")as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         print(row)        


with open("studentData.csv","a",newline="")as file:
    writer = csv.writer(file)
    writer.writerow(["Anonymous",19,"BBA"])



print("Data Display after append")
with open("studentData.csv","r")as file:
    reader=csv.reader(file)
    #next(reader)
    for row in reader:
        print(row)    