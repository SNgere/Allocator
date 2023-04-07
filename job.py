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
def add_horizontal_line(row):
    line = 'border-bottom: 1px solid black'
    if row.name.endswith('Friday'):
        return [line]*len(row)
    else:
        return ['']*len(row)

# Apply the horizontal line to the dataframe
df2_weekdays_styled = df2_weekdays.style.apply(add_horizontal_line, axis=1)

# Display the styled dataframe in Streamlit
st.write(df2_weekdays_styled)
