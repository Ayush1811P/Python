import pandas as pd

data={
    "Name":["Ayush","Babita","Rohan"],
    "Age":[10,30,40],
    "City":["Delhi","Noida","UK"]
}
df=pd.DataFrame(data)
print(df)


    ##SAVE DATA TO CSV FILE
#df.to_csv("OUTPUT.csv")
#df.to_csv("OUTPUT2.csv", index=False)



#SAVE DATA TO EXCEL FILE
#df.to_excel("EXCEL_OUTPUT.xlsx",index=False)


    ##SAVE DATA TO EXCEL FILE

#df.to_json("JSON_OUTPUT.json",index=False)    

