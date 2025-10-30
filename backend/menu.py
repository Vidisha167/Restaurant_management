from backend.db import execute_query

def get_menu_items():
    return execute_query("SELECT * FROM Menu")

def add_menu_item( name, price, category, restaurant_id):
    cols = [ "Name", "Price","Category","Restaurant_ID"]; 
    ph = [ "%s", "%s","%s","%s"]; 
    params = [ name, price,category,restaurant_id]
    execute_query(f"INSERT INTO Menu ({', '.join(cols)}) VALUES ({', '.join(ph)})", tuple(params))

def update_menu_item(item_id, name=None, price=None, category=None, restaurant_id=None):
    ups, params = [], []
    if name is not None:          ups.append("Name=%s");          params.append(name)
    if price is not None:         ups.append("Price=%s");         params.append(price)
    if category is not None:      ups.append("Category=%s");      params.append(category)
    if restaurant_id is not None: ups.append("Restaurant_ID=%s"); params.append(restaurant_id)
    if not ups: return
    params.append(item_id)
    execute_query(f"UPDATE Menu SET {', '.join(ups)} WHERE Item_ID=%s", tuple(params))

def delete_menu_item(item_id):
    execute_query("DELETE FROM Menu WHERE Item_ID=%s", (item_id,))