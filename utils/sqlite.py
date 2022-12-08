import sqlite3


def init_table(name: str):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        sqlite_create_query = f"""CREATE TABLE {name}(
                                 RUN_ID int,
                                 PASSED int,
                                 FAILED int,
                                 SKIPPED int);"""

        cursor.execute(sqlite_create_query)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def insert_results(records):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()

        sqlite_insert_query = """INSERT INTO results
                                 (RUN_ID, PASSED, FAILED, SKIPPED)
                                 VALUES (?, ?, ?, ?);"""

        cursor.executemany(sqlite_insert_query, records)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def get_results():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()

        sqlite_query = """SELECT * from results;"""

        data = cursor.execute(sqlite_query)
        for row in data:
            print(row)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def delete_table(name: str):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        sqlite_query = f"""DROP TABLE {name};"""
        cursor.execute(sqlite_query)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()

