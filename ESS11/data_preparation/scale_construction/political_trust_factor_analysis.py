import pandas as pd
import numpy as np
from factor_analyzer import FactorAnalyzer, calculate_kmo, calculate_bartlett_sphericity
df = pd.read_csv('C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf.csv', index_col=0)

#trust variables
pol_trust = df.loc[:, ['trstprl', 'trstlgl', 'trstplc', 'trstplt', 'trstprt', 'trstep', 'trstun',]].dropna()
pol_trust = pol_trust.rename(columns={'trstprl': 't_parlement', 'trstlgl': 't_legalsystem', 'trstplc': 't_police', 'trstplt': 't_politicians', 'trstprt': 't_political_parties', 'trstep': 't_EU_parlement', 'trstun': 't_united_nations'})
print(pol_trust.isna().sum())
print(pol_trust.info())

# Check Data Suitability
df_numeric = pol_trust.select_dtypes(include=[np.number])

# Check KMO Measure
kmo_all, kmo_model = calculate_kmo(df_numeric)
print(f"KMO Measure: {kmo_model}")

# Perform Bartlett’s Test of Sphericity
chi_square_value, p_value = calculate_bartlett_sphericity(df_numeric)
print(f"Bartlett’s test: chi_square({chi_square_value}), p_value({p_value})")

# Perform Factor Analysis
fa = FactorAnalyzer(n_factors=2, rotation='varimax')
fa.fit(df_numeric)

# Extract and print factors
loadings = fa.loadings_
loadings_df = pd.DataFrame(loadings, index=df_numeric.columns, columns=['Factor 1', 'Factor 2'])
print("Factor Loadings:\n", loadings_df)

# Plot the scree plot
import matplotlib.pyplot as plt

ev, v = fa.get_eigenvalues()
plt.scatter(range(1, df_numeric.shape[1] + 1), ev)
plt.plot(range(1, df_numeric.shape[1] + 1), ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()