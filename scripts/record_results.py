import json
import os
import sqlite3
from datetime import datetime

reports_path = os.path.join(os.path.dirname(__file__), "../tests/reports")


# Запись в таблицу
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


# Вывод из таблицы
def get_results(name: str):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()

        sqlite_query = f"""SELECT * from {name};"""

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

# ID прогона - текущее время
def get_current_datetime():
    now = datetime.now()
    return now.strftime("%H%M%S%d%m%Y")


passed = 0
failed = 0
skipped = 0
run_id = get_current_datetime()
for file in os.listdir(reports_path):
    if file.endswith("result.json"):
        file_path = os.path.join(reports_path, file)
        with open(file_path, "r") as outfile:
            json_file = json.load(outfile)
            status = json_file["status"]
        if status == "passed":
            passed += 1
        elif status == "failed":
            failed += 1
        elif status == "skipped":
            skipped += 1

insert_results([(run_id, passed, failed, skipped)])
get_results("results")
