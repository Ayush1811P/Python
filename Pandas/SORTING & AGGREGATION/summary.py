#Summary Statastics
from sorting import data
import pandas as pd
#.mean(), .mode(), .max(), .min(), .sum()
df=pd.DataFrame(data)



avg_salary=df["Salary"].mean()
print(avg_salary)