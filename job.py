import streamlit as st
import pandas as pd

# Load the Excel file into a Pandas DataFrame
excel_file = pd.read_excel('https://github.com/SNgere/Allocator/blob/e55257a9658e72e3093c18d212afbee8df88ad2d/job.xlsx', sheet_name=None)

# Get the DataFrame for each sheet
sheet1_df = excel_file['Sheet1']
sheet2_df = excel_file['Sheet2']

# Define the Streamlit app
def app():
    # Add a title to the app
    st.title("Work Allocation")

    # Create a dropdown to select the staff member
    staff_names = sheet1_df['Staff'].tolist()
    selected_staff = st.selectbox("Select Staff Member", staff_names)

    # Create a date input to select the week
    selected_date = st.date_input("Select Week Starting")

    # Get the work allocation for the selected staff member and week
    work_allocation = sheet2_df.loc[(sheet2_df['Date'] == selected_date) & (sheet2_df[selected_staff].notnull())]
    
    # If work allocation is found, display it in a table
    if not work_allocation.empty:
        st.write(f"Work for {selected_staff} in week starting {selected_date}:")
        st.dataframe(work_allocation, index=False)
    # If no work allocation is found, display a message
    else:
        st.write(f"No work found for {selected_staff} in week starting {selected_date}.")
