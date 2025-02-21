import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from ESS11.utilities.functions import shapiro_test

path = 'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf_kneighbor.csv'
df = pd.read_csv(path, index_col=0)

f, ax = plt.subplots(figsize=(20,14))
corr = df.corr(numeric_only=True, method='pearson')
hm = sns.heatmap(round(corr,2), annot=True, ax=ax, cmap="coolwarm",fmt='.2f', vmin=-1, vmax=1, yticklabels=corr.columns, xticklabels=corr.columns)
f.subplots_adjust(top=0.83)
t= f.suptitle('Correlation Heatmap', fontsize=14)
plt.savefig(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\correlation_heatmap_all.png')

alpha = 0.05

#FIXME model is no bueno
#Model
x = df.stfdem
y = df.political_trust
X = sm.add_constant(x)

mod = sm.OLS(y,X)
res = mod.fit()
print(res.summary())
dir(res)

residuals = res.resid
y_pred = res.predict(X)

#Using shapiro to determine normality of residuals
shapiro_test(residuals, alpha)

# Inspect residuals histogram, extra for determining normality
sns.histplot(residuals, kde=True)
plt.title('Residuals Distribution')
plt.show()

# Plotting the regression line and predictions on the data with model predictions
plt.figure(figsize=(10, 6))

# Scatter plot of the true values
plt.scatter(x, y, color='blue', label='Actual values')

# Regression line based on predictions
plt.plot(x, y_pred, color='red', linewidth=2, label='Regression line')

# Adding labels and title
plt.xlabel('stfgov')
plt.ylabel('Political Trust')
plt.title('Regression Model and Predictions')
plt.legend()
plt.show()

# Q-Qplot for comparing quantiles of residuals
sm.qqplot(residuals, line='45')
plt.title('Q-Q Plot of Residuals')
plt.show()