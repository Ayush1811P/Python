import pandas as pd
from describe import data
#df=pd.read_json("sample_Data.json")
# print("Displayinf the info or dataset")
# print(df.info())


# data={
#     "Name":["Ayush","Babita","Rohan"],
#     "Age":[10,30,40],
#     "City":["Delhi","Noida","UK"]
# }

df=pd.DataFrame(data)
print("Displayinf the info or dataset")
print(df.info())

