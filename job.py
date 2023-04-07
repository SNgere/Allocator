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

# Define a function to format the date as "Monday, DD/MM/YYYY" and color every Friday in maroon
def format_date_and_color_friday(date):
    if date.weekday() == 4:  # Friday
        return ['background-color: maroon; color: white']*len(date), date.strftime('%A, %d/%m/%Y')
    else:
        return ['']*len(date), date.strftime('%A, %d/%m/%Y')

# Apply the date format and color to the index column
df2_weekdays_styled = df2_weekdays.style.apply(lambda x: format_date_and_color_friday(x.index))

# Display the styled dataframe in Streamlit
st.write(df2_weekdays_styled)
