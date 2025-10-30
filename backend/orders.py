from backend.db import execute_query

def get_orders():
    return execute_query("SELECT * FROM CustomerOrder")


def add_order(total_amount=None, order_time=None, order_date=None, customer_id=None, table_id=None, waiter_id=None):
    if not all([customer_id, table_id, waiter_id]):
        raise ValueError("Customer_ID, Table_ID, and Waiter_ID cannot be empty")

    query = """
        INSERT INTO CustomerOrder (Total_Amount, Order_Time, Order_Date, Customer_ID, Table_ID, Waiter_ID)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    execute_query(query, (total_amount, order_time, order_date, customer_id, table_id, waiter_id))

def update_order(order_id, total_amount=None, order_time=None, order_date=None, customer_id=None, table_id=None, waiter_id=None):
    updates = []
    params = []

    if total_amount:
        updates.append("Total_Amount=%s")
        params.append(total_amount)
    if order_time:
        updates.append("Order_Time=%s")
        params.append(order_time)
    if order_date:
        updates.append("Order_Date=%s")
        params.append(order_date)
    if customer_id:
        updates.append("Customer_ID=%s")
        params.append(customer_id)
    if table_id:
        updates.append("Table_ID=%s")
        params.append(table_id)
    if waiter_id:
        updates.append("Waiter_ID=%s")
        params.append(waiter_id)

    if not updates:
        return  # nothing to update

    params.append(order_id)
    query = f"UPDATE CustomerOrder SET {', '.join(updates)} WHERE Order_ID=%s"
    execute_query(query, tuple(params))

def delete_order(order_id):
    query = "DELETE FROM CustomerOrder WHERE Order_ID=%s"
    execute_query(query, (order_id,))
