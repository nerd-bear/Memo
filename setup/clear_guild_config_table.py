import sqlite3

db_connection = sqlite3.connect("./memo.db")
db_cursor = db_connection.cursor()
db_cursor.execute("DROP TABLE guild_configs")
db_cursor.execute("CREATE TABLE guild_configs(guild_id, command_prefix)")
db_connection.commit()
