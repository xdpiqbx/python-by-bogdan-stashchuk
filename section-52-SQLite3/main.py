import sqlite3

DB_NAME = "sqlite_db.db"

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     print(sqlite_conn)
#     print(sqlite3.version)

# =================================================== Create table
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses(
#         id integer PRIMARY KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#     );"""
#     sqlite_conn.execute(sql_request)

# =================================================== Insert Data to DB
# courses = [
#     (124, "Django course", 107, 60),
#     (125, "Pandas course", 110, 35),
#     (126, "Telegram course", 50, 10),
#     (127, "AI course", 70, 20)
# ]
#
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses Values(?, ?, ?, ?)"
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#     sqlite_conn.commit()

# =================================================== Select Data from DB
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "SELECT * FROM courses"
#     sql_cursor = sqlite_conn.execute(sql_request)
#
#     records = sql_cursor.fetchall()
#     print(records)
#
#     # for row in sql_cursor:
#     #     print(row)
