import streamlit as st
import pandas as pd

# Load the dataframe from CSV file
df2 = pd.read_csv("https://raw.githubusercontent.com/SNgere/Allocator/main/job.csv")

# Convert 'Date' column to datetime format
df2['Date'] = pd.to_datetime(df2['Date'])

# Set 'Date' column as the index
df2.set_index('Date', inplace=True)

# Filter the dataframe to only show Monday to Friday
df2_weekdays = df2.loc[df2.index.weekday < 5]

# Display the dataframe in Streamlit
st.dataframe(df2_weekdays)
