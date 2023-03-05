#!/usr/bin/env python
# coding: utf-8

# In[7]:


import os
import pandas as pd

folder_name = 'data' # Replace with the name of your folder
data_path = os.path.join(os.getcwd(), folder_name) # Get the absolute path of the folder

# Create a list of file paths in the folder
file_paths = [os.path.join(data_path, file) for file in os.listdir(data_path) if file.endswith('.csv')]

# Initialize an empty list to store the DataFrames
dfs = []

# Loop through each file and read it into a DataFrame
for file_path in file_paths:
    df = pd.read_csv(file_path)
    dfs.append(df)

# Get a list of column names that are common to all DataFrames
common_cols = set.intersection(*[set(df.columns) for df in dfs])

# Loop through each DataFrame and keep only the common columns
for i, df in enumerate(dfs):
    dfs[i] = df[list(common_cols)]

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dfs)

# Drop rows with null values
combined_df.dropna(inplace=True)

# Display the first few rows of the combined DataFrame
combined_df.head()


# In[9]:


import os
import pandas as pd

# Define the folder name
folder_name = 'data'

# Get the absolute path of the folder
data_path = os.path.join(os.getcwd(), folder_name)

# Create a list of file paths in the folder
file_paths = [os.path.join(data_path, file) for file in os.listdir(data_path) if file.endswith('.csv')]

# Initialize an empty list to store the DataFrames
dfs = []

# Iterate over the file paths and read each CSV into a DataFrame
for file_path in file_paths:
    df = pd.read_csv(file_path, usecols=['PERWT09F', 'VARSTR', 'VARPSU', 'PID', 'DUID', 'PANEL', 'DUPERSID'])
    dfs.append(df)

# Merge the DataFrames based on the specified columns
merged_df = pd.concat(dfs, ignore_index=True).dropna()

# Print the merged DataFrame
print(merged_df)


# In[11]:


import os
import pandas as pd

# Set the name of the data folder
folder_name = 'data'

# Get the absolute path of the folder
data_path = os.path.join(os.getcwd(), folder_name)

# Create a list of file paths in the folder
file_paths = [os.path.join(data_path, file) for file in os.listdir(data_path) if file.endswith('.csv')]

# Initialize an empty list to store the DataFrames
dfs = []

# Read each file into a DataFrame and append it to the list
for file in file_paths:
    df = pd.read_csv(file, low_memory=False)
    dfs.append(df)

# Merge the DataFrames based on the specified columns
merged_df = pd.concat(dfs, axis=0, ignore_index=True, sort=False)
merged_df = merged_df.groupby(['PERWT09F', 'VARSTR', 'VARPSU', 'PID', 'DUID', 'PANEL', 'DUPERSID']).first().reset_index()

# Save the merged DataFrame to a CSV file
merged_df.to_csv('merged_data.csv', index=False)


# In[12]:


import os
import pandas as pd

folder_name = 'data'

# Get the absolute path of the folder
data_path = os.path.join(os.getcwd(), folder_name)

# Create a list of file paths in the folder
file_paths = [os.path.join(data_path, file) for file in os.listdir(data_path) if file.endswith('.csv')]

# Create an empty dictionary to store the column names and value counts
column_dict = {}

# Loop through the files
for file in file_paths:
    # Read the file into a DataFrame
    df = pd.read_csv(file)
    # Get the column names and value counts
    column_names = df.columns.tolist()
    value_counts = df.count().tolist()
    # Add the column names and value counts to the dictionary
    for i in range(len(column_names)):
        if column_names[i] not in column_dict:
            column_dict[column_names[i]] = value_counts[i]
        else:
            column_dict[column_names[i]] += value_counts[i]

# Sort the dictionary by value counts
sorted_columns = sorted(column_dict.items(), key=lambda x: x[1], reverse=True)

# Print the column names and value counts
for column, count in sorted_columns:
    print(f"{column}: {count}")


# In[13]:


print(merged_df)


# In[14]:


merged_df.describe()


# In[ ]:




