import streamlit as st
from backend.orders import get_orders, add_order, delete_order, update_order
import datetime
import pandas as pd

def show_orders_page():
    st.header("Orders")

    # Show all orders
    orders = get_orders()
    orders_df = pd.DataFrame(orders)

    # Convert Order_Time from timedelta to HH:MM:SS format (removes "0 days")
    if "Order_Time" in orders_df.columns:
        orders_df["Order_Time"] = orders_df["Order_Time"].apply(
        lambda x: str(x).split(" ")[-1] if pd.notnull(x) else ""
        )

    st.table(orders_df)

    # --- ADD ORDER ---
    with st.expander("Add New Order", expanded=False):
        with st.form("add_order_form"):
            total_amount = st.number_input("Total Amount", min_value=0.0, format="%.2f")
            order_time = st.time_input("Order Time", value=datetime.time(10, 0))
            order_date = st.date_input("Order Date")
            customer_id = st.number_input("Customer ID", min_value=1, step=1)
            table_id = st.number_input("Table ID", min_value=1, step=1)
            waiter_id = st.number_input("Waiter ID", min_value=1, step=1)

            submitted = st.form_submit_button("Add Order")
            if submitted:
                add_order(total_amount, order_time, order_date, customer_id, table_id, waiter_id)
                st.success("Order added successfully!")

    # --- DELETE ORDER ---
    with st.expander("Delete Order"):
        with st.form("delete_order_form"):
            order_id = st.number_input("Order ID to Delete", min_value=1, step=1)
            submitted = st.form_submit_button("Delete Order")
            if submitted:
                delete_order(order_id)
                st.success("Order deleted successfully!")

    # --- UPDATE ORDER ---
    with st.expander("Update Order"):
        with st.form("update_order_form"):
            order_id = st.number_input("Order ID to Update", min_value=1, step=1)
            total_amount = st.number_input("New Total Amount (leave blank if no change)")
            order_time = st.time_input("New Order Time (HH:MM:SS, leave blank if no change)")
            order_date = st.date_input("New Order Date (YYYY-MM-DD, leave blank if no change)")
            customer_id = st.number_input("New Customer ID (leave blank if no change)")
            table_id = st.number_input("New Table ID (leave blank if no change)")
            waiter_id = st.number_input("New Waiter ID (leave blank if no change)")

            submitted = st.form_submit_button("Update Order")
            if submitted:
                update_order(
                    order_id,
                    total_amount if total_amount else None,
                    order_time if order_time else None,
                    order_date if order_date else None,
                    customer_id if customer_id else None,
                    table_id if table_id else None,
                    waiter_id if waiter_id else None
                )
                st.success(" Order updated successfully!")
    