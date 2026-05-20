data={
    "Name":["Ayush","Babita","Rohan","Ajay","Annu","Jaggu","Oggy","Paplu"],
    "Age":[32,20,32,54,14,32,14,14],
    "Salary":[50000,40000,60000,34000,32000,1000,30000,450000],
    "P_S":[85,90,78,92,88,95,80,89]
}
"""COMMON AGGREGATION FUNCTIONS
1-sum()
2-count()
3-min()
4-max()
5-std()
6-mean()
"""
import pandas as pd
df=pd.DataFrame(data)
    #SYNTAX
#group = df.groupby("COLNAME TO MAKE GROUP ")["COL NAME TO RETURN"].AGGREGATION()
grouped=df.groupby("Age")["Salary"].sum()
#print( grouped )

count=df.groupby("Age")["Salary"].count()
#print(count)





    #multiple columns grouping

mul_groupled =df.groupby(["Age","Name"])["Salary"].sum()
print(mul_groupled)