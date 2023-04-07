import streamlit as st
import pandas as pd
import numpy as np

# Load the dataframe from CSV file
df2 = pd.read_csv("https://raw.githubusercontent.com/SNgere/Allocator/main/job.csv")

# Convert 'Date' column to datetime format
df2['Date'] = pd.to_datetime(df2['Date'])

# Set 'Date' column as the index
df2.set_index('Date', inplace=True)

# Filter the dataframe to only show Monday to Friday
df2_weekdays = df2.loc[df2.index.weekday < 5]

# Define a function to color code rows forming one week differently
def highlight_week(row):
    if row.name.week % 2 == 0:
        return ['background-color: #e8f8fc']*len(row)
    else:
        return ['background-color: #f4f4f4']*len(row)

# Apply the function to the dataframe
df2_weekdays_styled = df2_weekdays.style.apply(highlight_week, axis=1)

# Display the styled dataframe in Streamlit
st.write(df2_weekdays_styled)
