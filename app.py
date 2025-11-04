import streamlit as st
import mysql.connector
from frontend.customers_page import show_customers_page
from frontend.restaurants_page import show_restaurant_page
from frontend.orders_page import show_orders_page
from frontend.reservations_page import show_reservations_page
from frontend.order_items_page import show_order_items_page
from frontend.tables_page import show_tables_page
from frontend.menu_page import show_menu_page
from frontend.waiter_page import show_waiters_page
from frontend.payment_page import show_payments_page


from dotenv import load_dotenv
import os

load_dotenv()  # load .env file

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

st.write("DEBUG:", DB_NAME)


st.set_page_config(page_title="Restaurant Management System", layout="wide")

# ============================
# CUSTOMER PORTAL (NO LOGIN)
# ============================
st.sidebar.header("🧾 Customer Portal")

st.sidebar.markdown("If you’re a customer, please enter your details below:")

customer_name = st.sidebar.text_input("Name")
customer_phone = st.sidebar.text_input("Phone Number")
customer_email = st.sidebar.text_input("Email")

if st.sidebar.button("Continue as Customer"):
    if customer_name and customer_phone and customer_email:
        try:
            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,   # <--- replace with your root password
                database=DB_NAME
            )
            cur = conn.cursor()

            # insert new customer (ignore if already exists)
            cur.execute("""
                INSERT INTO Customer (Name, Phone, Email)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE Phone=VALUES(Phone), Email=VALUES(Email)
            """, (customer_name, customer_phone, customer_email))
            conn.commit()

            cur.close()
            conn.close()

            st.session_state["role"] = "customer"
            st.session_state["username"] = customer_name
            st.session_state["logged_in"] = True
            st.success(f"Welcome {customer_name}! You can now view the menu and place your order.")

        except mysql.connector.Error as e:
            st.error(f"Database error: {e}")
    else:
        st.warning("Please fill all customer details before continuing.")

# ============================
# STAFF PORTAL (LOGIN)
# ============================
st.sidebar.header("👨‍💼 Staff Login")

username = st.sidebar.text_input("Staff Username")
password = st.sidebar.text_input("Password", type="password")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.sidebar.button("Login as Staff"):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vidsql7834^^??",
            database="restaurant_db"
        )
        st.session_state["username"] = username
        st.session_state["role"] = "staff"
        st.session_state["logged_in"] = True
        st.sidebar.success(f"✅ Logged in as {username} (staff)")
        conn.close()
    except mysql.connector.Error as e:
        st.sidebar.error(f"❌ Login failed: {e}")

# ============================
# MAIN APP CONTENT
# ============================

if not st.session_state.get("logged_in"):
    st.warning("Please login (staff) or continue as customer.")
    st.stop()

st.title("Restaurant Management System")

def place_order(cart, total):
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cur = conn.cursor()

    # find customer ID
    cur.execute("SELECT Customer_ID FROM Customer WHERE Name=%s", (st.session_state["username"],))
    customer_id = cur.fetchone()[0]

    # insert into CustomerOrder
    cur.execute("""
    INSERT INTO CustomerOrder (Customer_ID, Order_Date, Order_Time, Total_Amount)
    VALUES (%s, CURDATE(), CURTIME(), %s)
""", (customer_id, total))

    order_id = cur.lastrowid  # get the auto-generated Order_ID


    # insert into OrderItem
    for item in cart:
        cur.execute("""
            INSERT INTO OrderItem (Order_ID, Item_ID, Quantity)
            VALUES (%s, %s, %s)
        """, (order_id, item['Item_ID'], 1))

    conn.commit()
    cur.close()
    conn.close()

    st.success(f"✅ Order placed successfully! Your order ID is {order_id}.")


def show_cart():
    st.subheader("🛒 Your Cart")

    cart = st.session_state.get("cart", [])
    if not cart:
        st.info("Your cart is empty.")
        return

    total = sum(item['Price'] for item in cart)

    for i, item in enumerate(cart):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(f"{item['Name']} ({item['Location']})")
        with col2:
            st.write(f"₹{item['Price']}")
        with col3:
            if st.button("Remove", key=f"remove_{i}"):
                cart.pop(i)
                st.experimental_rerun()

    st.write(f"### 💰 Total: ₹{total}")

    if st.button("Place Order"):
        place_order(cart, total)
        st.session_state["cart"] = []


def show_city_menu(selected_city):
    st.subheader(f"🍽️ Menu for restaurants in {selected_city}")

    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cur = conn.cursor(dictionary=True)

    # Fetch all menu items for restaurants in the selected city
    cur.execute("""
        SELECT M.Item_ID, M.Name, M.Price,M.Category,R.Location
        FROM Menu M
        JOIN Restaurant R ON M.Restaurant_ID = R.Restaurant_ID
        WHERE R.Location = %s
    """, (selected_city,))
    menu_items = cur.fetchall()

    cur.close()
    conn.close()

    if not menu_items:
        st.info("No menu items found for this city.")
        return

    # initialize cart if not already there
    if "cart" not in st.session_state:
        st.session_state["cart"] = []

    # display each item
    for item in menu_items:
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
        with col1:
            st.write(f"**{item['Name']}** ({item['Location']})")
        with col2:
            st.write(f"₹{item['Price']}")
        with col3:
            if st.button("Add to Cart", key=f"add_{item['Item_ID']}"):
                st.session_state["cart"].append(item)
                st.success(f"✅ Added {item['Name']} to cart")

    st.divider()
    show_cart()


if st.session_state["role"] == "customer":
    st.title(f"Welcome {st.session_state['username']} 👋")

    # --- City selection ---
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cur = conn.cursor()

    cur.execute("SELECT DISTINCT Location FROM Restaurant")
    cities = [row[0] for row in cur.fetchall()]
    cur.close()
    conn.close()

    selected_city = st.selectbox("Select your city:", cities)

    if "cart" not in st.session_state:
        st.session_state["cart"] = []

    if selected_city:
        show_city_menu(selected_city)

else:
    # full access for staff
    tabs = st.tabs([
        "Home", "Customers", "Restaurants", "Orders", "Reservations",
        "Tables", "Menu", "Waiter", "Order Item", "Payment"
    ])
    with tabs[0]:
        st.header(f"Welcome, {st.session_state['username']} 👋")
        st.write("Use the tabs above to manage the system.")
    with tabs[1]: show_customers_page()
    with tabs[2]: show_restaurant_page()
    with tabs[3]: show_orders_page()
    with tabs[4]: show_reservations_page()
    with tabs[5]: show_tables_page()
    with tabs[6]: show_menu_page()
    with tabs[7]: show_waiters_page()
    with tabs[8]: show_order_items_page()
    with tabs[9]: show_payments_page()
