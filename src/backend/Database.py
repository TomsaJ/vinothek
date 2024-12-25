import os
import mysql.connector

class Database:
    def __init__(self):
        self.host = os.getenv('DB_HOST', 'localhost')
        self.port = int(os.getenv('DB_PORT', 3306))
        self.user = os.getenv('DB_USER', '')
        self.password = os.getenv('DB_PASSWORD', '')
        self.database = os.getenv('DB_NAME', '')
        self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def getAllWines(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Produkt")
        rows = cursor.fetchall()
        return rows
