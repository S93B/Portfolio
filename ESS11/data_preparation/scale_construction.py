import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg

#first figure out factor analysis


from ESS11.data_preparation.var_selection import ptrust_var
# TODO: combineren tot schaal.
print(ptrust_var.describe())
print(pg.cronbach_alpha(data=ptrust_var)) # alfa == 0.9

ptrust_var['trust_scale'] = ptrust_var.mean(axis=1) #/ (len(ptrust_var.columns) - 1)