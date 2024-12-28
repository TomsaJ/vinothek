import os
import mysql.connector

class Database:
    def __init__(self):
        self.host = os.getenv('DB_HOST', 'localhost')
        self.port = int(os.getenv('DB_PORT', 3306))
        self.user = os.getenv('DB_USER', 'vino')
        self.password = os.getenv('DB_PASSWORD', 'vino')
        self.database = os.getenv('DB_NAME', 'Vino')
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
        cursor.execute("SELECT Produkt.*, Spezifikation.Herkunft, Spezifikation.Jahr FROM Produkt LEFT "
                       "JOIN Spezifikation ON Spezifikation.P_ID = Produkt.ID;")
        rows = cursor.fetchall()
        return rows

    def getHouseWines(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT Produkt.*, Spezifikation.Herkunft, Spezifikation.Jahr FROM Produkt LEFT "
            "JOIN Spezifikation ON Spezifikation.P_ID = Produkt.ID "
            "WHERE Produkt.K_ID = 0; ")
        rows = cursor.fetchall()
        return rows
