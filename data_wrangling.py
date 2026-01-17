# data_wrangling.py
# Data wrangling (or munging) is the process of cleaning and transforming raw data

import pandas as pd
import numpy as np

# --- 1. DATA CLEANING: RENAMING & TYPE CONVERSION ---
# Data wrangling is the process of cleaning and unifying messy data for analysis.
# Initial cleaning often involves renaming columns and fixing data types.

# Sample data setup
df = pd.DataFrame({
    'date': ['2018-10-11', '2018-10-12', '2018-10-13'],
    'temp_C': [20.5, 21.2, 19.8],
    'station': ['GHCND', 'GHCND', 'GHCND'],
    'datatype': ['TMIN', 'TMAX', 'TMIN']
})

# rename() is used to give columns easy-to-reference names.
df = df.rename(columns={'temp_C': 'temp_Celsius'})

# astype() converts columns to better formats, like integers or categories.
# Categorical variables are used when a column has a few distinct values.
df = df.assign(
    date=pd.to_datetime(df.date), # Convert string to datetime objects
    temp_int=df.temp_Celsius.astype('int'), # Chop off decimals
    station=df.station.astype('category') # Save memory with categories
)

# --- 2. DATA TRANSFORMATION: ADDING NEW COLUMNS ---
# Transformation occurs after initial cleaning.
# assign() allows you to create new columns, like converting Celsius to Fahrenheit.
df = df.assign(temp_F=(df.temp_Celsius * 9/5) + 32)

# --- 3. REORDERING AND SORTING ---
# We often need to sort by values to find extremes, like the hottest days.
# sort_values() sorts by one or more columns.
# Use 'ascending=False' for descending order.
sorted_df = df.sort_values(by='temp_F', ascending=False)

# sort_index() sorts the dataframe by its row or column labels.
# You must pass 'inplace=True' to update the original dataframe directly.
df.sort_index(axis=1, inplace=True) # Sort columns alphabetically

# --- 4. RE-INDEXING & DATETIME SLICING ---
# set_index() moves a column to the index position, replacing numeric indices.
df.set_index('date', inplace=True)

# Setting a datetime index allows for powerful date-based slicing.
# For example, selecting a specific date range.
october_data = df['2018-10-11':'2018-10-12']

# --- 5. SUMMARY STATISTICS FOR CATEGORIES ---
# describe() for categories shows unique values, the mode (top), and frequency.
print(df.describe(include='category'))