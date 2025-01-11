class IconAndImage:
    def __init__(self):
        self.path = f"/static/resource/"
        self.error = "/static/resource/404-fehler.png" # Ein Standard-Icon, falls kein Match gefunden wird

    def getCountry(self,country):
        # Mapping von Ländernamen zu den entsprechenden Dateinamen (alle in Kleinbuchstaben)
        country_icons = {
            "italien": "italy.png",
            "deutschland": "germany.png",
            "frankreich": "france.png",
            "spanien": "spain.png",
            # Weitere Länder können hier hinzugefügt werden
        }

        # Den übergebenen Ländernamen in Kleinbuchstaben umwandeln
        country = country.lower()

        # Überprüfen, ob das Land im Mapping existiert
        if country in country_icons:
            # Pfad zum Icon
            icon_path = f"/country/map/{country_icons[country]}"
            return self.path + icon_path
        else:
            # Fallback oder Fehlerbehandlung
            return self.error

    def getFood(self,food):
        # Mapping von Ländernamen zu den entsprechenden Dateinamen (alle in Kleinbuchstaben)
        food_icons = {
            "nudeln": "pasta.png",
            "rindfleisch": "steak.png",
            "softCheese": "softCheese.png",
            # Weitere Gerichte können hier hinzugefügt werden
        }

        food = food.lower()
        if food in food_icons:
            # Pfad zum Icon
            icon_path = f"food/{food_icons[food]}"
            return self.path + icon_path
        else:
            # Fallback oder Fehlerbehandlung
            return self.error