import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\Python homedirectory\Portfolio_git\Oefeningen\customer_satisfaction\E-commerce_NPA_Dataset.csv", index_col=0)
print(df.info())

#determine which driver of satisfaction has most signficant impact
sf = df.iloc[:,4:8]
sf_desc = sf.describe()

# Boxplots for showing distribution drivers
plt.figure(figsize=(20, 5))  # Adjusted the size for 4 plots
plt.subplot(1, 4, 1)  # Changed layout to 1 row, 4 columns
sns.boxplot(y=sf['ProductQualityRating'])
plt.title('Boxplot of Product Quality Rating')

plt.subplot(1, 4, 2)  # Changed the index to 4 columns layout
sns.boxplot(y=sf['DeliveryTimeRating'])
plt.title('Boxplot of Delivery Time Rating')

plt.subplot(1, 4, 3)
sns.boxplot(y=sf['CustomerServiceRating'])
plt.title('Boxplot of Customer Service Rating')

plt.subplot(1, 4, 4)  # Changed the index to 4 columns layout
sns.boxplot(y=sf['WebsiteEaseOfUseRating'])
plt.title('Boxplot of Website Ease of Use Rating')  # Corrected title typo

plt.tight_layout()
plt.show()
