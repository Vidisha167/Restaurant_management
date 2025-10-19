import streamlit as st
import pandas as pd
from db_config import get_connection

# --- Connect to database ---
conn = get_connection()
cursor = conn.cursor(dictionary=True)

st.title("Restaurant Management System")

tab1, tab2, tab3, tab4 = st.tabs(["Customers", "Restaurants", "Orders", "Reservations"])

with tab1:
    st.header("Customers")
    cursor.execute("SELECT * FROM customer")
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    st.dataframe(df)
