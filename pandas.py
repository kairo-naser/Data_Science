# pandas is a powerful library for data manipulation and analysis in Python[cite: 293].
import pandas as pd # [cite: 294]
import numpy as np # [cite: 295]

# --- 1. THE SERIES DATA STRUCTURE ---
# A Series is a one-dimensional object similar to an array, list, or column[cite: 306].
# Each item is assigned to an entry in an index[cite: 307].
s1 = pd.Series(np.random.rand(4), index=['a', 'b', 'c', 'd']) # [cite: 308]

# If no index is passed, Pandas creates one from 0 to N-1 by default[cite: 317].
s2 = pd.Series(np.random.rand(4)) # [cite: 318]

# You can access or modify values using the index[cite: 326, 329].
value_c = s1['c'] # [cite: 327]
s1['c'] = 3.14 # [cite: 329]

# --- 2. THE DATAFRAME DATA STRUCTURE ---
# A DataFrame is a tabular structure with ordered columns and rows[cite: 347].
# It can be viewed as a group of Series objects sharing an index[cite: 348].

# Initialize from a dictionary of lists[cite: 350].
data = {
    'Year': [2000, 2005, 2010, 2014],
    'Median_Age': [24.2, 26.4, 28.5, 30.3],
    'Density': [244, 256, 268, 279]
}
# By default, columns are ordered alphabetically[cite: 352].
# Use the 'columns' attribute to set a specific order[cite: 353].
df2 = pd.DataFrame(data, columns=['Year', 'Density', 'Median_Age']) # [cite: 353]

# --- 3. LOADING DATA FROM FILES ---
# read_csv is used to load data from text files[cite: 356].
# The 'sep' parameter allows you to change the delimiter (comma by default)[cite: 357, 360].
# Other parameters include 'dtype' (data type), 'header', and 'skiprows'[cite: 361, 362, 363].
# df4 = pd.read_csv('person.csv') # [cite: 359]

# --- 4. INSPECTING DATA ---
# Use head() and tail() to inspect small samples of large datasets[cite: 366].
# By default, they return five elements, but you can set a custom number[cite: 367].
s7 = pd.Series(np.random.rand(10000)) # [cite: 368]
print(s7.head())      # Displays first 5 [cite: 368]
print(s7.tail(3))     # Displays last 3 [cite: 369]

# --- 5. FUNCTIONAL STATISTICS ---
# summarize data using methods like sum() or mean()[cite: 371, 372].
df5 = pd.DataFrame(np.arange(9).reshape(3,3), columns=['a','b','c']) # [cite: 373]
total_sum = df5.sum() # [cite: 374]

# skipna (True by default) decides whether to exclude missing data[cite: 377, 378].
# describe() summarizes most statistical info (count, mean, std, etc.)[cite: 379, 380].
print(df5.describe()) # [cite: 380]

# --- 6. SORTING ---
# sort_index() sorts by row or column index[cite: 383].
# Use 'axis=1' for columns and 'ascending=False' for descending order[cite: 384, 385].
df7 = pd.DataFrame(np.arange(12).reshape(3,4), columns=['b', 'd', 'a', 'c'], index=['x', 'y', 'z']) # [cite: 387]
sorted_df = df7.sort_index(axis=1) # [cite: 388]

# --- 7. HANDLING MISSING DATA ---

# First, we must create the DataFrame 'df9' mentioned in the text 
# It contains 'NaN' (Not a Number) values to represent missing data[cite: 192].
data_missing = {
    'a': [0, 3, 6, 9],
    'b': [1, 4, 7, 10],
    'c': [2, 5, 8, 11],
    'd': [np.nan, np.nan, np.nan, np.nan] # This column is all missing values 
}
df9 = pd.DataFrame(data_missing)

# Now the code can be active:

# Detect missing (NaN/null) values using isnull().
# This returns True for every missing value found.
print(df9.isnull()) 

# dropna() is used to remove null data[cite: 196].
# By default, it drops any row containing a missing value[cite: 196].
# Using axis=1 tells it to drop columns with missing values instead[cite: 197].
clean_df = df9.dropna(axis=1) 
print(clean_df)

# fillna() allows you to fill missing values with a custom value.
# In this example, we replace all NaN values with -1.
filled_df = df9.fillna(-1) 
print(filled_df)