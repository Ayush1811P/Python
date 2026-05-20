import pandas as pd
from values import data
df=pd.DataFrame(data)


        #NOW INSTEAD OF DROPING LETS FILL THE NULL VALUES
#df.fillna(default_value,inplace=True)
#df.fillna(0, inplace=True)
df["Age"].fillna(df["Age"].mean(),inplace=True)
print(df)