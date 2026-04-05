import pandas as pd
data={
    "Name":["Ayush","Babita","Rohan","Ajay","Annu","Jaggu","Oggy","Paplu"],
    "Age":[32,20,30,54,56,30,18,14],
    "Salary":[50000,40000,60000,34000,32000,1000,30000,450000],
    "P_S":[85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)
# print("Sample data frame")
# print(df)

print("Descriptive Statistics")
print(df.describe())