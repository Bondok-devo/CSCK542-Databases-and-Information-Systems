# =================================================================
#  File: db_connector.py
#  Purpose: Handles the connection to the MySQL database and query execution.
# =================================================================
"""
This module provides functions to connect to the database and execute queries.
"""
import mysql.connector
from mysql.connector import Error
from db_config import DB_CONFIG

def get_db_connection():
    """Establishes a connection to the database."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error connecting to MySQL Database: {e}")
        return None

def execute_query(query, params=None, fetch=None):
    """
    Execute a database query.
    - For SELECT, set fetch='all' or fetch='one'.
    - For INSERT, UPDATE, DELETE, leave fetch=None.
    Returns results for SELECT, or the last inserted ID for INSERT.
    """
    conn = get_db_connection()
    if conn is None:
        return None if fetch else False

    cursor = conn.cursor(dictionary=True, buffered=True)
    last_row_id = None
    try:
        cursor.execute(query, params or ())

        if fetch == 'all':
            results = cursor.fetchall()
            return results
        elif fetch == 'one':
            result = cursor.fetchone()
            return result
        else:
            conn.commit()
            if cursor.lastrowid:
                last_row_id = cursor.lastrowid
            return last_row_id if last_row_id else True

    except Error as e:
        print(f"Error executing query: {e}")
        conn.rollback()
        return None if fetch else False
    finally:
        cursor.close()
        conn.close()
