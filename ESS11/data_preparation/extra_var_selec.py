import pandas as pd
from ESS11.documentation.lists_dic_repository import dic_political_parties
df = pd.read_csv(r'/ESS11/data/raw/ESS11.csv')

dd = df.loc[df['cntry'] == 'NL']

media_use = dd.loc[:, ['nwspol', 'netusoft', 'netustm']]

safe_var = dd.loc[:, ['crmvct', 'aesfdrk']]
