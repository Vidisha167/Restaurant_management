import streamlit as st
from backend.tables import get_tables, add_table, update_table, delete_table

def show_tables_page():
    st.header("Tables")
    st.dataframe(get_tables(), use_container_width=True)

    with st.expander("Add Table"):
        with st.form(key="dining_tables_add_form"):
            capacity = st.number_input("Capacity", min_value=1, step=1)
            status = st.selectbox("Status", ["Available", "Reserved"])
            restaurant_id = st.text_input("Restaurant_ID")
            if st.form_submit_button("Add"):
                rid = int(restaurant_id) if restaurant_id.strip() else None
                add_table(capacity, status, rid)
                st.success("Added!")
                st.rerun()

    with st.expander("Update Table"):
        with st.form(key="dining_tables_update_form"):
            table_id = st.number_input("Table_ID to update", min_value=1, step=1)
            capacity = st.text_input("New Capacity (blank=skip)")
            status = st.selectbox("New Status (optional)", ["", "Available", "Reserved"])
            restaurant_id = st.text_input("New Restaurant_ID (blank=skip)")
            if st.form_submit_button("Update"):
                cap = int(capacity) if capacity.strip() else None
                stat = status if status else None
                rid = int(restaurant_id) if restaurant_id.strip() else None
                update_table(table_id, cap, stat, rid)
                st.success("Updated!")
                st.rerun()

    with st.expander("Delete Table"):
        with st.form(key="dining_tables_delete_form"):
            table_id = st.number_input("Table_ID to delete", min_value=1, step=1)
            if st.form_submit_button("Delete"):
                delete_table(table_id)
                st.success("Deleted!")
                st.rerun()