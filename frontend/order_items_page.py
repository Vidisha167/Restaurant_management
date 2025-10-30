import streamlit as st
import pandas as pd
from backend.order_items import (
    get_order_items, add_order_item, update_order_item, delete_order_item
)


def show_order_items_page():
    st.header("Manage Order Items")

    order_items = get_order_items()
    df = pd.DataFrame(order_items)
    st.dataframe(df, use_container_width=True)

    #filter by order_id
    with st.expander("View Items by Order ID"):
        with st.form("filter_order_items"):
            order_id_input = st.text_input("Enter Order_ID (optional)", placeholder="Leave blank to show all")
            show_btn = st.form_submit_button("Show Items")

        if show_btn:
            try:
                if order_id_input.strip():
                    filtered_items = get_order_items(int(order_id_input))
                else:
                    filtered_items = get_order_items()

                if filtered_items:
                    st.dataframe(pd.DataFrame(filtered_items), use_container_width=True)
                else:
                    st.warning("No items found for that Order_ID.")
            except ValueError:
                st.error("Please enter a valid number for Order_ID.")

    #add order_item
    with st.expander("Add New Order Item"):
        with st.form("add_order_item_form"):
            order_id = st.number_input("Order_ID", min_value=1, step=1)
            item_id = st.number_input("Item_ID", min_value=1, step=1)
            quantity = st.number_input("Quantity", min_value=1, step=1)
            subtotal = st.number_input("Subtotal (₹)", min_value=0.0, step=0.5, format="%.2f")
            add_btn = st.form_submit_button("Add Item")

            if add_btn:
                try:
                    add_order_item(order_id, item_id, quantity, subtotal)
                    st.success(f"✅ Added item {item_id} to Order {order_id} successfully.")
                except Exception as e:
                    st.error(f"Error adding item: {e}")

    #update order item
    with st.expander("Update Order Item"):
        with st.form("update_order_item_form"):
            order_id = st.number_input("Existing Order_ID", min_value=1, step=1)
            item_id = st.number_input("Existing Item_ID", min_value=1, step=1)
            quantity = st.text_input("New Quantity (leave blank to skip)")
            subtotal = st.text_input("New Subtotal (leave blank to skip)")
            update_btn = st.form_submit_button("Update Item")

            if update_btn:
                try:
                    qty_val = int(quantity) if quantity.strip() else None
                    sub_val = float(subtotal) if subtotal.strip() else None
                    update_order_item(order_id, item_id, qty_val, sub_val)
                    st.success(f"Updated Item {item_id} in Order {order_id}.")
                except ValueError:
                    st.error("Please enter valid numeric values.")
                except Exception as e:
                    st.error(f"Error updating item: {e}")

    #delete order item
    with st.expander("Delete Order Item"):
        with st.form("delete_order_item_form"):
            order_id = st.number_input("Order_ID to delete from", min_value=1, step=1)
            item_id = st.number_input("Item_ID to delete", min_value=1, step=1)
            del_btn = st.form_submit_button("Delete Item")

            if del_btn:
                try:
                    delete_order_item(order_id, item_id)
                    st.success(f"✅ Deleted Item {item_id} from Order {order_id}.")
                except Exception as e:
                    st.error(f"Error deleting item: {e}")
