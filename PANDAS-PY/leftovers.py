import pandas as pd
import numpy as np

# -------------------------------
# SAMPLE DATASET
# -------------------------------
data = {
    "Name": ["Aayu", "Rohan", "Aayu", "Annu", "Rohan", None],
    "Age": [23, 25, 23, None, 25, 30],
    "Salary": [50000, 60000, 50000, 45000, None, 70000],
    "Department": ["IT", "HR", "IT", "HR", "IT", "HR"]
}

df = pd.DataFrame(data)

print("\n===== ORIGINAL DATA =====\n")
print(df)


# -------------------------------
# 1. BASIC EXPLORATION
# -------------------------------
# print("\n===== BASIC INFO =====\n")
# print(df.head(3))
# print("\nNull Values:\n", df.isnull().sum())
# print("\nData Types:\n", df.dtypes)


# # -------------------------------
# # 2. DATA CLEANING
# # -------------------------------
# print("\n===== DATA CLEANING =====\n")

# # Fill missing values
# print(df.fillna(df["Age"].mean()))
# print(df.fillna(df["Salary"].median()))

# Drop rows where Name is null
#print("\n",df.dropna(subset=["Name"]))




# # -------------------------------
# # 3. INDEXING (loc & iloc)
# # -------------------------------
# print("\n===== INDEXING =====\n")

#print("Using loc:\n", df.loc[df["Age"] > 23, ["Name", "Salary"]])
#print("\nUsing iloc:\n", df.iloc[0:2, 0:3])


# # -------------------------------
# # 4. STRING OPERATIONS
# # -------------------------------
# print("\n===== STRING OPERATIONS =====\n")

# df["Name"] = df["Name"].str.upper()
# # print(df["Name"])

# print("\nNames containing 'RA':\n", df[df["Name"].str.contains("R","A")])


# # -------------------------------
# # 5. DUPLICATES
# # -------------------------------
# print("\n===== DUPLICATES =====\n")

# print("Duplicate rows:\n", df.duplicated())
# df = df.drop_duplicates()
# print("\nAfter removing duplicates:\n", df)


# # -------------------------------
# # 6. RENAME COLUMNS
# # -------------------------------
# print("\n===== RENAME COLUMNS =====\n")

#df.rename(columns={"Salary": "Income"}, inplace=True)
# print(df.columns)


# # -------------------------------
# # 7. APPLY FUNCTION
# # -------------------------------
# print("\n===== APPLY FUNCTION =====\n")

# df["Salary"] = df["Salary"].apply(lambda x: x * 1.1)
# print("\n",df)


# # -------------------------------
# # 8. VALUE COUNTS
# # -------------------------------
# print("\n===== VALUE COUNTS =====\n")

#print("\n",df["Department"].value_counts())

 
# # -------------------------------
# # 9. GROUPBY
# # -------------------------------
# print("\n===== GROUPBY =====\n")

# print("Average Income per Department:\n",
#       df.groupby("Department")["Income"].mean())

# print("\nCount per Department:\n",
#       df.groupby("Department")["Name"].count())


# # -------------------------------
# # 10. PIVOT TABLE
# # -------------------------------
# print("\n===== PIVOT TABLE =====\n")

# pivot = pd.pivot_table(df, values="Salary",
#                        index="Department",
#                        aggfunc="mean")
# #print(pivot)
# pivit2=pd.pivot_table(df,values="Salary", index="Name", aggfunc=" ")
# print(pivit2)


# # -------------------------------
# # 11. SORTING
# # -------------------------------
# print("\n===== SORTING =====\n")

# print(df.sort_values(by="Income", ascending=False))


# # -------------------------------
# # 12. CONCAT
# # -------------------------------
# print("\n===== CONCAT =====\n")

# df2 = df.copy()
# combined = pd.concat([df, df2], axis=0)
# print(combined)


# # -------------------------------
# # 13. DATA TYPES
# # -------------------------------
# print("\n===== DATA TYPE CONVERSION =====\n")

# df["Age"] = df["Age"].astype(int)
# print(df.dtypes)


# # -------------------------------
# # 14. EXPORT DATA
# # -------------------------------
# print("\n===== EXPORTING FILES =====\n")

# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)

# print("Files saved: output.csv & output.xlsx")


# # -------------------------------
# # FINAL OUTPUT
# # -------------------------------
# print("\n===== FINAL DATA =====\n")
# print(df)