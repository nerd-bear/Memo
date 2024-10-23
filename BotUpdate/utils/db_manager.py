import sqlite3
import datetime
import json

DB_PATH = "./data/memo.db"

def get_db_connection():
    return sqlite3.connect(DB_PATH)

def execute_query(query: str, params: tuple = (), fetch: bool = False):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        if fetch:
            return cursor.fetchall()
        conn.commit()
        return True

def add_feedback(user_id: str, message: str) -> bool:
    datetime_value = datetime.datetime.now().strftime("%S:%M:%H %d/%m/%y")
    query = "INSERT INTO feedback VALUES (?, ?, ?)"
    return execute_query(query, (user_id, message, datetime_value))

def add_history(user_id: int, command: str, arguments: list[str] = ["none"]) -> bool:
    args_json = json.dumps(arguments)
    datetime_value = datetime.datetime.now().strftime("%S:%M:%H %d/%m/%y")
    query = "INSERT INTO history (user_id, command, arguments, datetime) VALUES (?, ?, ?, ?)"
    return execute_query(query, (user_id, command, args_json, datetime_value))

def get_usage(command_name: str) -> tuple[str, str, str]:
    query = "SELECT command_name, arguments, level FROM usage WHERE command_name = ?"
    result = execute_query(query, (command_name,), fetch=True)
    return result[0] if result else None

def get_all_usages() -> list[tuple[str, str, str]]:
    query = "SELECT command_name, arguments, level FROM usage"
    return execute_query(query, fetch=True)

def add_usage(command_name: str, arguments: list[str], level: int) -> bool:
    if not 0 <= level <= 3:
        raise ValueError("Level must be between 0 and 3")
    query = "INSERT INTO usage (command_name, arguments, level) VALUES (?, ?, ?)"
    args_json = json.dumps(arguments)
    return execute_query(query, (command_name, args_json, str(level)))

def create_tables():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS feedback (user_id TEXT, message TEXT, datetime TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS history (user_id INTEGER, command TEXT, arguments TEXT, datetime TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS usage (command_name TEXT, arguments TEXT, level TEXT)")
        conn.commit()

# Call this function when initializing the bot to ensure tables exist
create_tables()