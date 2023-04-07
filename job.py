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
    if date.weekday() == 4:
        return [date.strftime('%A, %d/%m/%Y'), '---']  # Add a row with a horizontal line after Fridays
    else:
        return [date.strftime('%A, %d/%m/%Y'), '']  # Add an empty row after other weekdays

# Apply the date format to the index column
df2_weekdays_formatted = pd.DataFrame(df2_weekdays.index.map(format_date).tolist(), columns=['Date', ''])

# Join the formatted date column with the original dataframe
df2_weekdays_joined = pd.concat([df2_weekdays_formatted, df2_weekdays], axis=1)

# Display the dataframe in Streamlit
st.write(df2_weekdays_joined)
