import pandas as pd
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

path = r'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf_kneighbor_v2.csv'
df = pd.read_csv(path, index_col=0)

#TODO model uitwerken in mindmap

f, ax = plt.subplots(figsize=(20,14))
corr = df.corr(numeric_only=True, method='pearson')
hm = sns.heatmap(round(corr,2), annot=True, ax=ax, cmap="coolwarm",fmt='.2f', vmin=-1, vmax=1, yticklabels=corr.columns, xticklabels=corr.columns)
f.subplots_adjust(top=0.83)
t= f.suptitle('Correlation Heatmap', fontsize=14)
plt.show()
#plt.savefig(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\correlation_heatmap_all.png')

########################################## niet gebruiken
stat, p_value=stats.shapiro(df['political_trust'])
print(p_value)
print(stat)

alpha = 0.05
if p_value > alpha:
    print("Sample looks Gaussian (fail to reject H0)")
else:
    print("Sample does not look Gaussian (reject H0)")

#Recode education categories into integers for analysis
educational_bins = [0, 5, 11, 18]
educational_levels = [1,2,3]
df['educational_level'] = pd.cut(df['education'], bins=educational_bins, labels=educational_levels)

sns.scatterplot(df, x='stfgov', y='political_trust')
g = sns.jointplot(x="stfgov", y="political_trust", data=df,
                  kind="reg", truncate=False,
                  xlim=(0, 60), ylim=(0, 12),
                  color="m", height=7)
plt.show()


X = df[['stfgov']]
y = df[['political_trust']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")
