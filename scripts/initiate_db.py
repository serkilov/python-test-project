import sqlite3


# Удаление таблицы
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


# Создание таблицы
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


init_table("results")
