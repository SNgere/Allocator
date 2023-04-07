import streamlit as st
import pandas as pd
import numpy as np

# Load the dataframe from CSV file
df2 = pd.read_csv('https://raw.githubusercontent.com/SNgere/Allocator/main/job.csv')

# Convert 'Date' column to datetime format
df2['Date'] = pd.to_datetime(df2['Date'])

# Set 'Date' column as the index
df2.set_index('Date', inplace=True)

# Filter the dataframe to only show Monday to Friday
df2_weekdays = df2.loc[df2.index.weekday < 5]

# Create a multi-level header for the table
week_nums = df2_weekdays.index.week
weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
header = pd.MultiIndex.from_product([np.unique(week_nums), weekday_names], names=['Week', 'Day'])

# Reshape the dataframe to match the header
df2_weekdays_reshaped = df2_weekdays.pivot(columns=df2_weekdays.index.weekday, values='Value')

# Rename the columns to match the weekday names
df2_weekdays_reshaped.columns = weekday_names

# Add the week number as a new column
df2_weekdays_reshaped['Week'] = week_nums

# Set the index as the week number and reset the dataframe index
df2_weekdays_reshaped.set_index('Week', inplace=True)
df2_weekdays_reshaped.index.name = 'Week'
df2_weekdays_reshaped.reset_index(inplace=True)

# Set the multi-level header for the table
df2_weekdays_reshaped.columns = header

# Display the nested table in Streamlit
st.write(df2_weekdays_reshaped)
