        #PROGRAM ONE

# students={
#     "Name":"Aayu",
#     "Course":"BCA",
#     "Branch":"SOET"
# }
# print(students.keys(),students.values())
# for key,value in students.items():
#     print(key,":",value)


        #PROGRAM 2 Count frequency

# arr=[1,2,3,2,4,2,4,2,3,2,4,2]
# freq={}
# for x in arr:
#     freq[x]=freq.get(x,0)+1

# print(freq)




                #PROGRAM 3
# student={
#     "Aayu":85,
#     "Babbu":35,
#     "baayu":55,
#     "rohit":95,
# }
# top_student=""
# max_marks=0
# for name,marks in student.items():
#     if marks > max_marks:
#         max_marks=marks
#         top_student=name

# print("Top Student: ",top_student)
# print("Marks: ", max_marks)



        #MERGE 2 DICTIONARYS#  dictionary1.update(dictionary2)
# d1={"a":10,"b":20}
# d2={"c":30,"d":40}
# d1.update(d2)
# print(d1)

# d3= d1 | d2  #METHOD 2 TO MERGE
# print(d3)

# data={
#     "a":10,
#     "b":20,
#     "a":10,
#     "d":20,
#     "g":30
# }
# unique={}       #an empty dictionary
# seen_values=set()

# for key,value in data.items():
#     if value not in seen_values:
#         unique[key]=value
#         seen_values.add(value)

# print(unique)

# unique_keys={}
# seen_keys=set()
# for key in data.items():
#     if key not in seen_keys:
#         unique_keys=key
#         seen_keys.add(key)
# print(unique_keys)        



# students={
#     "Aayu": 85,
#     "Rohit": 8,
#     "Neha": 92,
#     "Aman": 88
# }
# lowest_student=""
# min_marks=100
# for name,marks in students.items():
#     if marks<min_marks:
#         min_marks=marks
#         lowest_student=name
# print("Student name: ",lowest_student)
# print("marks: ",min_marks)    
#     

employee={
    "name": "Ayush",
    "Age":23,
    "Salary":400000,
    "Role":"Data Scientist"
}
account={
    "users1":{"name":"Aayu","balance":10000},
    "users2":{"name":"Babbu","balance":20000}
}

user={
    "name":"Ayush Singh",
    "Skillz":["Python","Java","C"],
    "is_active":True,
    "Wallet":134000.65,
    "balance":1000
}
user["balance"]+=2000
employee["Experiance"] = "2 Years"
#print(employee["Experiance"])
employee.pop("Age")

# for key, value in employee.items():
#     print(key," : ",value)
employee["Experiance"]="Fresher"
#for key, value in employee.items():
#    print(key," : ",value)
account["users3"]={"name":"XYZ","balance":30000}
# for user_id,details in account.items():
#     print(user_id,"->",details["name"]," :",details["balance"])
user["Skillz"].append("SQL")
#print(user["Skillz"])
# if user["is_active"]:
#     print("User is Active")
total_money=user["Wallet"]+user["balance"]
# print("Total money is:",total_money)
#print(user.get("balance","Not-Available"))
# if "users4" in account:
#     print("users4 exists")
# else:
#     print("Users4 dose not exists")
emp2=employee.copy()
emp2["name"]="Changed"
extra_info={"Department": "AI","Location":"Banglore"}
employee.update(extra_info)
