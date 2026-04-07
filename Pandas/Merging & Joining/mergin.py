"""SYNTAX
pd.merge(dataFrame1, dataFrame2, on="col_name",how="tye-of-join")
"""
import pandas as pd
df_customer=pd.DataFrame({
    "Customer_id":[1,2,3],
    "Name":["Ayush","babita","Babbu"]
})

df_orders=pd.DataFrame({
    "Customer_id":[1,2,5],
    "Order_amount":[24,34,145]
})

#merging dataframes=

        #INNER JOIN
df_inner=pd.merge(df_customer,df_orders,on="Customer_id",how="inner")
#print(df_inner)


        #OUTER JOIN
df_Outer=pd.merge(df_customer,df_orders,on="Customer_id",how="outer")
#print(df_Outer)

        #LEFT JOIN
df_left=pd.merge(df_customer,df_orders,on="Customer_id",how="left")
#print(df_left)


        #Right JOIN
df_right=pd.merge(df_customer,df_orders,on="Customer_id",how="right")
#print(df_right)


        #CROSS JOIN
df_cross=pd.merge(df_customer,df_orders,how="cross")
print(df_cross)

