import streamlit as st
import pandas as pd

# Load the data
df = pd.read_csv("https://github.com/SNgere/Allocator/blob/ae2a35c1e76639b22d02c62f734c79c35f76f86d/job.csv")

# Convert the "Date" column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Group the data by week and sum the values in each group
weekly_work = df.groupby(pd.Grouper(key='Date', freq='W-MON')).sum()

# Drop any NaN values in the resulting dataframe
weekly_work = weekly_work.dropna(how='all')

# Define the start and end date for the date range filter
start_date = pd.to_datetime('2023-04-10')
end_date = pd.to_datetime('2023-04-14')

# Filter the data by date range
filtered_work = weekly_work.loc[start_date:end_date]

# Display the resulting dataframe
st.write(filtered_work)
