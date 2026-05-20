import pandas as pd
from values import data
df=pd.DataFrame(data)
# print(df)


# print("]\nAfter bonus addition!")
# print("*"*30)
df["Bonus"]=df["Salary"]*0.1
# print(df)

#USING INSERT METHOD TO ADD COLUMN AT SPECIFIT INDEX NUMBER IN THE TABLE

    #SYNTAX
#df.insert(loc, " col_name",some_data)
df.insert(0,"Emp_id", [12,13,14,15,17,18,19,20])
print(df)