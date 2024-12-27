from src.backend.Database import Database

database = Database()

class WineBottle:

    def getBottle(self):
        rows = database.getAllWines()
        htmlContent = ''.join([
            self.getBottleHtml(vino)
            for vino in rows
        ])
        return htmlContent

    def getBottleHtml(self, vino):
        bottle = ''.join([
            f"""
                    <div class="flasche" onclick="location.href='/{vino[2]}'">
                        <div class="hals"></div>
                        <div class="körper"></div>
                        <div class="etikett">
                            <p>{vino[2]}</p>
                            <br>
                            <br><br>
                            <p>{vino[7]}</p>
                        </div>
                        <div class="korken"></div>
                    </div>
                    """])
        return bottle

    def getCountry(country):
        # Mapping von Ländernamen zu den entsprechenden Dateinamen (alle in Kleinbuchstaben)
        country_icons = {
            "italien": "italy.png",
            "deutschland": "germany.png",
            "frankreich": "france.png",
            "spanien": "spain.png",
            # Weitere Länder kannst du hier hinzufügen
        }

        # Den übergebenen Ländernamen in Kleinbuchstaben umwandeln
        country = country.lower()

        # Überprüfen, ob das Land in der Mapping-Liste existiert
        if country in country_icons:
            # Pfad zum Icon
            icon_path = f"/resource/country/{country_icons[country]}"
            return icon_path
        else:
            # Fallback oder Fehlerbehandlung
            return "/resource/404-fehler.png"  # Ein Standard-Icon, falls kein Match gefunden wird

