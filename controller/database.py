import sqlite3

def create():
    conn = None
    try:
        conn = sqlite3.connect("emails.db")
        cursor = conn.cursor()
        #create emails table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY,

            )
            """
            )
        #create trash table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS trash
            """
            )

    except sqlite3.Error as e:
        print(e)

    finally:
        if conn:
            conn.close()