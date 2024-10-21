import pandas as pd
from ESS11.documentation.lists_dic_repository import dic_political_parties

###IGNORE FOR NOW

df = pd.read_csv(r'C:\Python homedirectory\Portfolio_git\ESS11\data\raw\ESS11.csv')

dd = df.loc[df['cntry'] == 'NL']

media_use = dd.loc[:, ['nwspol', 'netusoft', 'netustm']]

safe_var = dd.loc[:, ['crmvct', 'aesfdrk']]

satisfaction_society = dd.loc[:, ['stflife', 'stfeco', 'stfgov', 'stfdem', 'stfedu', 'stfhlth']]

masculine_feminine = dd.loc[:, ['likrisk', 'liklead', 'sothnds', 'actcomp', 'mascfel', 'femifel', 'impbemw']]

#var selection social trus
soc_trust = dd.loc[:, ['ppltrst', 'pplfair', 'pplhlp',]]

#health variable selection
health_var = dd.loc[:, ['etfruit', 'eatveg', 'dosprt', 'cgtsmok', 'alcfreq', 'alcwkdy', 'alcwknd', 'alcbnge',]]
bmi = dd.loc[:, ['height', 'weighta']]

#var selection subjective-wellbeing; identity etc
nat_id_var = dd.loc[:, ['atchctr', 'atcherp']]
### Add var below
add_df = pd.read_csv(r'/ESS11/archive/data_NL_transf_v2.csv')

political_party = dd.loc[: ,['prtclhnl', 'prtdgcl', 'lrscale']]
political_descr = political_party.describe()
from ESS11.documentation.lists_dic_repository import list_sentinel_thou, list_sentinel_ten
