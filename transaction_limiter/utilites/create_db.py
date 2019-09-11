def create_connection(db_file):
    import sqlite3
    from sqlite3 import Error

    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("--------DB OK--------", sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()




