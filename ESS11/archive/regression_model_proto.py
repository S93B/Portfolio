import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

path = r'/ESS11/data/processed/data_NL_transf_kneighbor_v2.csv'
df = pd.read_csv(path, index_col=0)

alpha = 0.05

# R = .72 for stfgov - pol trust
X = df[['stfgov']]
y = df[['political_trust']]

# Calculate the p-value for the significance of the regression model
res = stats.mstats.linregress(X, y)
# slope, intercept, r_value, p_value, std_err = stats.linregress(df['stfgov'], df['political_trust'])

print(f"Significance level (p-value) for the regression model: {res.pvalue}")

if res.pvalue < 0.05:
    print('Model is significant, < 0.05')
else:
    print('Model is not significant, >= 0.05')

print(f"R-squared: {res.rvalue ** 2}")

plt.plot(X,y, 'o', label='Original data')
plt.plot(X, res.intercept + res.slope*X, 'r', label='fitted line')
plt.legend()
plt.show()

# Calculate the residuals
residuals = y - (res.intercept + res.slope * X)

# Perform the Shapiro-Wilk test on the residuals
def shapiro_test(data):
    stat, p_value = stats.shapiro(data)
    print(f"Shapiro-Wilk test p-value for distribution: {p_value}")
    print(f"Shapiro-Wilk test statistic for distribution: {stat}")

    if p_value > alpha:  # H0 = normally distributed variable
        print("Variable look Gaussian (fail to reject H0)")
    else:
        print("Variable do not look Gaussian (reject H0)")

shapiro_test(residuals)

# # Inspect residuals for better diagnosis
# residuals = y - y_pred
# sns.histplot(residuals, kde=True)
# plt.title('Residuals Distribution')
# plt.show()
#
# # Plotting the regression line and predictions on the data with model predictions
# plt.figure(figsize=(10, 6))
#
# # Scatter plot of the true values
# plt.scatter(X, y, color='blue', label='Actual values')
#
# # Regression line based on predictions
# plt.plot(X, y_pred, color='red', linewidth=2, label='Regression line')
#
# # Adding labels and title
# plt.xlabel('stfgov')
# plt.ylabel('Political Trust')
# plt.title('Regression Model and Predictions')
# plt.legend()
#
# # Show plot
# plt.show()
