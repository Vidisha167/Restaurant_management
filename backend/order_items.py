from backend.db import execute_query


def get_order_items(order_id=None):
    if order_id:
        return execute_query("SELECT * FROM OrderItem WHERE Order_ID=%s", (order_id,))
    return execute_query("SELECT * FROM OrderItem")


def add_order_item(order_id, item_id, quantity, subtotal):
    if order_id is None or item_id is None or quantity is None or subtotal is None:
        raise ValueError("Order_ID, Item_ID, Quantity, and Subtotal are required.")

    query = """
        INSERT INTO OrderItem (Order_ID, Item_ID, Quantity, Subtotal)
        VALUES (%s, %s, %s, %s)
    """
    execute_query(query, (order_id, item_id, quantity, subtotal))


def update_order_item(order_id, item_id, quantity=None, subtotal=None):
    updates = []
    params = []

    if quantity is not None:
        updates.append("Quantity=%s")
        params.append(quantity)
    if subtotal is not None:
        updates.append("Subtotal=%s")
        params.append(subtotal)

    if not updates:
        return  # Nothing to update

    params.extend([order_id, item_id])

    query = f"""
        UPDATE OrderItem
        SET {', '.join(updates)}
        WHERE Order_ID=%s AND Item_ID=%s
    """
    execute_query(query, tuple(params))


def delete_order_item(order_id, item_id):
    query = "DELETE FROM OrderItem WHERE Order_ID=%s AND Item_ID=%s"
    execute_query(query, (order_id, item_id))
