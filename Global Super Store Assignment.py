#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the dataset
url = "https://docs.google.com/spreadsheets/d/1Ez8RhO1rE2QikfdddOZ19eEZhN4r6eW7WHb9qB05T7E/export?format=csv"
df = pd.read_csv(url)

# Display basic information
df.info()

# Check for missing values
missing_data = df.isnull().sum()

# Drop duplicates if any
df.drop_duplicates(inplace=True)

# Handle missing values (either drop or fill, depending on the importance of the column)
df.fillna(method='ffill', inplace=True)  # This fills missing data forward






# In[2]:


import matplotlib.pyplot as plt
import seaborn as sns

# Sales by Country
plt.figure(figsize=(10,6))
sns.barplot(x='Country', y='Sales', data=df)
plt.xticks(rotation=90)
plt.title('Sales by Country')
plt.show()

# Sales by Region
plt.figure(figsize=(10,6))
sns.barplot(x='Region', y='Sales', data=df)
plt.title('Sales by Region')
plt.show()

# Sales by Market
plt.figure(figsize=(10,6))
sns.barplot(x='Market', y='Sales', data=df)
plt.title('Sales by Market')
plt.show()


# In[3]:


# Plot percentage of shipping by ship mode
ship_mode_percentage = df['Ship Mode'].value_counts(normalize=True) * 100

plt.figure(figsize=(8,5))
ship_mode_percentage.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2'))
plt.title('Percentage of Shipping by Ship Mode')
plt.ylabel('')
plt.show()


# In[4]:


# Sales by City
plt.figure(figsize=(10,6))
sns.barplot(x='City', y='Sales', data=df.head(20))  # Showing top 20 cities
plt.xticks(rotation=90)
plt.title('Sales by City')
plt.show()

# Sales by State
plt.figure(figsize=(10,6))
sns.barplot(x='State', y='Sales', data=df)
plt.xticks(rotation=90)
plt.title('Sales by State')
plt.show()

# You can repeat this for Region and Market similarly as done for State and City


# In[6]:


# Example table for Sales by Region
sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
print(sales_by_region)


# In[ ]:




