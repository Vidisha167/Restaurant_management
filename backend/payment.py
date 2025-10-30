from backend.db import execute_query

def get_payments():
    return execute_query("SELECT * FROM Payment")

def add_payment(amount, payment_type, payment_date, order_id):
    query = """
        INSERT INTO Payment (Amount, Payment_Type, Payment_Date, Order_ID)
        VALUES (%s, %s, %s, %s)
    """
    execute_query(query, (amount, payment_type, payment_date, order_id))

def update_payment(payment_id, amount=None, payment_type=None, payment_date=None, order_id=None):
    updates, params = [], []

    if amount is not None:
        updates.append("Amount=%s")
        params.append(amount)

    if payment_type is not None:
        updates.append("Payment_Type=%s")
        params.append(payment_type)

    if payment_date is not None:
        updates.append("Payment_Date=%s")
        params.append(payment_date)

    if order_id is not None:
        updates.append("Order_ID=%s")
        params.append(order_id)

    if not updates:
        return  # nothing to update

    params.append(payment_id)
    query = f"UPDATE Payment SET {', '.join(updates)} WHERE Payment_ID=%s"
    execute_query(query, tuple(params))

def delete_payment(payment_id):
    execute_query("DELETE FROM Payment WHERE Payment_ID=%s", (payment_id,))
