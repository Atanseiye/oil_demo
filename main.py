import streamlit as st
from views import load_file_from_db, csv_to_sqlite
import pandas as pd
from processes import feature_engineer
import os

uploaded_file = st.file_uploader("Choose files", type=["csv", "xlsx"])

if uploaded_file is not None:
    file_name = uploaded_file.name
    if file_name.endswith('.csv'):
        data = pd.read_csv(uploaded_file)
        csv_to_sqlite(data)
    if file_name.endswith('.xlsx'):
        data = pd.read_excel(uploaded_file)
        csv_to_sqlite(data)
