import pandas as pd
from ESS11.documentation.lists_dic_repository import dic_political_parties
df = pd.read_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\raw\ESS11.csv')

dd = df.loc[df['cntry'] == 'NL']

#var selection media use; social trust and happiness
media_use = dd.loc[:, ['nwspol', 'netusoft', 'netustm']]
soc_trust = dd.loc[:, ['ppltrst', 'pplfair', 'pplhlp', 'happy']]
