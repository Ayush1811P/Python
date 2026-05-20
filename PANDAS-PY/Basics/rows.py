#head() tail()
#head(n) if n not passed then default first 5 rows will be shown
#tail(n)if n not passed then default last 5 rows will be shown

import pandas as pd
df=pd.read_json("sample_Data.json")


print("Display 10 rows of first")
print(df.head(10))



print("----"*30)


print("Display 10 rows of last")
print(df.tail(10))


