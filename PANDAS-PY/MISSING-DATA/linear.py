import pandas as pd
data={
    "Time":[1,2,3,4,5],
    "Values":[10,20,30,None,50]
}
df=pd.DataFrame(data)
print("**************BEFORE INTERPOLATION**************")
print(df)
print("\n**************BEFORE INTERPOLATION**************\n")
df["Values"]=df["Values"].interpolate(method="linear")
print(df)
