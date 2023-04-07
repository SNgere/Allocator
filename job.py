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

# Define a function to format the date as "Monday, DD/MM/YYYY" and highlight every Friday in maroon
def format_date_and_highlight_fridays(date):
    if date.weekday() == 4:
        return [f'background-color: #800000; color: white'] * len(date)
    return [''] * len(date)

df2_weekdays_styled = df2_weekdays.style.apply(format_date_and_highlight_fridays, axis=1)

# Apply the date format to the index column
df2_weekdays_styled.set_caption('Weekly Data')
df2_weekdays_styled.set_table_styles(
    [{
        'selector': 'caption',
        'props': [('color', '#008080'),
                  ('font-size', '18px'),
                  ('text-align', 'center'),
                  ('font-weight', 'bold'),
                  ('padding-top', '12px'),
                  ('padding-bottom', '12px')]
    }]
)

# Display the styled dataframe in Streamlit
st.write(df2_weekdays_styled)
