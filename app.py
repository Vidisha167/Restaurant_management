import streamlit as st
from frontend.customers_page import show_customers_page
from frontend.restaurants_page import show_restaurant_page
from frontend.orders_page import show_orders_page
from frontend.reservations_page import show_reservations_page
from frontend.order_items_page import show_order_items_page
from frontend.tables_page import show_tables_page
from frontend.menu_page import show_menu_page
from frontend.waiter_page import show_waiters_page
from frontend.payment_page import show_payments_page

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
    "Order Item",
    "Payment"
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

with tabs[3]:
    show_orders_page()

with tabs[4]:
    show_reservations_page()

with tabs[5]:
    show_tables_page()

with tabs[6]:
    show_menu_page()

with tabs[7]:
    show_waiters_page()

with tabs[8]:
    show_order_items_page()

with tabs[9]:
    show_payments_page()
