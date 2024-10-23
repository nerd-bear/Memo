import sqlite3
import datetime
import json
from typing import List, Union

def sanitize_input(value: Union[int, str, List[str]]) -> Union[int, str, List[str]]:
    """Sanitizes input values before database insertion
    
    Args:
        value: The value to sanitize
        
    Returns:
        Sanitized value
    """
    if isinstance(value, int):
        return abs(int(value))
    elif isinstance(value, str):
        return sqlite3.escape_string(str(value))
    elif isinstance(value, list):
        return [sqlite3.escape_string(str(x)) for x in value]
    else:
        raise ValueError("Invalid input type")

def add_history(user_id: int, guild_id: int, command: str, arguments: List[str] = ["none"]) -> bool:
    """Uses SQLite to add user command to history of commands ran with enhanced security
    
    Args:
        user_id: The user id of the person who ran the command
        guild_id: The guild id of the server that the user ran the command in
        command: The name of the command that the user ran
        arguments: The arguments passed to the command, defaults to ["none"]
    
    Returns:
        bool: True on success, False on failure
        
    Raises:
        ValueError: If input validation fails
    """
    try:
        clean_user_id = sanitize_input(user_id)
        clean_guild_id = sanitize_input(guild_id)
        clean_command = sanitize_input(command)
        clean_arguments = sanitize_input(arguments)

        if not isinstance(clean_user_id, int) or not isinstance(clean_guild_id, int):
            raise ValueError("Invalid ID format")

        if not clean_command:
            raise ValueError("Command cannot be empty")

        args_json = json.dumps(clean_arguments, ensure_ascii=True)
        
        datetime_value = datetime.datetime.now().strftime("%S:%M:%H %d/%m/%y")
        
        with sqlite3.connect("./memo.db", isolation_level='EXCLUSIVE') as db_connection:
            db_connection.set_trace_callback(print)  
            db_connection.execute("PRAGMA foreign_keys = ON")
            db_connection.execute("PRAGMA journal_mode = WAL")
            
            db_cursor = db_connection.cursor()
            
            query = """
                INSERT INTO history 
                    (user_id, guild_id, command, arguments, datetime) 
                VALUES 
                    (?, ?, ?, ?, ?)
            """
            
            db_cursor.execute(query, (
                clean_user_id,
                clean_guild_id,
                clean_command,
                args_json,
                datetime_value
            ))
            
            db_connection.commit()
            return True
            
    except ValueError as e:
        print(f"ERROR_LOG: Validation error: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"ERROR_LOG: JSON encoding error: {e}")
        return False
    except sqlite3.Error as e:
        print(f"ERROR_LOG: Database error: {e}")
        return False
    except Exception as e:
        print(f"ERROR_LOG: Unexpected error: {e}")
        return False