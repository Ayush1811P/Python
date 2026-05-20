import pandas as pd
from values import data
df=pd.DataFrame(data)
print("\n******************ORIGINAL DATA******************\n")
print(df)
print("\n******************MODIFIED COLUMN DATA******************\n")
#df.drop(columns=["Column_name"],inplace=True)
df.drop(columns=["P_S"],inplace=True)
print(df)

#if drop multiple columns
#df.drop(columns=["P_S","Age"],inplace=True)