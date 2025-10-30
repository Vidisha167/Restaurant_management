from backend.db import execute_query

def get_reservations():
    return execute_query("SELECT * FROM Reservation")

def add_reservation(date, time, number_of_people, customer_id, table_id):
    if not all([date, time, number_of_people, customer_id, table_id]):
        raise ValueError("All fields must be filled")

    query = """
        INSERT INTO Reservation (Date, Time, Number_Of_People, Customer_ID, Table_ID)
        VALUES (%s, %s, %s, %s, %s)
    """
    execute_query(query, (date, time, number_of_people, customer_id, table_id))


def update_reservation(reservation_id, date=None, time=None, number_of_people=None, customer_id=None, table_id=None):
    updates = []
    params = []

    if date:
        updates.append("Date=%s")
        params.append(date)
    if time:
        updates.append("Time=%s")
        params.append(time)
    if number_of_people:
        updates.append("Number_Of_People=%s")
        params.append(number_of_people)
    if customer_id:
        updates.append("Customer_ID=%s")
        params.append(customer_id)
    if table_id:
        updates.append("Table_ID=%s")
        params.append(table_id)

    if not updates:
        return  # Nothing to update

    params.append(reservation_id)
    query = f"UPDATE Reservation SET {', '.join(updates)} WHERE Reservation_ID=%s"
    execute_query(query, params)


def delete_reservation(reservation_id):
    query = "DELETE FROM Reservation WHERE Reservation_ID=%s"
    execute_query(query, (reservation_id,))
