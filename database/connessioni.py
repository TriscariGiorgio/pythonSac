from database.funzioniDB import *
from database.config import *

def crea_db():
    connection = create_server_connection(DB_HOST, DB_USER, DB_PASSWORD)
    esegui_query(connection, f"DROP DATABASE {DB_NAME}")
    create_database(connection, f"CREATE DATABASE {DB_NAME}")

    return connection

def crea_connessione_db():
    connection = create_db_connection(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    query = """SET GLOBAL max_allowed_packet = 268435456"""
    cursor = connection.cursor()
    cursor.execute(query)
    return connection
