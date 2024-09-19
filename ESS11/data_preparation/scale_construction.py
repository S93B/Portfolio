import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg

df = pd.read_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf.csv', index_col=0)
corr_df = df.corr(numeric_only=True)

# TODO: first figure out factor analysis


from ESS11.data_preparation.var_selection import ptrust_var
# TODO: combineren tot schaal.
corr_ptrust = ptrust_var.corr(numeric_only=True)

print(ptrust_var.describe())
print(pg.cronbach_alpha(data=ptrust_var)) # alfa == 0.9

ptrust_var['trust_scale'] = ptrust_var.mean(axis=1) #/ (len(ptrust_var.columns) - 1)