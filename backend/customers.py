from backend.db import execute_query

def get_customers():
    return execute_query("SELECT * FROM Customer")

def add_customer(name, phone=None, email=None):
    if not name:
        raise ValueError("Name cannot be empty")

    columns = ["Name"]
    placeholders = ["%s"]
    params = [name]

    if phone:
        columns.append("Phone")
        placeholders.append("%s")
        params.append(phone)

    if email:
        columns.append("Email")
        placeholders.append("%s")
        params.append(email)

    query = f"INSERT INTO Customer ({', '.join(columns)}) VALUES ({', '.join(placeholders)})"
    execute_query(query, tuple(params))


def update_customer(customer_id, name=None, phone=None, email=None):
    updates = []
    params = []

    if name:
        updates.append("Name=%s")
        params.append(name)
    if phone:
        updates.append("Phone=%s")
        params.append(phone)
    if email:
        updates.append("Email=%s")
        params.append(email)

    if not updates:
        # Nothing to update
        return

    params.append(customer_id)
    query = f"UPDATE Customer SET {', '.join(updates)} WHERE Customer_ID=%s"
    execute_query(query, params)


def delete_customer(customer_id):
    query = "DELETE FROM Customer WHERE Customer_ID=%s"
    execute_query(query, (customer_id,))
