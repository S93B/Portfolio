import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = "/ESS11/archive/data_NL_transf_kneighbor_v3.csv"
df = pd.read_csv(path, index_col=0)

df_pol = df.loc[:, ['age', 'gender', 'education', 'educational_level', 'activity_work', 'voted', 'political_trust']]

#todo Group age in categories for plot

# Group the data by age and gender, calculate percentages
age_gender = (
    df_pol.groupby(['age', 'gender'])
    .size()
    .reset_index(name='count')
    .pivot(index='age', columns='gender', values='count')
    .fillna(0)
)

# Convert counts to percentages
age_gender_percent = age_gender.div(age_gender.sum(axis=1), axis=0) * 100

# Create the pyramid plot
plt.figure(figsize=(12, 8))

# Plot for category 1 (e.g., Female)
plt.barh(age_gender_percent.index, -age_gender_percent['Female'], color='lightcoral', label='Female')

# Plot for category 2 (e.g., Male)
plt.barh(age_gender_percent.index, age_gender_percent['Male'], color='skyblue', label='Male')

# Add labels
plt.xlabel('Percentage')
plt.ylabel('Age')
plt.title('Age Pyramid by Gender')
plt.legend(loc='upper right')
plt.axvline(0, color='black', linewidth=0.5)  # Add a vertical line at 0

# Show plot
plt.tight_layout()
plt.savefig(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\age.png')
#plt.show()