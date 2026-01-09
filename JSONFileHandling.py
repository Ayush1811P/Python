import json
data={
    "Name": "Ayush",
    "Age": 22,
    "Course":"BCA", 
    "Skills":["Python, Java, C"]
} 

with open("data.json","w")as file:
    json.dump(data, file, indent = 4)

# with open("data.json","r")as file:
#     data=json.load(file)
# print(data)
# print(data["Name"])        

from pathlib import Path

file_path=Path("data.json")
Data={
     "Name": "Babbu",
    "Age": 18,
    "Course":"BCA",
    "Skills":["Python, Java, C"]


}

