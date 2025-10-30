import streamlit as st
from backend.reservations import get_reservations, add_reservation, delete_reservation, update_reservation
import pandas as pd

def show_reservations_page():
    st.header("Reservations")

    # Show all reservations
    reservations = get_reservations()
    reservations_df = pd.DataFrame(reservations)

    if "Time" in reservations_df.columns:
        reservations_df["Time"] = reservations_df["Time"].apply(
            lambda x: str(x).split(" ")[-1] if pd.notnull(x) else ""
        )
    st.table(reservations_df)

    # Add reservation
    with st.expander("Add New Reservation", expanded=False):
        with st.form("add_reservation_form"):
            date = st.date_input("Date")
            time = st.text_input("Time (HH:MM:SS)")
            number_of_people = st.number_input("Number Of People", min_value=1)
            customer_id = st.number_input("Customer ID", min_value=1)
            table_id = st.number_input("Table ID", min_value=1)
            submitted = st.form_submit_button("Add Reservation")
            if submitted:
                add_reservation(date, time, number_of_people, customer_id, table_id)
                st.success("Reservation added!")

    # Delete reservation
    with st.expander("Delete Reservation"):
        with st.form("delete_reservation_form"):
            reservation_id = st.number_input("Reservation ID to Delete", min_value=1, step=1)
            submitted = st.form_submit_button("Delete Reservation")
            if submitted:
                delete_reservation(reservation_id)
                st.success("Reservation deleted!")

    # Update reservation
    with st.expander("Update Reservation"):
        with st.form("update_reservation_form"):
            reservation_id = st.number_input("Reservation ID to Update", min_value=1, step=1)
            date = st.date_input("New Date (leave blank for no change)")
            time = st.text_input("New Time (leave blank for no change)")
            number_of_people = st.text_input("New Number Of People (leave blank for no change)")
            customer_id = st.text_input("New Customer ID (leave blank for no change)")
            table_id = st.text_input("New Table ID (leave blank for no change)")
            submitted = st.form_submit_button("Update Reservation")
            if submitted:
                update_reservation(
                    reservation_id,
                    date if date else None,
                    time if time else None,
                    int(number_of_people) if number_of_people else None,
                    int(customer_id) if customer_id else None,
                    int(table_id) if table_id else None,
                )
                st.success("Reservation updated!")
