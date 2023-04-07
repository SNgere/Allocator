# Load the dataframe from CSV file
df2 = pd.read_csv('"https://raw.githubusercontent.com/SNgere/Allocator/main/job.csv"')

# Convert 'Date' column to datetime format
df2['Date'] = pd.to_datetime(df2['Date'])

# Set 'Date' column as the index
df2.set_index('Date', inplace=True)

# Filter the dataframe to only show Monday to Friday
df2_weekdays = df2.loc[df2.index.weekday < 5]

# Define a function to color code rows forming one week differently
def highlight_week(row):
    week_num = row.name.week
    week_odd = week_num % 2 == 1
    if (week_num == 15 or week_num == 16) and row.name.day < 14:
        return ['background-color: #e0e0e0']*len(row)  # Change color for April 10-14, 2023
    elif week_odd:
        return ['background-color: #f0f4c3']*len(row)  # Light yellow for odd weeks
    else:
        return ['background-color: #c2e6c9']*len(row)  # Light green for even weeks

# Apply the function to the dataframe
df2_weekdays_styled = df2_weekdays.style.apply(highlight_week, axis=1)

# Set the date format to YYYY-MM-DD
df2_weekdays_styled.format({'Date': '{:%Y-%m-%d}'})

# Display the styled dataframe in Streamlit
st.write(df2_weekdays_styled)
