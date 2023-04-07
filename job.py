import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(
    page_title="Scanning Department",
    page_icon=":memo:",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Define page background color and font
page_bg_color = "#F8F8FF"
font = "sans-serif"

# Define header styles
header_bg_color = "#222831"
header_text_color = "#F8F8FF"
header_font_size = "30px"
header_font_weight = "bold"
header_padding = "1rem"

# Define subheader styles
subheader_bg_color = "#393e46"
subheader_text_color = "#F8F8FF"
subheader_font_size = "20px"
subheader_font_weight = "bold"
subheader_padding = "0.5rem"

# Set page header
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background-color: {page_bg_color};
            font-family: {font};
        }}
        .css-hby737 {{
            padding: 0;
        }}
        .main-header {{
            background-color: {header_bg_color};
            color: {header_text_color};
            font-size: {header_font_size};
            font-weight: {header_font_weight};
            padding: {header_padding};
            margin-bottom: 1rem;
        }}
        .main-subheader {{
            background-color: {subheader_bg_color};
            color: {subheader_text_color};
            font-size: {subheader_font_size};
            font-weight: {subheader_font_weight};
            padding: {subheader_padding};
        }}
    </style>
    
    <div class="main-header">
        <div class="css-hby737"> </div>
        <span>Scanning Department</span>
    </div>
    
    <div class="main-subheader">
        <span>Batches allocated weekly</span>
    </div>
    """,
    unsafe_allow_html=True
)

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

# Display the dataframe in Streamlit
st.write(df2_weekdays)

#################################################################################################################################################################

import pandas as pd
import streamlit as st

# Load the data
df = pd.read_csv("https://raw.githubusercontent.com/SNgere/Allocator/main/job.csv")

# Define the search function
def search_columns(input_str):
    # Iterate over the columns of the DataFrame
    for col in df.columns:
        # If the input string matches the column name, return the column
        if input_str.lower() == col.lower():
            return df[col]
    # If no matching column was found, return an error message
    return "No matching column found."

# Define the Streamlit app
def app():
    # Set the page title
    st.set_page_config(page_title="Column Search")

    # Add a title to the app
    st.title("Column Search")

    # Add a text input field for the user to enter their search string
    search_str = st.text_input("Enter a column name:")

    # If the user has entered a search string, search for the column and display the results
    if search_str:
        result = search_columns(search_str)
        st.write(result)
        
if __name__ == '__main__':
    app()
