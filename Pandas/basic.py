import pandas as pd

#READING DATA FROM CSV FILE INTO A DATA_FRAME

    #CSV
# df=pd.read_csv("sales_data_sample.csv",encoding='latin1')
# print(df)


        #EXCEL
# df=pd.read_excel("SampleSuperstore.xlsx")
# print(df)

        #JSON   
df=pd.read_json("sample_Data.json")
print(df)