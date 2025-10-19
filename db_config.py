import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="vidsql7834^^??",
        database="mini_project"
    )
    return conn
