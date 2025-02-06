import streamlit as st

# App title
st.title("Multi-Select Example with Deselect Option")

# List of items to select from
items = ["Apple", "Banana", "Orange", "Grapes", "Mango", "Pineapple"]

# Multi-select widget
selected_items = st.multiselect("Select items:", items)

# Display selected items
if selected_items:
    st.write("You selected:", selected_items)
else:
    st.write("No items selected.")

# Button to clear selection
if st.button("Deselect All"):
    selected_items = []  # Clear selection
    st.experimental_rerun()  # Rerun the script to update UI
