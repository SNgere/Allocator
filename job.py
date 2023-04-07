import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title="Weekly Work Allocation", page_icon=":memo:", layout="wide")

# Set page header
st.title("Weekly Work Allocation")
st.markdown("This table shows the weekly work allocation for each team member.")

# Load the data
df = pd.read_csv("https://raw.githubusercontent.com/SNgere/Allocator/main/job.csv")

# Convert the "Date" column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Group the data by week and sum the values in each group
weekly_work = df.groupby(pd.Grouper(key='Date', freq='W-MON')).sum()

# Drop any NaN values in the resulting dataframe
weekly_work = weekly_work.dropna(how='all')

# Define the start and end date for the date range filter
start_date = pd.to_datetime('2023-04-10')
end_date = pd.to_datetime('2023-04-14')

# Filter the data by date range
filtered_work = weekly_work.loc[start_date:end_date]

# Display the resulting dataframe with formatting
st.write(filtered_work.style
    .set_caption("Work allocation from April 10th to April 14th")
    .format("{:.0f}")
    .set_properties(**{'text-align': 'center'})
    .set_table_styles([{'selector': 'th', 'props': [('font-size', '120%')]}]) # increase table size
    .set_properties(subset=['Date'], **{'width': '120px'}) # remove time component from date column
    .set_properties(subset=['Date'], **{'text-align': 'center'})) # center align date column
