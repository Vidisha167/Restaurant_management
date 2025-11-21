README.md
🍽️ Restaurant Management System (DBMS Mini Project)

OVERVIEW
The Restaurant Management System (RMS) is a database-driven application designed to streamline restaurant operations such as customer management, reservations, menu handling, order processing, billing, and staff management.
This project showcases core DBMS concepts including ER modeling, relational schema design, normalization, SQL operations, and Python–MySQL connectivity.

The backend includes modular Python files handling CRUD operations for each entity in the system:
-Customer Management
-Menu Items
-Reservations
-Orders & Order Items
-Payments
-Dining Tables
-Waiters
-Restaurant Details
-Database Connectivity Layer

The system uses a MySQL database and Python (mysql-connector-python) for execution of queries.

FEATURES:
- Customer Management
    Add, update, delete, and list customers.
- Menu Management
    Manage menu items including name, price, category, and restaurant ID.
- Order & Billing
    Place customer orders, attach order items, and process payments.
- Reservations
    Create, update, and delete reservations linked to specific tables and customers.
- Table & Waiter Management
    Maintain table availability, capacity, and waiter details.
- Centralized Database Layer
    Reusable database functions for executing queries and calling stored procedures.

TOOLS USED:
-Python 3.x
-MySQL
-mysql-connector-python
-Git & GitHub
-Streamli

ER DIAGRAM
<img width="2561" height="1111" alt="finaler drawio" src="https://github.com/user-attachments/assets/68ac46f1-43f3-4b48-a44f-17d80f6bc83f" />

RELATIONALSCHEMA:
Customer(Customer_ID, Name, Phone, Email)
Menu(Item_ID, Name, Price, Category, Restaurant_ID)
DiningTable(Table_ID, Capacity, Status, Restaurant_ID)
Waiter(Waiter_ID, Name, Phone, Shift, Restaurant_ID)
CustomerOrder(Order_ID, Total_Amount, Order_Time, Order_Date, Customer_ID, Table_ID, Waiter_ID)
OrderItem(Order_ID, Item_ID, Quantity, Subtotal)
Reservation(Reservation_ID, Date, Time, Number_Of_People, Customer_ID, Table_ID)
Payment(Payment_ID, Amount, Payment_Type, Payment_Date, Order_ID)
Restaurant(Restaurant_ID, Contact_Number, Location)

Team & Contribution Note
Vidisha Murali- PES1UG23CS681
VipaanchiPriyyom- PES1UG23CS693

(All team members contributed to discussions, design decisions, and documentation.
However, only one team member appears in the Git commit history — this was simply because we were all working on the same system, and due to an issue with Git authentication on other laptops, all commits had to be pushed using a single machine and Git account.
All work was still collaborative.)

How to Run the Project
1️⃣ Install Requirements
pip install mysql-connector-python

2️⃣ Configure Database
Update your database credentials in db.py:

host="localhost",
user="root",
password="your_password",
database="restaurant_db"

3️⃣ Run Python Modules
Each file can be imported or executed via an interactive Python environment.

Example:

from backend.customers import add_customer
add_customer("Alice", "9876543210", "alice@example.com")
