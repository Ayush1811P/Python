import pandas as pd
from describe import data
df=pd.DataFrame(data)

        #applying single condition on rows
# high_salary=df[df["Salary"] > 50000]
# print("HIGH SALARY > 50000")
# print(high_salary)

        #applying multiple condition on rows
        #salary>50k & age>30
age_salary=df[(df["Age"]>40) & (df["Salary"]>50000)]
#print("EMPLOYEE WHERE AGE AND SALAY FILTERED")
#print(age_salary)

        #applying multiple condition on rows
        #salary>50k or age>30
using_or_condition=df[(df["Age"]>0) | (df["P_S"]>90)]        
print(using_or_condition)