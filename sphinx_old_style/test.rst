Test de carte
=============

.. raw:: html

     <div class="post-content inarticle">
     <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.4/leaflet.css" />
     <!--[if lte IE 8]></p>
     <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet-0.4/leaflet.ie.css" />
     < ![endif]--><br />
     <script src="http://cdn.leafletjs.com/leaflet-0.4/leaflet.js"></script></p>
     <h2>À quoi servent les groupes de maison</h2>
     <p>Les groupes de maison sont un espace de confiance où un petit nombre de personne se retrouve sur une base régulière pour partager, prier, s&#8217;encourager. Il s&#8217;agit d&#8217;un lieu de croissance privilégié, dans lequel chacun contribue au bien des autres.</p>
     <h2>Rejoindre un groupe</h2>
     <p>Vous souhaitez rejoindre un groupe de maison existant, ou en créer un nouveau?<br />
     Pour toute information, prenez contact avec <a href="http://corsiercorseaux.eerv.ch/contacts/?type=wp&#038;userid=93">Pierre Bader</a>.</p>
     <p>Voici les groupes existants liés à notre paroisse:</p>
     <div id="map" style="height: 400px;"></div>
     <ul>
     <li><b>N° 1:</b> Groupe mixte, <i>2ème et 4ème Mardi 19h30-22h</i> <a href="#map" onClick="groupe1.openPopup();">(carte)</a></li>
     <li><b>N° 2:</b> Groupe femmes, <i>1x15j Jeudi 9h-10h30</i> <a href="#map" onClick="groupe2.openPopup();">(carte)</a></li>
     <li><b>N° 3:</b> Groupe hommes, <i>Les Mardi 7h30-8h</i> <a href="#map" onClick="groupe3.openPopup();">(carte)</a></li>
     <li><b>N° 4:</b> Groupe lecture de la Bible, <i>1x15j Mercredi, 20h-22h</i> <a href="#map" onClick="groupe4.openPopup();">(carte)</a></li>
     <li><b>N° 5:</b> Groupe mixte, <i>Les Lundi 20h-22h, 1x15j Mercredi</i> <a href="#map" onClick="groupe5.openPopup();">(carte)</a></li>
     <li><b>N° 6:</b> Groupe femmes, <i>8h15-9h15</i> <a href="#map" onClick="groupe6.openPopup();">(carte)</a></li>
     <li><b>N° 7:</b> Groupe mixte, <i>1x15j Mercredi 20h-22h</i> <a href="#map" onClick="groupe7.openPopup();">(carte)</a></li>
     <li><b>N° 8:</b> Groupe mixte, <i>Les Jeudi 20h-22h</i> <a href="#map" onClick="groupe8.openPopup();">(carte)</a></li>
     <li><b>N° 9:</b> Groupe mixte, <i>Les Lundi 20h30-22h</i> <a href="#map" onClick="groupe9.openPopup();">(carte)</a></li>
     <li><b>N° 10:</b> Groupe Mères en contact, <i>Les Mardi 8h30-9h30</i> <a href="#map" onClick="groupe10.openPopup();">(carte)</a></li>
     <li><b>N° 11:</b> Groupe mixte, <i>Les Jeudi 20h-22h</i> <a href="#map" onClick="groupe11.openPopup();">(carte)</a></li>
     <li><b>N° 12:</b> Groupe mixte, <i>Jour à définir 20h</i> <a href="#map" onClick="groupe12.openPopup();">(carte)</a></li>
     <li><b>N° 13:</b> Groupe femmes, <i>Les Lundi 14h-16h</i> <a href="#map" onClick="groupe13.openPopup();">(carte)</a></li>
     <li><b>N° 14:</b> Groupe famille, <i>À définir</i> <a href="#map" onClick="groupe14.openPopup();">(carte)</a></li>
     <li><b>N° 15:</b> Groupe mixte, <i>Les Mardi 18h30</i> <a href="#map" onClick="groupe15.openPopup();">(carte)</a></li>
     <li><b>N° 16:</b> Groupe hommes, <i>Les Mardi 6h30-7h</i> <a href="#map" onClick="groupe16.openPopup();">(carte)</a></li>
     <li><b>N° 17:</b> Groupe des jeunes post-Jp, <i>1x15j Mercredi 20h</i> <a href="#map" onClick="groupe17.openPopup();">(carte)</a></li>
     <li><b>N° 18:</b> Groupe jeunes filles, <i>Les Jeudi 16h30</i> <a href="#map" onClick="groupe18.openPopup();">(carte)</a></li>
     <li><b>N° 19:</b> Groupe mixte jeunes, <i>A définir</i> <a href="#map" onClick="groupe19.openPopup();">(carte)</a></li>
     <li><b>N° 20:</b> Groupe mixte, <i>Infos à venir</i> <a href="#map" onClick="groupe20.openPopup();">(carte)</a></li>
     <li><b>N° 21:</b> Groupe mixte, <i>Infos à venir</i> <a href="#map" onClick="groupe20.openPopup();">(carte)</a></li>
     </ul>
     <p><script>
     //initialisation de la carte
     var map = L.map('map').setView([46.470209,6.841719], 14);
     //Utilisation d'OSM
     L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
     attribution: 'Map data © OpenStreetMap contributors',
     maxZoom: 18
     }).addTo(map);
     //Contour des villages
     var polygon = L.polygon([
             [46.4689827, 6.8366943],
             [46.468973, 6.8455377],
             [46.4715583, 6.8490258],
             [46.4730752, 6.8531311],
             [46.4774836, 6.8572219],
             [46.4793564, 6.860701],
             [46.4812692, 6.8659085],
             [46.4833834, 6.8680532],
             [46.4848324, 6.870719],
             [46.4868538, 6.8742701],
             [46.4896428, 6.8764541],
             [46.4937426, 6.8805933],
             [46.4970301, 6.8836083],
             [46.4994175, 6.8859415],
             [46.5027258, 6.8900341],
             [46.505595, 6.8936271],
             [46.5075564, 6.8956815],
             [46.5129585, 6.8960261],
             [46.5189636, 6.8971257],
             [46.5192776, 6.895309],
             [46.5043069, 6.8724362],
             [46.4928901, 6.8577742],
             [46.4890186, 6.8575737],
             [46.4842625, 6.8538834],
             [46.4778413, 6.8468011],
             [46.4761283, 6.8430173],
             [46.4745582, 6.8396839],
             [46.4738159, 6.8341405],
             [46.4741378, 6.8280647],
             [46.4725534, 6.8200138],
             [46.4714518, 6.8139477],
             [46.4698365, 6.815528],
             [46.4695197, 6.8205234],
             [46.4677112, 6.8230908],
             [46.4684139, 6.8287617],
             [46.4687388, 6.8361246],
             [46.4689827, 6.8366943]
             ], {
     fillOpacity: 0.1
             }).addTo(map);
     //polygon.bindPopup("Territoire de la paroisse de Corseaux-Corsier.");
     //Groupes
     var groupe1 = L.marker([46.47073712773207, 6.835700258282698]).addTo(map);
     var groupe2 = L.marker([46.46687178123551, 6.865381721707204]).addTo(map);
     var groupe3 = L.marker([46.470381299164714, 6.841193027335058]).addTo(map);
     var groupe4 = L.marker([46.476026131454276, 6.825028227782561]).addTo(map);
     var groupe5 = L.marker([46.486563075731134, 6.841402529744104]).addTo(map);
     var groupe6 = L.marker([46.47249750852557, 6.845244624309322]).addTo(map);
     var groupe7 = L.marker([46.47102740720879, 6.82747470066716]).addTo(map);
     var groupe8 = L.marker([46.49107890408472, 6.874137109033098]).addTo(map);
     var groupe9 = L.marker([46.46663766713093, 6.863940549629111]).addTo(map);
     var groupe10 = L.marker([46.471074226334245, 6.82884789293025]).addTo(map);
     var groupe11 = L.marker([46.47012847219002, 6.827379528926152]).addTo(map);
     var groupe12 = L.marker([46.45445791493686, 6.860693773849812]).addTo(map);
     var groupe13 = L.marker([46.47261923487992, 6.8317438330494396]).addTo(map);
     var groupe14 = L.marker([46.470989951879424, 6.8256664375880405]).addTo(map);
     var groupe15 = L.marker([46.469360620104425, 6.83893609747691]).addTo(map);
     var groupe16 = L.marker([46.47143941413053, 6.832206095791469]).addTo(map);
     var groupe17 = L.marker([46.471982509398394, 6.834789328761637]).addTo(map);
     var groupe18 = L.marker([46.4697632755977, 6.8417912497070965]).addTo(map);
     var groupe19 = L.marker([46.48231363220039, 6.769766475820904]).addTo(map);
     var groupe20 = L.marker([46.468724,6.839651]).addTo(map);
     var groupe20 = L.marker([46.450277,6.866527]).addTo(map);
     //Popups
     groupe2.bindPopup("<b>N° 2:</b> Groupe femmes<br /><i>1x15j Jeudi 9h-10h30</i>");
     groupe3.bindPopup("<b>N° 3:</b> Groupe hommes<br /><i>Les Mardi 7h30-8h</i>");
     groupe4.bindPopup("<b>N° 4:</b> Groupe lecture de la Bible<br /><i>1x15j Mercredi, 20h-22h</i>");
     groupe5.bindPopup("<b>N° 5:</b> Groupe mixte<br /><i>Les Lundi 20h-22h, 1x15j Mercredi</i>");
     groupe6.bindPopup("<b>N° 6:</b> Groupe femmes<br /><i>8h15-9h15</i>");
     groupe7.bindPopup("<b>N° 7:</b> Groupe mixte<br /><i>1x15j Mercredi 20h-22h</i>");
     groupe8.bindPopup("<b>N° 8:</b> Groupe mixte<br /><i>Les Jeudi 20h-22h</i>");
     groupe9.bindPopup("<b>N° 9:</b> Groupe mixte<br /><i>Les Lundi 20h30-22h</i>");
     groupe10.bindPopup("<b>N° 10:</b> Groupe Mères en contact<br /><i>Les Mardi 8h30-9h30</i>");
     groupe11.bindPopup("<b>N° 11:</b> Groupe mixte<br /><i>Les Jeudi 20h-22h</i>");
     groupe12.bindPopup("<b>N° 12:</b> Groupe mixte<br /><i>Jour à définir 20h</i>");
     groupe13.bindPopup("<b>N° 13:</b> Groupe femmes<br /><i>Les Lundi 14h-16h</i>");
     groupe14.bindPopup("<b>N° 14:</b> Groupe famille<br /><i>À définir</i>");
     groupe15.bindPopup("<b>N° 15:</b> Groupe mixte<br /><i>Les Mardi 18h30</i>");
     groupe16.bindPopup("<b>N° 16:</b> Groupe hommes<br /><i>Les Mardi 6h30-7h</i>");
     groupe17.bindPopup("<b>N° 17:</b> Groupe des jeunes post-Jp<br /><i>1x15j Mercredi 20h</i>");
     groupe18.bindPopup("<b>N° 18:</b> Groupe jeunes filles<br /><i>Les Jeudi 16h30</i>");
     groupe19.bindPopup("<b>N° 19:</b> Groupe mixte jeunes<br /><i>A définir</i>");
     groupe20.bindPopup("<b>N° 20:</b> Groupe mixte<br /><i>Infos à venir</i>");
     groupe21.bindPopup("<b>N° 21:</b> Groupe mixte<br /><i>Infos à venir</i>");
     groupe1.bindPopup("<b>N° 1:</b> Groupe mixte<br /><i>2éme et 4éme Mardi 19h30-22h</i>");
     </script></p>
     
     </div>
