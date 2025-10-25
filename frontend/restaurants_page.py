import streamlit as st
from backend.restaurant import get_restaurant, add_restaurant, update_restaurant, delete_restaurant

def show_restaurant_page():
    st.header("Restaurants")

    # Show all restaurants
    restaurants = get_restaurant()
    st.table(restaurants)

    # --- Add Restaurant ---
    with st.expander("Add New Restaurant", expanded=False):
        with st.form("add_restaurant_form"):
            contact_number = st.text_input("Contact Number")
            location = st.text_input("Location")
            submitted = st.form_submit_button("Add Restaurant")
            if submitted:
                add_restaurant(contact_number, location)
                st.success("Restaurant added!")

    # --- Delete Restaurant ---
    with st.expander("Delete Restaurant"):
        with st.form("delete_restaurant_form"):
            restaurant_id = st.number_input("Restaurant ID to Delete", min_value=1, step=1)
            submitted = st.form_submit_button("Delete Restaurant")
            if submitted:
                delete_restaurant(restaurant_id)
                st.success("Restaurant deleted!")

    # --- Update Restaurant ---
    with st.expander("Update Restaurant"):
        with st.form("update_restaurant_form"):
            restaurant_id = st.number_input("Restaurant ID to Update", min_value=1, step=1)
            contact_number = st.text_input("Contact Number")
            location = st.text_input("Location")
            submitted = st.form_submit_button("Update Restaurant")
            if submitted:
                update_restaurant(
                    restaurant_id,
                    contact_number if contact_number else None,
                    location if location else None
                )
                st.success("Restaurant updated!")
