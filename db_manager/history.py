import sqlite3
import datetime
import json
from typing import List, Union

def sanitize_input(value: Union[int, str, List[str]]) -> Union[str, List[str]]:
    """Sanitizes input values before database insertion
    
    Args:
        value: The value to sanitize
        
    Returns:
        Sanitized value
    """
    if isinstance(value, (int, str)):
        return str(value).strip()
    elif isinstance(value, list):
        return [str(x).strip() for x in value]
    else:
        raise ValueError(f"Invalid input type: {type(value)}")

def add_history(user_id: str, guild_id: str, command: str, arguments: List[str] = None) -> bool:
    """Uses SQLite to add user command to history of commands ran with enhanced security

    Args:
        user_id: The user id of the person who ran the command
        guild_id: The guild id of the server that the user ran the command in
        command: The name of the command that the user ran
        arguments: The arguments passed to the command, defaults to None

    Returns:
        bool: True on success, False on failure

    Raises:
        ValueError: If input validation fails
    """
    try:
        if arguments is None:
            arguments = ["none"]

        # Input validation
        if not isinstance(user_id, str) or not isinstance(guild_id, str):
            raise ValueError("User ID and Guild ID must be strings")
        
        if not isinstance(command, str) or not command.strip():
            raise ValueError("Command must be a non-empty string")
        
        if not isinstance(arguments, list):
            raise ValueError("Arguments must be a list")

        # Sanitize inputs
        clean_user_id = sanitize_input(user_id)
        clean_guild_id = sanitize_input(guild_id)
        clean_command = sanitize_input(command)
        clean_arguments = sanitize_input(arguments)

        # Additional validation that IDs are not empty after cleaning
        if not clean_user_id or not clean_guild_id:
            raise ValueError("IDs cannot be empty")

        # Convert arguments to JSON
        args_json = json.dumps(clean_arguments, ensure_ascii=True)

        # Get current timestamp
        datetime_value = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Database connection with context manager
        with sqlite3.connect("./memo.db", timeout=20.0) as db_connection:
            query = """
                INSERT INTO history 
                    (user_id, guild_id, command, arguments, datetime) 
                VALUES 
                    (?, ?, ?, ?, ?)
            """
            
            db_connection.execute(query, (
                clean_user_id,
                clean_guild_id,
                clean_command,
                args_json,
                datetime_value
            ))
            
            db_connection.commit()
            return True

    except ValueError as e:
        print(f"ERROR_LOG: Validation error: {str(e)}")
        return False
    except json.JSONDecodeError as e:
        print(f"ERROR_LOG: JSON encoding error: {str(e)}")
        return False
    except sqlite3.Error as e:
        print(f"ERROR_LOG: Database error: {str(e)}")
        return False
    except Exception as e:
        print(f"ERROR_LOG: Unexpected error: {str(e)}")
        return False