import streamlit as st
import pandas as pd
import numpy as np
from streamlit_awesome_icons import *

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

# Add a new column called "Icon"
df2_weekdays['Icon'] = np.nan

# Define a function to assign an icon to each week
def assign_icon(row):
    week_num = row.name.week
    if week_num % 4 == 1:
        return IconFamily.SOLID_ARROW_DOWN
    elif week_num % 4 == 2:
        return IconFamily.SOLID_ARROW_UP
    elif week_num % 4 == 3:
        return IconFamily.SOLID_CIRCLE
    else:
        return IconFamily.SOLID_SQUARE

# Apply the function to the "Icon" column
df2_weekdays['Icon'] = df2_weekdays.apply(assign_icon, axis=1)

# Display the dataframe in Streamlit
st.write(df2_weekdays)
