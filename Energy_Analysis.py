#!/usr/bin/env python
# coding: utf-8

# #### Analyzing data on the potentials of rooftop solar energy 
# ##### Importing appropriate libraries 
# 
# 

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# #### Loading and exploring dataset

# In[8]:


energy_potential = pd.read_csv("accra_rooftop_solarpotential.csv")
solar_energy_potential = energy_potential.set_index('OBJECTID')
solar_energy_potential


# In[9]:


# Display the first few rows of the dataset
solar_energy_potential.head()


# In[10]:


# Get information about the dataset
solar_energy_potential.info()


# In[11]:


# Generate summary statistics
solar_energy_potential.describe()


# #### Data cleaning

# In[12]:


# Check for missing values
solar_energy_potential.isnull().sum()



# In[13]:


# Handle missing values by filling missing values with zeros:
solar_energy_potential['Peak_installable_capacity'].fillna(0, inplace=True)


# #### Data visualization

# In[14]:


# Scatter plot of Surface Area vs. Energy Potential per Year
plt.figure(figsize=(10, 6))
sns.scatterplot(data=solar_energy_potential, x='Surface_area', y='Energy_potential_per_year', hue='Assumed_building_type')
plt.title('Surface Area vs. Energy Potential per Year')
plt.xlabel('Surface Area')
plt.ylabel('Energy Potential per Year')
plt.grid()

plt.show()



# In[ ]:





# #### Calculating the average energy potential for different building 

# In[17]:


# Calculate average energy potential by building type
average_energy_by_type = solar_energy_potential.groupby('Assumed_building_type')['Energy_potential_per_year'].mean()
average_energy_by_type


# In[ ]:





# In[18]:


# Create a bar plot of average energy potential by building type
plt.figure(figsize=(12, 6))
sns.barplot(x=average_energy_by_type.index, y=average_energy_by_type.values, palette='viridis')
plt.title('Average Energy Potential by Building Type')
plt.xlabel('Building Type')
plt.ylabel('Average Energy Potential per Year')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')

plt.show()



# In[ ]:




