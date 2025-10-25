import streamlit as st
from frontend.customers_page import show_customers_page
from frontend.restaurants_page import show_restaurant_page
# from frontend.reservations_page import show_reservations_page

st.set_page_config(page_title="Restaurant Management System", layout="wide")

st.title("Restaurant Management System")

# --- Tabs ---
tab_names = [
    "Home", 
    "Customers", 
    "Restaurants", 
    "Orders", 
    "Reservations", 
    "Tables", 
    "Menu", 
    "Waiter", 
    "Order Item"
]

tabs = st.tabs(tab_names)


with tabs[0]:
    st.header("Welcome to the Restaurant Management System")
    st.write("""
    This system helps you manage your restaurant operations efficiently.
    Use the tabs above to navigate between Customers, Orders, Reservations, and more.
    """)

with tabs[1]:
    show_customers_page()

with tabs[2]:
    show_restaurant_page()
