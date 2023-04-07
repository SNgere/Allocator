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

# Define the color map for each name
cmap = {'Alice': 'lightblue', 'Bob': 'lightgreen', 'Charlie': 'lightpink', 'Dave': 'lavender', 'Eve': 'lightyellow'}

# Apply background gradient to each name based on its color map
styled_table = filtered_work.style.background_gradient(subset=pd.IndexSlice[:, 'Alice'], cmap=cmap['Alice']).\
              background_gradient(subset=pd.IndexSlice[:, 'Bob'], cmap=cmap['Bob']).\
              background_gradient(subset=pd.IndexSlice[:, 'Charlie'], cmap=cmap['Charlie']).\
              background_gradient(subset=pd.IndexSlice[:, 'Dave'], cmap=cmap['Dave']).\
              background_gradient(subset=pd.IndexSlice[:, 'Eve'], cmap=cmap['Eve'])

# Display the resulting dataframe with formatting and color map
st.write(styled_table.set_caption("Work allocation from April 10th to April 14th").\
          format("{:.0f}").set_properties(**{'text-align': 'center'}))
