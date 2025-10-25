from backend.db import execute_query

def get_restaurant():
    return execute_query("SELECT * FROM RESTAURANT")

def add_restaurant(contact_number, location=None):
    if not contact_number:
        raise ValueError("Contact number cannot be empty")

    columns = ["Contact_Number"]
    placeholders = ["%s"]
    params = [contact_number]

    if location:
        columns.append("Location")
        placeholders.append("%s")
        params.append(location)

    query = f"INSERT INTO RESTAURANT ({', '.join(columns)}) VALUES ({', '.join(placeholders)})"
    execute_query(query, tuple(params))

def update_restaurant(restaurant_id, contact_number=None, location=None):
    updates = []
    params = []

    if contact_number:
        updates.append("Contact_Number=%s")
        params.append(contact_number)
    if location:
        updates.append("Location=%s")
        params.append(location)

    if not updates:
        return

    params.append(restaurant_id)
    query = f"UPDATE RESTAURANT SET {', '.join(updates)} WHERE Restaurant_ID=%s"
    execute_query(query, tuple(params))

def delete_restaurant(restaurant_id):
    query = "DELETE FROM RESTAURANT WHERE Restaurant_ID=%s"
    execute_query(query, (restaurant_id,))
