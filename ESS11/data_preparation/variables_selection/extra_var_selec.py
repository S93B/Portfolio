import pandas as pd
from ESS11.documentation.lists_dic_repository import dic_political_parties

###IGNORE FOR NOW

df = pd.read_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\raw\ESS11.csv')

dd = df.loc[df['cntry'] == 'NL']

media_use = dd.loc[:, ['nwspol', 'netusoft', 'netustm']]

safe_var = dd.loc[:, ['crmvct', 'aesfdrk']]

satisfaction_society = dd.loc[:, ['stflife', 'stfeco', 'stfgov', 'stfdem', 'stfedu', 'stfhlth']]

