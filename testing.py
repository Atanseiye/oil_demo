import streamlit as st
import pandas as pd
from processes import feature_engineer

# App title
st.title("Multi-Select Example with Deselect Option")

uploaded_file = st.file_uploader("Choose files", type=["xlsx"])
if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)
    # List of items to select from
    st.write(feature_engineer(data).head())
    items = data.columns
    # Multi-select widget
    selected_items = st.multiselect("Select items:", items)
    st.write(f'---> {type(selected_items)}')

    # Display selected items
    if selected_items:
        st.write("You selected:", selected_items)
    else:
        st.write("No items selected.")

else:
    pass







# Button to clear selection
if st.button("Deselect All"):
    selected_items = []  # Clear selection
    st.experimental_rerun()  # Rerun the script to update UI
