import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


con = psycopg2.connect("user=postgres password='postgres' host=bot_db port=5432")
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = con.cursor()
cursor.execute("CREATE DATABASE dbbot;")

