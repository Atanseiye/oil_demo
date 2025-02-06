import streamlit as st
import pandas as pd
from processes import feature_engineer
from components import plot_3

# App title
st.title("Multi-Select Example with Deselect Option")

uploaded_file = st.file_uploader("Choose files", type=["xlsx"])
if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)
    # Use the Feature Engineering function here and save it to the data variable
    data = feature_engineer(data)
    # write the head of the data to the front-end
    st.write(data.head())
    # List of items to select from
    items = data.columns
    # Multi-select widget 
    selected_items = st.multiselect("Select items:", items)

    # Display selected itemsd
    if selected_items:
        st.write(data[selected_items])
        if len(selected_items) == 3:
            plot_3(data, selected_items)
        else:
            st.warning('Please, reduce the selected features to 3. \n This software cannot process more than three features at a time now.')
    else:
        st.write("No items selected.")

else:
    pass







# Button to clear selection
if st.button("Deselect All"):
    selected_items = []  # Clear selection
    st.experimental_rerun()  # Rerun the script to update UI
