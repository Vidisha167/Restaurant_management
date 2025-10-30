import streamlit as st
from backend.payment import get_payments, add_payment, update_payment, delete_payment
from backend.db import call_procedure

def show_payments_page():
    st.header("Payments")
    st.dataframe(get_payments(), use_container_width=True)

    with st.expander("Add Payment"):
        with st.form(key="payments_add_form"):
            amount = st.number_input("Amount", min_value=0.0, step=0.5, format="%.2f")
            payment_type = st.selectbox("Payment_Type", ["Cash", "Card", "UPI"])
            payment_date = st.date_input("Payment_Date")
            order_id = st.number_input("Order_ID", min_value=1, step=1)
            if st.form_submit_button("Add"):
                add_payment(amount, payment_type, payment_date, order_id)
                st.success("Added!")
                st.rerun()

    with st.expander("Update Payment"):
        with st.form(key="payments_update_form"):
            payment_id = st.number_input("Payment_ID to update", min_value=1, step=1)
            amount = st.text_input("New Amount (blank=skip)")
            payment_type = st.selectbox("New Payment_Type (optional)", ["", "Cash", "Card", "UPI"])
            payment_date = st.text_input("New Payment_Date (YYYY-MM-DD, blank=skip)")
            order_id = st.text_input("New Order_ID (blank=skip)")
            if st.form_submit_button("Update"):
                amt = float(amount) if amount.strip() else None
                ptype = payment_type if payment_type else None
                pdate = payment_date.strip() or None
                oid = int(order_id) if order_id.strip() else None
                update_payment(payment_id, amt, ptype, pdate, oid)
                st.success("Updated!")
                st.rerun()

    with st.expander("Delete Payment"):
        with st.form(key="payments_delete_form"):
            payment_id = st.number_input("Payment_ID to delete", min_value=1, step=1)
            if st.form_submit_button("Delete"):
                delete_payment(payment_id)
                st.success("Deleted!")
                st.rerun()

   