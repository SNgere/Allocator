
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
    st.write("Enter a valid number to search.")

#####################################################################################################################################
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/SNgere/Allocator/main/cell_counts.csv')

# Set up plot style
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(5, 5), facecolor='#f2f2f2')

# Create a pie chart with custom colors and explode
colors = ['#ff6666', '#66b3ff']
explode = (0.1, 0)
wedges, texts, autotexts = ax.pie(df['Count'], labels=df['Color'], autopct='%1.1f%%', startangle=90,
       colors=colors, explode=explode, shadow=True, textprops=dict(color="w"))

# Add arrows inside the pie chart
center_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(center_circle)

for i, wedge in enumerate(wedges):
    ang = (wedge.theta2 - wedge.theta1)/2. + wedge.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = f"angle,angleA=0,angleB={ang}"
    ax.annotate(f"{df['Count'][i]}", xy=(x, y), xytext=(1.2*np.sign(x), 1.2*y),
            horizontalalignment=horizontalalignment, fontsize=10, fontweight='bold',
            xycoords=ax.transData, textcoords=ax.transData,
            arrowprops=dict(arrowstyle="->", color='white', lw=1.5, connectionstyle=connectionstyle))

ax.axis('equal')
ax.set_title('Cell Counts by Fill Color', fontweight='bold', fontsize=16)

# Show the pie chart in Streamlit
st.pyplot(fig)




