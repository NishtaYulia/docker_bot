from .connection import conn
from psycopg2 import OperationalError


def execute_query(query, connection=conn):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_message_table = """
CREATE TABLE IF NOT EXISTS message (
    id SERIAL PRIMARY KEY,
    message TEXT,
    userid INTEGER NOT NULL,
    message_time TIMESTAMP WITH TIME ZONE
) 
"""

execute_query(create_message_table)


