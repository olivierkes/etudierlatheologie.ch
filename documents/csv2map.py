import sys, csv, jinja2

template="""
<link href="http://cdn.leafletjs.com/leaflet-0.4/leaflet.css" rel="stylesheet" />
<!--[if lte IE 8]>
<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.4/leaflet.ie.css" />
< ![endif]-->
<script type="text/javascript" src="http://cdn.leafletjs.com/leaflet-0.4/leaflet.js"></script>
<style type="text/css"><!--
#map img {padding: 1px; border: 0; float: right;}
--></style>
<div id="map" style="height: 400px;"></div>
<script>
     //initialisation de la carte
     var map = L.map('map').setView([48.070738,6.183471], 6);
     //Utilisation d'OSM
     L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
     attribution: 'Map data © OpenStreetMap contributors',
     maxZoom: 18
     }).addTo(map);
     //Ajout d'une deuxième icône
     var catho = L.icon({
    iconUrl: 'http://www.theologeek.ch/elt/assets/marker-red.png',
    //iconRetinaUrl: 'my-icon@2x.png',
    iconSize: [25, 40],
    iconAnchor: [12, 40],
    popupAnchor: [1, -34]
});
{% for d in data -%}
var fac{{ loop.index }} = L.marker([{{ d.geo }}]{% if d.theologie == "Catholique" %}, {icon: catho}{% endif %}).addTo(map); 
fac{{ loop.index }}.bindPopup('<b>{{ d.faculte|e }}</b><br />{% if d.theologie %}<i>{{ d.theologie|e }}</i><br />{% endif %}{{ d.universite|e }} - {{ d.ville|e }}<br /><a href="#">présentation</a> | <a href="{{ d.web }}" target="_blank">site web</a>');
{% endfor -%}
</script>
"""

# Si une base est donnée en argument, on la prend.
# Sinon on suppose que le script n'a pas bougé
if len(sys.argv) >= 2:
    db = sys.argv[1]
else:
    db = 'facultes.csv'

# En essaie d'ouvrir le fichier choisi
try:
    f = open(db, 'r')

except IOError:
    print("Fichier introuvable")

else: 
    # On fait du CSV un dictionnaire
    data = csv.DictReader(f, delimiter="\t")
    
    page = jinja2.Template(template)
    
    # On passe directement le dictionnaire courant à Jinja
    print(page.render(locals()))
    
    f.close()
