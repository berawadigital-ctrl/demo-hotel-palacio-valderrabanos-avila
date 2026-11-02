# Contenido de la demo Hotel Palacio Valderrábanos (Ávila) (es/en/fr/de). Hechos de hotelpalaciovalderrabanos.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Habitaciones dobles, triples y familiares','Suites con vistas a la catedral'],'en':['Double, triple and family rooms','Suites with cathedral views'],'fr':['Chambres doubles, triples et familiales','Suites avec vue sur la cathédrale'],'de':['Doppel-, Dreibett- und Familienzimmer','Suiten mit Blick auf die Kathedrale']}
RD={
'es':['Clásicas, plus o económicas, con aire acondicionado, calefacción, wifi gratuito, TV y baño privado con secador. Algunas con cama king size y vistas a la catedral.','De corte clásico, con zona de estar, dos TV de pantalla plana, sofá y cafetera. Tres suites distintas: «Duque Suarez», «Teresa de Jesús» y «Torreón».'],
'en':['Classic, plus or economy, with air conditioning, heating, free wifi, TV and private bathroom with hairdryer. Some with a king-size bed and cathedral views.','Classic in style, with a sitting area, two flat-screen TVs, sofa and coffee maker. Three different suites: «Duque Suarez», «Teresa de Jesús» and «Torreón».'],
'fr':['Classiques, plus ou économiques, avec climatisation, chauffage, wifi gratuit, TV et salle de bains privée avec sèche-cheveux. Certaines avec lit king size et vue sur la cathédrale.','De style classique, avec coin salon, deux TV à écran plat, canapé et cafetière. Trois suites différentes : «Duque Suarez», «Teresa de Jesús» et «Torreón».'],
'de':['Klassik, Plus oder Economy, mit Klimaanlage, Heizung, kostenlosem WLAN, TV und eigenem Bad mit Föhn. Einige mit Kingsize-Bett und Blick auf die Kathedrale.','Im klassischen Stil, mit Sitzbereich, zwei Flachbildfernsehern, Sofa und Kaffeemaschine. Drei verschiedene Suiten: «Duque Suarez», «Teresa de Jesús» und «Torreón».']}
ART={
'hero':('skyline',5511,['#20262b','#a8844f','#efe3cc','#59606a','#373d44','#171b1f']),
'intro':('arches',5512,['#f1ede6','#faf8f3','#6e5430','#545b63','#25292d']),
'r1':('columns',5521,['#ece7de','#d4b27e','#6e5430','#545b63','#25292d']),
'r2':('arches',5522,['#20262b','#b38f58','#f1e5cf','#626973','#3c434a','#191d21']),
'g1':('hills',5531,['#e6e2da','#e9dbc3','#d4b27e','#8e8a86','#66625f','#423f3d']),
'g2':('skyline',5532,['#20262b','#a8844f','#efe3cc','#59606a','#373d44','#171b1f']),
'g3':('waves',5533,['#f1ede6','#faf8f3','#6e5430','#545b63','#25292d']),
'g4':('columns',5534,['#20262b','#b38f58','#f1e5cf','#626973','#3c434a','#191d21'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Palacio Valderrábanos · Palacio del siglo XIV junto a la Catedral de Ávila',see_rooms='Ver habitaciones',hero_k='Ávila · Plaza de la Catedral, 9',hero_t='Esencia del siglo XIV',hero_s='Un palacio junto a la Catedral de Ávila, con interiores modernos que conservan su historia.',
 intro_t='Diseño, arte e historia',intro_p1='El Hotel Palacio Valderrábanos está junto a la Catedral de Ávila, una situación que permite disfrutar de la ciudad sin grandes desplazamientos. Ofrece wifi gratuito en todo el edificio.',
 intro_p2='Tiene varias zonas de estar, salones para eventos y La Crestería y el Café del Hotel, donde tomar algo con vistas a la catedral.',
 stats=['80 habitaciones','Junto a la catedral','Recepción 24 horas','Pet friendly'],nav_rooms='Habitaciones',rooms_t='Habitaciones y suites',rooms_s='80 habitaciones espaciosas y confortables, y habitaciones adaptadas para movilidad reducida.',
 svcs=['Recepción 24 horas','Wifi gratuito en todo el edificio','Admite mascotas','Habitaciones adaptadas para movilidad reducida','Tres salones para eventos con luz natural','Seguro de cancelación incluido en tarifas no reembolsables'],
 loc_p='Plaza de la Catedral, 9 · 05001 Ávila. Teléfono: +34 920 211 023. Correo: reservas@hotelpalaciovalderrabanos.com.',
 chips=['¿Qué habitaciones tenéis?','¿Hay parking?','¿Admitís mascotas?','¿Cómo reservo?']),
'en':dict(title='Hotel Palacio Valderrábanos · 14th-century palace next to Ávila Cathedral',see_rooms='See rooms',hero_k='Ávila · Plaza de la Catedral, 9',hero_t='The essence of the 14th century',hero_s='A palace next to Ávila Cathedral, with modern interiors that keep its history.',
 intro_t='Design, art and history',intro_p1='Hotel Palacio Valderrábanos stands next to Ávila Cathedral, a location that lets you enjoy the city without long journeys. It offers free wifi throughout the building.',
 intro_p2='It has several lounges, event rooms and La Crestería and the Hotel Café, where you can have a drink with views of the cathedral.',
 stats=['80 rooms','Next to the cathedral','24-hour reception','Pet friendly'],nav_rooms='Rooms',rooms_t='Rooms and suites',rooms_s='80 spacious and comfortable rooms, and rooms adapted for reduced mobility.',
 svcs=['24-hour reception','Free wifi throughout the building','Pets allowed','Rooms adapted for reduced mobility','Three event rooms with natural light','Cancellation insurance included in non-refundable rates'],
 loc_p='Plaza de la Catedral, 9 · 05001 Ávila. Phone: +34 920 211 023. Email: reservas@hotelpalaciovalderrabanos.com.',
 chips=['Which rooms do you have?','Is there parking?','Do you allow pets?','How do I book?']),
'fr':dict(title='Hotel Palacio Valderrábanos · Palais du XIVe siècle à côté de la cathédrale d’Ávila',see_rooms='Voir les chambres',hero_k='Ávila · Plaza de la Catedral, 9',hero_t='L’essence du XIVe siècle',hero_s='Un palais à côté de la cathédrale d’Ávila, aux intérieurs modernes qui gardent son histoire.',
 intro_t='Design, art et histoire',intro_p1='L’Hotel Palacio Valderrábanos se trouve à côté de la cathédrale d’Ávila, un emplacement qui permet de profiter de la ville sans longs trajets. Wifi gratuit dans tout le bâtiment.',
 intro_p2='Il dispose de plusieurs salons, de salles pour événements et de La Crestería et du Café de l’hôtel, pour prendre un verre avec vue sur la cathédrale.',
 stats=['80 chambres','À côté de la cathédrale','Réception 24 h/24','Animaux acceptés'],nav_rooms='Chambres',rooms_t='Chambres et suites',rooms_s='80 chambres spacieuses et confortables, et des chambres adaptées aux personnes à mobilité réduite.',
 svcs=['Réception 24 h/24','Wifi gratuit dans tout le bâtiment','Animaux acceptés','Chambres adaptées à la mobilité réduite','Trois salles pour événements à la lumière naturelle','Assurance annulation incluse dans les tarifs non remboursables'],
 loc_p='Plaza de la Catedral, 9 · 05001 Ávila. Téléphone : +34 920 211 023. E-mail : reservas@hotelpalaciovalderrabanos.com.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il un parking ?','Acceptez-vous les animaux ?','Comment réserver ?']),
'de':dict(title='Hotel Palacio Valderrábanos · Palast aus dem 14. Jahrhundert neben der Kathedrale von Ávila',see_rooms='Zimmer ansehen',hero_k='Ávila · Plaza de la Catedral, 9',hero_t='Die Essenz des 14. Jahrhunderts',hero_s='Ein Palast neben der Kathedrale von Ávila, mit modernen Räumen, die seine Geschichte bewahren.',
 intro_t='Design, Kunst und Geschichte',intro_p1='Das Hotel Palacio Valderrábanos liegt neben der Kathedrale von Ávila – so lässt sich die Stadt ohne weite Wege genießen. Kostenloses WLAN im ganzen Gebäude.',
 intro_p2='Es gibt mehrere Aufenthaltsbereiche, Veranstaltungssäle sowie La Crestería und das Hotelcafé, wo man mit Blick auf die Kathedrale etwas trinken kann.',
 stats=['80 Zimmer','Neben der Kathedrale','Rezeption rund um die Uhr','Haustiere willkommen'],nav_rooms='Zimmer',rooms_t='Zimmer und Suiten',rooms_s='80 geräumige und komfortable Zimmer sowie Zimmer für Menschen mit eingeschränkter Mobilität.',
 svcs=['Rezeption rund um die Uhr','Kostenloses WLAN im ganzen Gebäude','Haustiere erlaubt','Zimmer für eingeschränkte Mobilität','Drei Veranstaltungssäle mit Tageslicht','Reiserücktrittsversicherung in nicht erstattbaren Tarifen inklusive'],
 loc_p='Plaza de la Catedral, 9 · 05001 Ávila. Telefon: +34 920 211 023. E-Mail: reservas@hotelpalaciovalderrabanos.com.',
 chips=['Welche Zimmer gibt es?','Gibt es einen Parkplatz?','Sind Haustiere erlaubt?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://www.hotelpalaciovalderrabanos.com/booking1?language=SPANISH'
RE='https://www.hotelpalaciovalderrabanos.com/booking1?language=ENGLISH'
BOOK=dict(mode='engine',url=dict(es=R,en=RE,fr=RE,de=RE))
D=dict(name='Hotel Palacio Valderrábanos',ac='#20262b',ac2='#6e5430',ac2_a11y='#5a4426',book=BOOK,around=[],foot=FOOT,
 address='Plaza de la Catedral, 9 · 05001 Ávila',phones=['+34 920 211 023'],emails=['reservas@hotelpalaciovalderrabanos.com'],maps='Hotel Palacio Valderrábanos, Plaza de la Catedral 9, 05001 Ávila',t=T)
META=dict(repo='demo-hotel-palacio-valderrabanos-avila',name='Hotel Palacio Valderrábanos',legal_name='BELTRAN MENESES SL, NIF B83965061 (aviso legal de su web)',registry_ids=['B83965061'],
 url='https://www.hotelpalaciovalderrabanos.com/',domain='hotelpalaciovalderrabanos.com',municipality='Ávila',province='Ávila',sector='hotel en un palacio del siglo XIV junto a la Catedral de Ávila',
 read_at='2026-11-02T09:07:00+01:00',created_at='2026-11-02T09:06:00+01:00',built_at='2026-11-02T09:25:00+01:00',audit_date='2026-11-02T09:07:00+01:00',
 rating=dict(value=4.4,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Hotel+Palacio+Valderr%C3%A1banos/@40.6557102,-4.6981046,17z'),
 book=dict(mode='engine',url=R,note='motor propio Paraty de su web (formulario Reservar -> /booking1): https://www.hotelpalaciovalderrabanos.com/booking1?language=SPANISH, HTTP 200 y muestra el calendario de reserva (02/11/2026 09:10). ES en espanol; EN/FR/DE a la version inglesa del mismo motor.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Tenéis suites?','K02'),('¿Qué tienen las habitaciones?','K03'),('¿A qué hora es la entrada?','K04'),('¿Hay parking?','K05'),('¿Dónde estáis?','K06'),('¿Cómo reservo?','K07'),('¿Podéis confirmarme disponibilidad para mañana?','K07'),('¿Admitís mascotas?','K08'),('¿Tenéis salones para eventos?','K09'),('¿Qué ver en Ávila?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Hay cafetería?','K12'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('Do you have suites?','K02'),('What do the rooms include?','K03'),('What time is check-in?','K04'),('Is there parking?','K05'),('Where are you?','K06'),('How do I book?','K07'),('Can you confirm availability for tomorrow?','K07'),('Do you allow pets?','K08'),('Do you have event rooms?','K09'),('What to see in Ávila?','K10'),('What is your phone number?','K11'),('Is there a café?','K12'),('How much is a night?',None),('Do you have a pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Avez-vous des suites ?','K02'),('Que comprennent les chambres ?','K03'),('À quelle heure est l’arrivée ?','K04'),('Y a-t-il un parking ?','K05'),('Où êtes-vous ?','K06'),('Comment réserver ?','K07'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K07'),('Acceptez-vous les animaux ?','K08'),('Avez-vous des salles pour événements ?','K09'),('Que voir à Ávila ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Y a-t-il un café ?','K12'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Haben Sie Suiten?','K02'),('Was bieten die Zimmer?','K03'),('Wann ist der Check-in?','K04'),('Gibt es einen Parkplatz?','K05'),('Wo liegt das Hotel?','K06'),('Wie kann ich buchen?','K07'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K07'),('Sind Haustiere erlaubt?','K08'),('Haben Sie Veranstaltungssäle?','K09'),('Was kann man in Ávila besichtigen?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Gibt es ein Café?','K12'),('Was kostet eine Nacht?',None),('Haben Sie einen Pool?',None)]}
