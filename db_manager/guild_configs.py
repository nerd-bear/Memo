import sqlite3
import json


def add_guild_config(guild_id: str, command_prefix: str) -> bool:
    try:
        if not isinstance(guild_id, str):
            raise ValueError("ID must be string")

        if not isinstance(command_prefix, str):
            raise ValueError("Command_prefix must be a non-empty string")

        with sqlite3.connect("./memo.db", timeout=20.0) as db_connection:
            # First check if guild already exists to avoid duplicates
            check_query = """
                SELECT 1
                FROM guild_configs
                WHERE guild_id = ?
            """
            cursor = db_connection.execute(check_query, (guild_id,))
            if cursor.fetchone() is not None:
                print(f"ERROR_LOG: Guild ID {guild_id} already exists in database")
                return False

            # If guild doesn't exist, proceed with insert
            query = """
                INSERT INTO guild_configs
                    (guild_id, command_prefix)
                VALUES
                    (?, ?)
            """

            db_connection.execute(
                query,
                (
                    guild_id,
                    command_prefix,
                ),
            )

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


def get_guild_config(guild_id: str) -> dict:
    try:
        if not isinstance(guild_id, str):
            raise ValueError("ID must be string")

        with sqlite3.connect("./memo.db", timeout=20.0) as db_connection:
            query = """
                SELECT
                    command_prefix
                FROM
                    guild_configs
                WHERE
                    guild_id = ?
            """

            cursor = db_connection.execute(query, (guild_id,))

            result = cursor.fetchone()

            if result is None:
                return None

            return {
                "command_prefix": result[0],
            }

    except Exception as e:
        print(f"ERROR_LOG: Unexpected error: {str(e)}")
        return None


def set_guild_config(guild_id: str, command_prefix: str) -> bool:
    try:
        if not isinstance(guild_id, str):
            raise ValueError("ID must be string")

        if not isinstance(command_prefix, str):
            raise ValueError("Command_prefix must be a non-empty string")

        with sqlite3.connect("./memo.db", timeout=20.0) as db_connection:
            # First check if the guild_id exists
            check_query = """
                SELECT 1
                FROM guild_configs
                WHERE guild_id = ?
            """

            cursor = db_connection.execute(check_query, (guild_id,))
            if cursor.fetchone() is None:
                print(f"ERROR_LOG: Guild ID {guild_id} not found in database")
                return False

            # If guild exists, proceed with update
            update_query = """
                UPDATE
                    guild_configs
                SET
                    command_prefix = ?
                WHERE
                    guild_id = ?
            """

            db_connection.execute(
                update_query,
                (
                    command_prefix,
                    guild_id,
                ),
            )

            db_connection.commit()
            return True

    except Exception as e:
        print(f"ERROR_LOG: Unexpected error: {str(e)}")
        return False
