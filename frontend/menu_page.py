import streamlit as st
from backend.menu import get_menu_items, add_menu_item, update_menu_item, delete_menu_item

def show_menu_page():
    st.header("Menu")
    st.dataframe(get_menu_items(), use_container_width=True)

    with st.expander("Add Menu Item"):
        with st.form(key="menu_add_form"):
            name = st.text_input("Name")
            price = st.number_input("Price", min_value=0.0, step=0.5, format="%.2f")
            category = st.text_input("Category")
            restaurant_id = st.text_input("Restaurant_ID")
            if st.form_submit_button("Add"):
                rid = int(restaurant_id) if restaurant_id.strip() else None
                add_menu_item( name, price, category, rid)
                st.success("Added!")
                st.rerun()

    with st.expander("Update Menu Item"):
        with st.form(key="menu_update_form"):
            item_id = st.number_input("Item_ID to update", min_value=1, step=1)
            name = st.text_input("New Name (blank=skip)")
            price = st.text_input("New Price (blank=skip)")
            category = st.text_input("New Category (blank=skip)")
            restaurant_id = st.text_input("New Restaurant_ID (blank=skip)")
            if st.form_submit_button("Update"):
                price_v = float(price) if price.strip() else None
                rid_v = int(restaurant_id) if restaurant_id.strip() else None
                update_menu_item(item_id, name or None, price_v, category or None, rid_v)
                st.success("Updated!")
                st.rerun()

    with st.expander("Delete Menu Item"):
        with st.form(key="menu_delete_form"):
            item_id = st.number_input("Item_ID to delete", min_value=1, step=1)
            if st.form_submit_button("Delete"):
                delete_menu_item(item_id)
                st.success("Deleted!")
                st.rerun()