import pandas as pd
from values import data
df=pd.DataFrame(data)



#updation for row specific
#syntax:  #df.loc[roe_index,col_name]=new_value
df.loc[0,"Salary"]=100000
print(df)




print("\n\tAfter updation of salary by 5%\n")
#INCREASING SALARY BY 5%
df["Salary"]=df["Salary"]*1.05
print(df)