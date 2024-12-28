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

    def getWineInfo(self, wine):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT Produkt.* FROM Produkt WHERE Produkt.Name = %s;",
            (wine,)
        )

        row = cursor.fetchall()
        return row

    def getSpezification(self, wine):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT Spezifikation.* FROM Spezifikation WHERE Spezifikation.P_ID = %s;",
            (wine,)
        )
        row = cursor.fetchall()
        return row

    def getRecommendation(self, wine):
        id = self.getWineInfo(wine)
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT Spezifikation.Recommendation FROM Spezifikation WHERE Spezifikation.P_ID = %s;",
            (id[0][0],)
        )
        row = cursor.fetchall()
        return row
