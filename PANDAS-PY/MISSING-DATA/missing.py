import pandas as pd
from values import data
df=pd.DataFrame(data)
#print(df.isnull())
print(df.isnull().sum())