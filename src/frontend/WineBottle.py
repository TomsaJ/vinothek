import os.path

from src.backend.Database import Database
from src.frontend.IconAndImage import IconAndImage

database = Database()
iconAndImage = IconAndImage()

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
                            <img src="{iconAndImage.getCountry(vino[7])}" width="18px" height="18px" >
                            <br>
                            <br>
                            <p>{vino[8]}</p>
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
            ("Herkunft", getInfo[0][2], iconAndImage.getCountry(getInfo[0][2])),
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
        bottle = database.getWineInfo(wine)
        if bottle[0][6] is None or bottle[0][6] == '':
            bottle = '<img src="/static/resource/wine-bottle/default/wine-bottle.png" width="128px" height="128px"><h1>' + wine + '</h1><h2 style="margin-bottom: 50px">' + bottle[0][3] + '</h2>'
        else:
            bottle = '<img src="/static/resource/wine-bottle/custom/' + bottle[0][6] + '" width="128px" height="128px"><h1>' + wine + '</h1><h2 style="margin-bottom: 50px">' + bottle[0][3] + '</h2>'
        return bottle

    def getRecommendation(self, wine):
        # SQL-Ergebnisse abrufen
        recommendation = database.getRecommendation(wine)  # Liste mit Tupel, z.B. [('Nudel, Rind',)]

        # String aus dem Tupel extrahieren und in eine Liste umwandeln
        recommendation_list = recommendation[0][0].split(',')  # ['Nudel', 'Rind']

        # HTML-Tabelle als String vorbereiten
        html_table = """
        <div style="overflow-x: auto;">
            <table style="width: 100%; min-width: 100%; border-collapse: collapse; table-layout: fixed;">
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
            f'<th style="padding: 8px; text-align: center; width: 50%;"><img src="{iconAndImage.getFood(item)}" alt="{item}" width="100px" height="100px"></th>'
            for item in recommendation_list
        )
        labels = ''.join(
            f'<td style="padding: 8px; text-align: center; width: 50%;">{item}</td>'
            for item in recommendation_list
        )

        # HTML zusammenfügen
        html_table = html_table.format(images=images, labels=labels)

        # Rückgabe der HTML-Tabelle als String
        return html_table


    def getTasteCharacteristics(self, wine):
        row = database.getTasteCharacteristics(wine)
        if row != None:
            htmlContent = (f"<tr>"
                       f"<td>Leicht</td>"
                       f"<td><div class='slider-container'><div class='slider-thumb' style='left: calc("+str(row[0][2]*10)+"% - 50px);'></div></div></td>"
                       f"<td>Kräftig</td>"
                       f"</tr>")

            htmlContent += (f"<tr>"
                       f"<td>Flexibel</td>"
                       f"<td><div class='slider-container'><div class='slider-thumb' style='left: calc(" + str(
                    row[0][3] * 10) + "% - 50px);'></div></div></td>"
                                                     f"<td>Tranninhalting</td>"
                                                     f"</tr>")
            htmlContent += (f"<tr>"
                        f"<td>Trocken</td>"
                        f"<td><div class='slider-container'><div class='slider-thumb' style='left: calc(" + str(
                                row[0][4] * 10) + "% - 50px);'></div></div></td>"
                                                  f"<td>Süß</td>"
                                                  f"</tr>")

            htmlContent += (f"<tr>"
                        f"<td>Sanft</td>"
                        f"<td><div class='slider-container'><div class='slider-thumb' style='left: calc(" + str(
                                row[0][5] * 10) + "% - 50px);'></div></div></td>"
                                                  f"<td>Säure</td>"
                                                  f"</tr>")
        else:
            htmlContent = (f"<tr>"
                            f"<td></td>"
                            f"<td>Keine Geschmacksmerkmale vorhanden</td>"
                            f"<td></td>"
                            f"</tr>")
        return htmlContent

