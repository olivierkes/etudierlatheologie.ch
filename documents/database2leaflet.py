# Génère une carte leaflet à partir de la base de donnée en csv.
# Pas très propre, mais ça marche.
# usage:    python database2leaflet.py [database] > output.html
# preview:  http://www.theologeek.ch/elt/lieux-detudes/par-situation-geographique/


import sys, csv

include = """<link href="http://cdn.leafletjs.com/leaflet-0.4/leaflet.css" rel="stylesheet" />
<!--[if lte IE 8]>
<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.4/leaflet.ie.css" />
< ![endif]-->
<script type="text/javascript" src="http://cdn.leafletjs.com/leaflet-0.4/leaflet.js"></script>
<style type="text/css"><!--
#map img {padding: 1px; border: 0; float: right;}
--></style>"""



carte = """<div id="map" style="height: 400px;"></div>"""
     
     
     
initialisation_A = """<script>
     //initialisation de la carte
     var map = L.map('map').setView([_COORD_], 8);
     //Utilisation d'OSM
     L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
     attribution: 'Map data © OpenStreetMap contributors',
     maxZoom: 18
     }).addTo(map);\n"""

faculte = """var fac{0} = L.marker([{1}]).addTo(map); 
fac{0}.bindPopup('{2}');\n"""

initialisation_B = "</script>\n"


if __name__ == "__main__":
    
    # Si une base est donnée en argument, on la prend.
    # Sinon on suppose que le script n'a pas bougé
    if len(sys.argv) >= 2:
        db = sys.argv[1]
    else:
        db = 'facultes.csv'
    
    f = open(db, 'r')
    t = f.read()
    f.close()
    t = t.split("\n")

    for i in range(0, len(t)):
        # On sépare les tabs, et on vire les lignes vides
        if t[i]: t[i] = t[i].split("\t")
        else: t.pop(i)
    
    # page est la variable imprimée
    page = include + "\n" + carte + "\n" + initialisation_A
    
    # Pour calculer la moyenne des coordonnées (et centrer la carte)
    n=cy=cx=0
    
    for i in t[1:]:
        # Images des drapeaux des langues
        langue = ""
        if "Français" in i[7]: langue += '<img src="http://upload.wikimedia.org/wikipedia/commons/f/f3/Icons-flag-fr.png">'
        if "Allemand" in i[7]: langue += '<img src="http://upload.wikimedia.org/wikipedia/commons/b/b5/Icons-flag-de.png">'
        
        # La description dans le popup
        description = '<b>{0}</b><br><i>{5} {4}</i><br>{1}, {2}<br><a href="#">présentation</a> | <a href="{3}" target="_blank">site web</a>'.format(i[0], i[1], i[2], i[4], i[5], langue)
        
        # On ajoute le javascript nécessaire pour ajouter la fac
        page += faculte.format(t.index(i), i[6], description)
        
        #Calcul de la moyenne des coordonnées
        cx += float(i[6].split(",")[0])
        cy += float(i[6].split(",")[1])
        n += 1
        
    # Fermer le bousin
    page += initialisation_B
    
    # Calculer la moyenne des coordonnées, et convertir en string
    c = str(cx/n) + ", " + str(cy/n)
    
    # Retourner le bousin
    print(page.replace("_COORD_", c))
