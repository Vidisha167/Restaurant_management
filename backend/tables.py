from backend.db import execute_query

def get_tables():
    return execute_query("SELECT * FROM DiningTable")

def add_table(capacity,status,restaurant_id):
    cols = ["Capacity","Status","Restaurant_ID"]
    ph   = ["%s", "%s","%s"]
    params = [capacity,status,restaurant_id]
    execute_query(f"INSERT INTO DiningTable ({', '.join(cols)}) VALUES ({', '.join(ph)})", tuple(params))

def update_table(table_id, capacity=None, status=None, restaurant_id=None):
    ups, params = [], []
    if capacity is not None:     ups.append("Capacity=%s");     params.append(capacity)
    if status is not None:       ups.append("Status=%s");       params.append(status)
    if restaurant_id is not None:ups.append("Restaurant_ID=%s");params.append(restaurant_id)
    if not ups: return
    params.append(table_id)
    execute_query(f"UPDATE DiningTable SET {', '.join(ups)} WHERE Table_ID=%s", tuple(params))

def delete_table(table_id):
    execute_query("DELETE FROM DiningTable WHERE Table_ID=%s", (table_id,))