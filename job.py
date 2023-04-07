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
#df2_weekdays = df2.loc[df2.index.weekday < 5]

# Define a function to color code consecutive rows forming two weeks differently
def highlight_2weeks(row):
    week_num = row.name.week
    week_odd = week_num % 2 == 1
    if (week_num == 15 or week_num == 16) and row.name.day < 14:
        return ['background-color: #800020']*len(row)  # Change color for April 10-14, 2023
    elif (week_num % 4 == 0) and row.name.weekday() < 5:
        return ['background-color: #DC143C']*len(row)  # Light green for first week
    elif (week_num % 4 == 1 or week_num % 4 == 2) and row.name.weekday() < 5:
        return ['background-color: #C04000']*len(row)  # Light yellow for second week
    else:
        return ['background-color: #722f37']*len(row)  # White for other weeks

# Apply the function to the dataframe
df2_weekdays_styled = df2_weekdays.style.apply(highlight_2weeks, axis=1)

# Set the date format to YYYY-MM-DD
df2_weekdays_styled.format({'Date': '{:%Y-%m-%d}'})

# Display the styled dataframe in Streamlit
st.write(df2_weekdays_styled)

