import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
        <span>Completed vs Outstanding Tasks     
        </span>
    </div>
    """,
    unsafe_allow_html=True
)



# Read the CSV file into a pandas DataFrame
df3 = pd.read_csv('https://raw.githubusercontent.com/SNgere/Allocator/main/cell_counts.csv')

# Set up plot style
plt.style.use('default')

# Create a pie chart with custom colors and explode
colors = ['#008000', '#66b3ff']
explode = (0.02, 0)
fig, ax = plt.subplots(figsize=(8, 4))
wedges, labels = ax.pie(df3['Count'], labels=df3['Color'], startangle=120,
       colors=colors, explode=explode, shadow=False)

ax.axis('equal')
#ax.set_title('Progress', fontweight='bold')

# Add the values inside the pies
for i, wedge in enumerate(wedges):
    # Calculate the angle at the middle of the wedge
    ang = (wedge.theta2 - wedge.theta1)/2. + wedge.theta1
    # Convert the angle to radians
    ang = ang*np.pi/180.
    # Calculate the position of the text label
    y = np.sin(ang)*wedge.r*0.8
    x = np.cos(ang)*wedge.r*0.8
    # Place the text label at the calculated position
    ax.text(x, y, str(df3['Count'][i]), ha='center', va='center', fontweight='bold', fontsize=12)

# Show the pie chart in Streamlit
st.pyplot(fig)

st.header('Batches allocated weekly')

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
import matplotlib.pyplot as plt
import streamlit as st

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/SNgere/Allocator/main/job.csv')

# Drop the 'Date' column
df = df.drop('Date', axis=1)

# Convert numeric columns to string type
df = df.astype(str)

# Calculate the ratio of cells with * to those without for each column
ratios = df.apply(lambda x: x.str.contains('\*').value_counts(normalize=True).get(True, 0)) * 10

# Sort the ratios in descending order
ratios = ratios.sort_values(ascending=True)

# Create a horizontal bar chart using matplotlib and display it in the Streamlit app
fig, ax = plt.subplots()
ratios.plot(kind='barh', ax=ax, color='tab:blue')
ax.set_xlim([0, 10])
ax.set_xticks(range(0, 11, 1))
plt.xlabel('Batches completed out of those allocated')

# Add vertical lines to show where the bars are on the scale
for x in range(11):
    ax.axvline(x=x, color='gray', alpha=0.1)

# Add sad emoji if the bar is less than or equal to 5
for i, v in enumerate(ratios):
    if v < 1:
        ax.text(v + 0.2, i, u'\U0001F622', fontsize=16, color='red') # \U0001F622

# Display the chart in the Streamlit app
st.pyplot(fig)


##########################################################################################################################################################

import pandas as pd
import streamlit as st

# Load the data
df = pd.read_csv("https://raw.githubusercontent.com/SNgere/Allocator/main/job.csv")

# Add a text input widget to allow the user to search
search_term = st.text_input("Search")

# Convert the search term to a numeric type
try:
    search_num = int(search_term)
except ValueError:
    try:
        search_num = float(search_term)
    except ValueError:
        search_num = None

# Check if the search term matches any column
if search_num is not None:
    match_found = False
    for col in df.columns:
        if df[col].dtype in ['int64', 'float64'] and col != 'date':
            if search_num in df[col].values:
                st.write(f"{search_num} was assigned to '{col}'.")
                match_found = True
    if not match_found:
        st.write(f"No match found for {search_num}.")
else:
    st.write("Enter Batch No.")

#####################################################################################################################################

