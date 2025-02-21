import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path = 'C:\Python homedirectory\Portfolio_git\ESS11\data\processed\data_NL_transf_kneighbor.csv'
df = pd.read_csv(path, index_col=0)

df_pol = df.loc[:, ['age', 'gender', 'education', 'educational_level', 'activity_work', 'voted', 'political_trust']]

#Create age groups for plot
age_bins = [0, 17, 24, 34, 44, 54, 64, 74, 120]
age_labels = ['0-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75+']

# Create a new column for age groups
df_pol['age_group'] = pd.cut(df_pol['age'], bins=age_bins, labels=age_labels, right=True)

# Verify the result
print(df_pol[['age', 'age_group']].head())

# Count age group occurrences
age_distribution = df_pol['age_group'].value_counts().sort_index()
print(age_distribution)

# Group the data by age and gender, calculate percentages
age_gender = (
    df_pol.groupby(['age_group', 'gender'])
    .size()
    .reset_index(name='count')
    .pivot(index='age_group', columns='gender', values='count')
)

# Convert counts to percentages
# age_genderpercent = age_gender.div(age_gender.sum(axis=1), axis=0) * 100

# Create the pyramid plot
plt.figure(figsize=(12, 8))

# Plot for category 1 (e.g., Female)
plt.barh(age_gender.index, -age_gender['Female'], color='lightcoral', label='Female')

# Plot for category 2 (e.g., Male)
plt.barh(age_gender.index, age_gender['Male'], color='skyblue', label='Male')

# Add labels
plt.xlabel('Count')
plt.ylabel('Age')
plt.title('Age Pyramid by Gender')
plt.legend(loc='upper right')
plt.axvline(0, color='black', linewidth=0.5)  # Add a vertical line at 0

# Show plot
plt.tight_layout()
plt.savefig(r'C:\Python homedirectory\Portfolio_git\ESS11\reports\figures\age_pyramid_grouped.png')
plt.show()