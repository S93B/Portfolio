import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import seaborn as sns

path = r'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf_kneighbor_v2.csv'
df = pd.read_csv(path, index_col=0)

alpha = 0.05

#Model
x = df.stfgov
y = df.political_trust
X = sm.add_constant(x)

mod = sm.OLS(y,X)
res = mod.fit()
print(res.summary())
dir(res)

residuals = res.resid
y_pred = res.predict(X)

#Using shapiro to determine normality of residuals
stat, p_value = stats.shapiro(residuals)
print(f"Shapiro-Wilk test p-value for distribution: {p_value}")
print(f"Shapiro-Wilk test statistic for distribution: {stat}")

if p_value > alpha:  # H0 = normally distributed variable
    print("Variable look Gaussian (fail to reject H0)")
else:
    print("Variable do not look Gaussian (reject H0)")

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