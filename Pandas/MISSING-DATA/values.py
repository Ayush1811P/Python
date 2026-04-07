
data={
    "Name":["Ayush","Babita",None,"Ajay","Annu","Jaggu","Oggy","Paplu"],
    "Age":[32,20,None,54,56,30,18,14],
    "Salary":[50000,40000,None,34000,32000,1000,30000,450000],
    "P_S":[85,90,None,92,88,95,80,89]
}
import pandas as pd
df=pd.DataFrame(data)
df["Age"]=df["Age"].fillna(df["Age"].mean())#1

#HANDLING NULL VALUE WITH THE MEAN OF THE COLUMN

df["Salary"]=df["Salary"].fillna(df["Salary"].mean())#2

df["P_S"]=df["P_S"].fillna(df["P_S"].mean())#3


print(df)
