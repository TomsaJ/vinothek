import mysql.connector
from mysql.connector import Error
import os


class Database:
    def connection(self):
        try:
            connection = mysql.connector.connect(
                host=os.getenv("DB_HOST", "localhost"),
                user=os.getenv("DB_USER", "admin"),
                passwd=os.getenv("DB_PASSWORD", "admin"),
                database=os.getenv("DB_NAME", "WS-AI-VS")
            )
            if connection.is_connected():
                return connection
            else:
                print("Connection failed")
                return None
        except Error as e:
            print(f"Fehler bei der Datenbankverbindung: {e}")
            return None