import streamlit as st
from backend.customers import get_customers, add_customer,delete_customer,update_customer

def show_customers_page():
    st.header("Customers")

    #show customers
    customers = get_customers()
    st.table(customers)
    #add customers
    with st.expander("Add New Customer", expanded=False):  # starts collapsed
        with st.form("add_customer_form"):
            name = st.text_input("Name")
            phone = st.text_input("Phone")
            email = st.text_input("Email")
            submitted = st.form_submit_button("Add Customer")
            if submitted:
                add_customer(name, phone, email)
                st.success("Customer added!")
    #delete customers
    with st.expander("Delete Customer"):
        with st.form("delete_customer_form"):
            customer_id = st.number_input("Customer ID to Delete", min_value=1, step=1)
            submitted = st.form_submit_button("Delete Customer")
            if submitted:
                delete_customer(customer_id)
                st.success("Customer deleted!")
    #update customers
    with st.expander("Update Customer"):
        with st.form("update_customer_form"):
            customer_id = st.number_input("Customer ID to Update", min_value=1, step=1)
            name = st.text_input("New Name (leave blank if no change)")
            phone = st.text_input("New Phone (leave blank if no change)")
            email = st.text_input("New Email (leave blank if no change)")
            submitted = st.form_submit_button("Update Customer")
            if submitted:
                update_customer(customer_id, name if name else None, phone if phone else None, email if email else None)
                st.success("Customer updated!")



