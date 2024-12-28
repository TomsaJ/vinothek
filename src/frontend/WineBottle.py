import os.path

from src.backend.Database import Database

database = Database()

class WineBottle:

    def getBottle(self):
        houseWine = database.getHouseWines()
        rows = database.getAllWines()
        htmlContent = ''.join([
                                  self.getBottleHtml(vino)
                                  for vino in houseWine
                              ] + [
                                  self.getBottleHtml(vino)
                                  for vino in rows
                              ])

        return htmlContent

    def getBottleHtml(self, vino):
        bottle = ''
        for _ in range(vino[5]):
            if vino[6] == None or os.path.exists(vino[6] == None):
                bottle += ''.join([
                f"""
                    <div class="flasche" onclick="location.href='/{vino[2]}'">
                        <div class="hals"></div>
                        <div class="körper"></div>
                        <div class="etikett">
                            <p>{vino[2]}</p>
                            <br>
                            <img src="{self.getCountry(vino[7])}" width="18px" height="18px" >
                            <br>
                            <br>
                            <!--<p>{vino[7]}</p>-->
                        </div>
                        <div class="korken"></div>
                    </div>
                    """])
            else:
                bottle += ''.join([f"""
                    <div onclick="location.href='/{vino[2]}'">
                        <img src='{vino[3]}' alt='{vino[4]}'></div>
                    </div>
                    """])
        return bottle

    def getInfo(self, wine):
        """
        Generiert eine HTML-Tabelle mit zwei Spalten, bei der zwischen Header, Bild und Inhalt
        abwechselnd Zeilen eingefügt werden (Header | Header, Bild | Bild, Inhalt | Inhalt).
        """
        db = Database()
        bottle = db.getWineInfo(wine)
        getInfo = db.getSpezification(bottle[0][0])

        # Spezifikationen extrahieren
        data = [
            ("Herkunft", getInfo[0][2], self.getCountry(getInfo[0][2])),
            ("Jahr", getInfo[0][3], "static/resource/icon/jahrgang.png"),
            ("Alkoholgehalt", f"{getInfo[0][4]} %" if getInfo[0][4] != '' else '', "static/resource/icon/wein.png"),
            ("Rebsorte", getInfo[0][5], "static/resource/icon/trauben.png"),
            ("Dekantieren", f"{getInfo[0][6]} min" if getInfo[0][6] != '' else '', "static/resource/icon/karaffe.png"),
            ("Temperatur", f"{getInfo[0][7]} C°" if getInfo[0][7] != '' else '', "static/resource/icon/thermometer.png"),

        ]

        # Filter: Nur Werte mit Daten berücksichtigen
        filtered_data = [(header, value, image) for header, value, image in data if value is not None and value != '']

        # HTML-Tabelle erstellen
        htmlContent = '<table class="product-table">'

        # Header, Bild und Inhalt für jedes Paar
        for i in range(0, len(filtered_data), 2):
            # Header-Zeile
            headers = "".join(f"<th ><p class='head'>{header}</p></th>" for header, _, _ in filtered_data[i:i + 2])
            htmlContent += f"<tr>{headers}</tr>"

            # Bild-Zeile (Bilder in zwei Spalten)
            images = "".join(f"<td><img src='{image}' width='48px' height='48px'/></td>" for _, _, image in filtered_data[i:i + 2])
            htmlContent += f"<tr>{images}</tr>"

            # Inhalt-Zeile
            values = "".join(f"<td>{value}</td>" for _, value, _ in filtered_data[i:i + 2])
            htmlContent += f"<tr>{values}</tr>"

        htmlContent += "</table>"
        return htmlContent

    def getWineTitel(self, wine):
        db = Database()
        bottle = db.getWineInfo(wine)
        if bottle[0][6] == '':
            bottle = '<img src="/static/resource/wine-bottle/default/wine-bottle.png" width="128px" height="128px"><h2>' + wine + '</h2><h3 style="margin-bottom: 50px">' + bottle[0][3] + '</h3>'
        else:
            bottle = '<img src="/static/resource/wine-bottle/custom/' + bottle[0][6] + '" width="128px" height="128px"><h2>' + wine + '</h2><h3 style="margin-bottom: 50px">' + bottle[0][3] + '</h3>'
        return bottle

    def getRecommendation(self, wine):
        # SQL-Ergebnisse abrufen
        recommendation = database.getRecommendation(wine)  # Liste mit Tupel, z.B. [('Nudel, Rind',)]

        # String aus dem Tupel extrahieren und in eine Liste umwandeln
        recommendation_list = recommendation[0][0].split(', ')  # ['Nudel', 'Rind']

        # HTML-Tabelle als String vorbereiten
        html_table = """
        <divstyle="overflow-x: auto;">
            <table  style="width: 100%; min-width: 700px;border-collapse: collapse;">
                <tr>
                    {images}
                </tr>
                <tr>
                    {labels}
                </tr>
            </table>
        </div>
        """

        images = ''.join(
            f'<th style="padding: 8px; text-align: center;"><img src="{self.getFood(item)}" alt="{item}" width="100px" height="auto"></th>'
            for item in recommendation_list
        )
        labels = ''.join(
            f'<td style="padding: 8px; text-align: center;">{item}</td>'
            for item in recommendation_list
        )

        # HTML zusammenfügen
        html_table = html_table.format(images=images, labels=labels)

        # Rückgabe der HTML-Tabelle als String
        return html_table

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
            icon_path = f"/static/resource/country/map/{country_icons[country]}"
            return icon_path
        else:
            # Fallback oder Fehlerbehandlung
            return "/resource/404-fehler.png"  # Ein Standard-Icon, falls kein Match gefunden wird

    def getFood(self,food):
        # Mapping von Ländernamen zu den entsprechenden Dateinamen (alle in Kleinbuchstaben)
        food_icons = {
            "nudeln": "nudeln.png",
            "rind": "steak.png",
            "frankreich": "france.png",
            "spanien": "spain.png",
            # Weitere Länder können hier hinzugefügt werden
        }

        # Den übergebenen Ländernamen in Kleinbuchstaben umwandeln
        food = food.lower()

        # Überprüfen, ob das Land im Mapping existiert
        if food in food_icons:
            # Pfad zum Icon
            icon_path = f"/static/resource/food/{food_icons[food]}"
            return icon_path
        else:
            # Fallback oder Fehlerbehandlung
            return "/static/resource/404-fehler.png"  # Ein Standard-Icon, falls kein Match gefunden wird



