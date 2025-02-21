import pandas as pd
from pandas.api.types import CategoricalDtype

# RQ: Why are some countries more successful than other countries?
## Do Standard of Living (GDP), population and politics matter?
### Are come countries more successfull in Summer/Winter? Why?
#### Are in some countries men/women more successful? why?
##### Do traditions/national sports matter?

df_dic = pd.read_csv(r"C:\Python homedirectory\udemy_panda_cursus\new_things_practice\Pandas_course\Course_Materials_Part3\Explanatory_DataAnalysis_Challenge\dictionary.csv")
df_summer = pd.read_csv(r"C:\Python homedirectory\udemy_panda_cursus\new_things_practice\Pandas_course\Course_Materials_Part3\Explanatory_DataAnalysis_Challenge\summer.csv")
df_winter = pd.read_csv(r"C:\Python homedirectory\udemy_panda_cursus\new_things_practice\Pandas_course\Course_Materials_Part3\Explanatory_DataAnalysis_Challenge\winter.csv")

# Data import and inspection
df_dic.info()
df_summer.info()
df_winter.info()
# TODO Merging and concatenating
df_winter['Edition'] = 'Winter'
df_summer['Edition'] = 'Summer'
df = pd.concat([df_summer, df_winter])

#Function to add full country name
from Explanatory_data_challenge..pandas_opdr.Explanatory_data_challenge.functions import *
replace_country(df, df_dic, "Country_Name","Country", 'Code', 'Country')
df = df.rename(columns={"Country":"Code", "Country_Name":"Country"})

#TODO Data Cleaning
df.info()
print(df.isna().sum())

#print Codes for missing Countries
print(df.Code.unique())
missing_country_rows = df[df["Country"].isna()]
print(missing_country_rows.Code.unique())

# 6367 missings for Country; 4 for Code
df["Country"] = df["Code"].map(country_codes).fillna(df["Country"])
print(df.Country.nunique())

#remove rows with missing country codes
df = df.dropna()
df.reset_index(drop=True)
# Convert medal column into ordered categorical column Gold > Silver > Bronze
medal_order = CategoricalDtype(categories=["Bronze", "Silver", "Gold"], ordered=True)

# Convert the Medal column to an ordered categorical column
df["Medal"] = df["Medal"].astype(medal_order)

# Inspect the DataFrame
print(df)
print(df["Medal"].dtype)  # Verify the dtype is now "Categorical"
