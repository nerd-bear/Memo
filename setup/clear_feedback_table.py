import sqlite3

db_connection = sqlite3.connect("./Memo.db")
db_cursor = db_connection.cursor()
db_cursor.execute("DROP TABLE feedback")
db_cursor.execute("CREATE TABLE feedback(used_id, message, datetime)")
db_connection.commit()