import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pingouin as pg

from var_selection import ptrust_var
# TODO: combineren tot schaal.
print(ptrust_var.describe())
print(pg.cronbach_alpha(data=ptrust_var)) # alfa == 0.9