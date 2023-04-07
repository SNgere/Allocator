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

# Set page title and favicon
st.set_page_config(page_title="Weekly Work Allocation", page_icon=":memo:", layout="wide")

# Set page header
st.title("Weekly Work Allocation")
st.markdown("Batches allocated weekly.")

# Set page background color
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: #f5f5f5;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Set table styles
styles = [
    dict(selector="th", props=[("font-size", "16pt"), ("text-align", "center"), ("border", "1px solid #ccc"), ("padding", "8px")]),
    dict(selector="td", props=[("font-size", "14pt"), ("text-align", "center"), ("border", "1px solid #ccc"), ("padding", "8px")]),
    dict(selector="caption", props=[("caption-side", "top"), ("font-size", "20pt"), ("padding-top", "16px"), ("margin-bottom", "32px")]),
]

# Define a function to highlight Fridays in maroon color
def highlight_fridays(row):
    if row.name.weekday() == 4:
        return ['background-color: #800000']*len(row)
    else:
        return ['']*len(row)

# Apply the highlight function to the dataframe
df2_weekdays_styled = df2_weekdays.style.apply(highlight_fridays, axis=1).set_table_styles(styles)

# Display the styled dataframe in Streamlit
st.write(df2_weekdays_styled)
