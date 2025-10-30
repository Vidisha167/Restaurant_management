import streamlit as st
from backend.waiter import get_waiters, add_waiter, update_waiter, delete_waiter

def show_waiters_page():
    st.header("Waiters")
    st.dataframe(get_waiters(), use_container_width=True)

    with st.expander("Add Waiter"):
        with st.form(key="waiters_add_form"):
            name = st.text_input("Name")
            phone = st.text_input("Phone (optional)")
            shift = st.text_input("Shift (optional)")
            rid=st.number_input("Restaurant_ID (optional)")
            if st.form_submit_button("Add"):
                add_waiter( name, phone, shift, rid)
                st.success("Added!")
                st.rerun()

    with st.expander("Update Waiter"):
        with st.form(key="waiters_update_form"):
            waiter_id = st.number_input("Waiter_ID to update", min_value=1, step=1)
            name = st.text_input("New Name (blank=skip)")
            phone = st.text_input("New Phone (blank=skip)")
            shift = st.text_input("New Shift (blank=skip)")
            restaurant_id = st.text_input("New Restaurant_ID (blank=skip)")
            if st.form_submit_button("Update"):
                rid = int(restaurant_id) if restaurant_id.strip() else None
                update_waiter(waiter_id, name or None, phone or None, shift or None, rid)
                st.success("Updated!")
                st.rerun()

    with st.expander("Delete Waiter"):
        with st.form(key="waiters_delete_form"):
            waiter_id = st.number_input("Waiter_ID to delete", min_value=1, step=1)
            if st.form_submit_button("Delete"):
                delete_waiter(waiter_id)
                st.success("Deleted!")
                st.rerun()