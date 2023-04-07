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

# Define a function to format the date as "Monday, DD/MM/YYYY"
def format_date(date):
    return date.strftime('%A, %d/%m/%Y')

# Apply the date format to the index column
df2_weekdays.index = df2_weekdays.index.map(format_date)

# Add a horizontal line after every Friday
def add_weekly_separator(index, column):
    if index.weekday() == 4:
        return 'border-bottom: 2px solid #ccc'
    else:
        return ''

df2_weekdays_styled = df2_weekdays.style.applymap(add_weekly_separator)

# Display the styled dataframe in Streamlit
st.write(df2_weekdays_styled)
