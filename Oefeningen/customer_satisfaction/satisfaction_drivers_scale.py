import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from factor_analyzer import FactorAnalyzer, calculate_kmo, calculate_bartlett_sphericity
from ESS11.utilities.factoranalysis_function import *
import pingouin as pg

df = pd.read_csv("C:\Python homedirectory\Portfolio_git\Oefeningen\customer_satisfaction\E-commerce_NPA_Dataset.csv", index_col=0)
print(df.info())

#determine which driver of satisfaction has most signficant impact
sf = df.iloc[:,4:8]
sf_desc = sf.describe()

sns.scatterplot(x=sf.ProductQualityRating, y=sf.CustomerServiceRating)
plt.show()
#Creating mean scale for satisfaction, first factor analysis
factor_analysis(sf, 3)

print(pg.cronbach_alpha(sf)) # alpha = .039