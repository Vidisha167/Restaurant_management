from backend.db import execute_query

def get_waiters():
    return execute_query("SELECT * FROM waiter")

def add_waiter(name, phone, shift, restaurant_id):
    cols = ["Name","Phone","Shift","Restaurant_ID"]; 
    ph = ["%s", "%s","%s","%s"]; 
    params = [name,phone,shift,restaurant_id]
    execute_query(f"INSERT INTO waiter ({', '.join(cols)}) VALUES ({', '.join(ph)})", tuple(params))

def update_waiter(waiter_id, name=None, phone=None, shift=None, restaurant_id=None):
    ups, params = [], []
    if name is not None:          ups.append("Name=%s");          params.append(name)
    if phone is not None:         ups.append("Phone=%s");         params.append(phone)
    if shift is not None:         ups.append("Shift=%s");         params.append(shift)
    if restaurant_id is not None: ups.append("Restaurant_ID=%s"); params.append(restaurant_id)
    if not ups: return
    params.append(waiter_id)
    execute_query(f"UPDATE waiter SET {', '.join(ups)} WHERE Waiter_ID=%s", tuple(params))

def delete_waiter(waiter_id):
    execute_query("DELETE FROM waiter WHERE Waiter_ID=%s", (waiter_id,))