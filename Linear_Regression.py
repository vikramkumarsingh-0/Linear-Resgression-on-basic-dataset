import pandas as pd
import streamlit1 as st
df = pd.read_csv("data.csv")
# print(df.info(True))
# print(df)
# df.dropna(inplace=True)
# print(df)
# df.mean()  # mean of all columns 
# df.median()  # median of all columns
# df.mode()  # mode of all columns

df.fillna(df["Marks"].median(), inplace=True) # here we use median as it is not changes on slightly different values
print(df)

print(df.duplicated())

df.drop_duplicates(inplace=True)
print(df)