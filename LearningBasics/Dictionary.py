#A dictionary is an unordered,
# mutable collection of elements stored as key–value pairs.
#Key points:

# Stores data as key : value

# Keys must be unique

# Keys must be immutable (int, str, tuple)

# Values can be any data type

# Fast access (hashing)




    #METHODS OF DICTIONARY
#student.keys()
# student.values()
# student.item()
# student.update({updated values and keys})
# student.pop()
# student.popitem()
# student.clear()




# d={"a":1, "B":3}
# D= dict(name="Aayu", age=20)
# Dd={}       #empty dictiionary
# print(D["age"])
# print(D["name"])
# print(D.get("age"))     #THIS IS MORE SATE TO FETCH DATA


# student={
#     "name": "Aayu",
#     "age": 20,
#     "course": "BCA"
# }
# student["age"]=23   #updation of age, dictionary is mutable
# student["course"]="MSOET"



# print(student.get("course"))
# print(student.get("age"))
# print(student.get("name"))

# for key in student:
#     print(key)   #using loop to print all the keys in the dictionary

# for key,value in student.items():
#     print(key,value)     #using loop to print key and value together

# if student["age"]>=20:
#     print(student.get("age"))    



    #NESTED DICTIONARY

# Data={
#     "name": "Aayu",
#     "course": "BCA",
#     "marks":{
#         "Maths": 70,
#         "CS": 80,
#         "Science": 78,
#         "Civics":89
#     }
# }
# max_marks=0
# for value in Data["marks"].values():
#     if max_marks < value:
#         max_marks=value
# print(max_marks)
# print(max(Data["marks"].values()))#shortcut to find max marks
# print(Data["marks"])
# for key,value in Data.items():
#     print(key,value)


    #INPORTANT FOR NOTES
# data = {"a": 1, "b": 2}
# data["c"] = data.get("a") + data.get("b")
# data["d"]=data.get("a")+20
# print(data)


# data1 = {"x": 10}
# #print(data1.get("y", 0))

# s = set([1, 1, 1, 2])
# print(s)



#creating a list of dictionaries to make the program look simple hence all the key values are same
#in all those dictionaries
# students=[
#     {"name":"harry","house":"san-frans"},
#     {"name":"kevin","house":"san-frans"},
#     {"name":"bobby","house":"san-autria"},
#     {"name":"adam","house":None},

# ]

# for student in students:
#     print(student['name'],student['house'],sep=",")


# import random as r


# my_list=[]
# for x in range(10):
#     my_list.append(r.randint(1,9))
   

# print(my_list)

# import sys
# value=sys.argv[1]
# print("HELLO I AM ' ",value)



