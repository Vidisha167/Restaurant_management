import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="vidsql7834^^??",
        database="restaurant_db"
    )
    return conn

def execute_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return result

def call_procedure(proc_name, params=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.callproc(proc_name, params or [])
        for result in cursor.stored_results():
            return result.fetchall()
    finally:
        cursor.close()
        conn.close()

