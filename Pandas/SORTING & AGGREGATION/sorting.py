import pandas as pd
data={
    "Name":["Ayush","Babita","Aayu"],
    "Age":[23,45,32],
    "Salary":[45000,56000,34000]
}
df=pd.DataFrame(data)

#get age as decs order
descending_age=df.sort_values(by="Age",ascending=False)
#print("**************Sorted by age**************")
#print(descending_age)


#get age as asc order
asc_age=df.sort_values(by="Age",ascending=True)
#print("**************Sorted by age**************")
#print(asc_age)


#for multiply column sorting
print(df.sort_values(by=["Age","Salary"],ascending=[True,False]))
                                                                