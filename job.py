import streamlit as st
import pandas as pd

# Load the CSV files into Pandas DataFrames
staff_df = pd.read_csv('https://github.com/SNgere/Allocator/blob/3129b1761d8c113ac7a4fe941bd45356ad64c972/staff.csv')
work_df = pd.read_csv('https://github.com/SNgere/Allocator/blob/3129b1761d8c113ac7a4fe941bd45356ad64c972/job.csv')

# Define the Streamlit app
def app():
    # Add a title to the app
    st.title("Work Allocation")

    # Create a dropdown to select the staff member
    staff_names = staff_df['Staff'].tolist()
    selected_staff = st.selectbox("Select Staff Member", staff_names)

    # Create a date input to select the week
    selected_date = st.date_input("Select Week Starting")

    # Get the work allocation for the selected staff member and week
    work_allocation = work_df.loc[(work_df['Date'] == selected_date) & (work_df[selected_staff].notnull())]
    
    # If work allocation is found, display it in a table
    if not work_allocation.empty:
        st.write(f"Work for {selected_staff} in week starting {selected_date}:")
        st.dataframe(work_allocation, index=False)
    # If no work allocation is found, display a message
    else:
        st.write(f"No work found for {selected_staff} in week starting {selected_date}.")
