import sqlite3

db_connection = sqlite3.connect("./memo.db")
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE history(user_id, guild_id, command, arguments, datetime)")
db_connection.commit()