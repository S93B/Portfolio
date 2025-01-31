import pandas as pd
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

# Why correlation is not causation: a confounder in action

# Reading the data
stand_data_df = pd.read_csv('C:\Python homedirectory\Portfolio_git\Oefeningen\icecream_summer\chap1-stand_data.csv')

# Presuming additional steps for analysis are to be included here
# Example: A simple regression model and plotting
model = ols("icecream_sales ~ temps", data=stand_data_df).fit()
print(model.summary())

# Scatter plot
sns.scatterplot(x='temps', y='icecream_sales', data=stand_data_df)
plt.xlabel("Temperature")
plt.ylabel("Ice Cream Sales")
plt.title("Ice Cream Sales vs Temperature")
# plt.show()

print(ols("icecream_sales ~ temps + summer_months + iced_coffee_sales",
          data=stand_data_df).fit().summary())