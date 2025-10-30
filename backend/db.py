import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
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

