FALLBACK_ASK = "eh mo, ti serve altro?"
DAY_OF_THE_WEEK = {
    "Mon": "Lunedì",
    "Tue": "Martedì",
    "Wed": "Mercoledì",
    "Thu": "Giovedì",
    "Fri": "Venerdì",
    "Sat": "Sabato",
    "Sun": "Domenica"
}
DAYS_TO_ADD = {
    "oggi": 0,
    "domani": 1,
    "dopo domani": 2,
    "dopodomani": 2,
    "ieri": -1,
    "l'altro ieri": -2,
}
# AIRING_ANIME = [
#     {
#         "id": 1,
#         "name": "tsukimichi - moonlit fantasy",
#         "descr": "Makoto Misumi era solo un adolescente medio che all'improvviso fu convocato in un altro mondo come un eroe. Ma la dea di questo mondo lo definì brutto e gli tolse il suo status di eroe costringendolo a rimanere li in disparte ai bordi di quel mondo. Cosi' lui decide di vivere la sua esperienza al 100%. Questa e' la storia.",
#         "genere": "Isekai",
#         "airing_day": "Mon",
#         "season": "2",
#         "episode": "8",
#         "rating": 4.9,
#         "follower": 72200
#     },
#     {
#         "id": 2,
#         "name": "classroom of the elite",
#         "descr": "Ayanokoji Kiyotaka sta per cominciare il suo percorso scolastico presso il 'Liceo per la formazione di alto livello di Tokyo'. Agli studenti di tale scuola, alla fine dei corsi, è garantita l'ammissione al college scelto o verrà trovato lavoro. Si accorge subito che non e' un normale liceo e che la sua non e' una classe qualunque.",
#         "genere": "Gakuen",
#         "airing_day": "Wed",
#         "season": "3",
#         "episode": "9",
#         "rating": 4.8,
#         "follower": 106700
#     },
#     {
#         "id": 3,
#         "name": "metallic rouge",
#         "descr": "In un mondo in cui gli umani coesistono con gli androidi chiamati Nean, un gruppo noto come Immortal Nine si ribella alla società. Incaricati di eliminare i rivoltosi, un Nean di nome Rouge Redstar (alias Metal Rouge) e l'investigatrice Naomi Orthmann si recano su Marte per rintracciarli.",
#         "genere": "Cyber Punk",
#         "airing_day": "Wed",
#         "season": "1",
#         "episode": "8",
#         "rating": 4.5,
#         "follower": 6600
#     },
#     {
#         "id": 4,
#         "name": "the witch and the beast",
#         "descr": "Guideau è una giovane donna maledetta da una strega, costretta a portare con sé un oscuro segreto. Ashaf è un uomo alto con una bara legata alla schiena e segreti non ancora svelati. In un dark fantasy pieno di avventura, riusciranno gli improbabili eroi a trovare la vendetta contro le streghe?",
#         "genere": "Dark Fantasy",
#         "airing_day": "Thu",
#         "season": "1",
#         "episode": "8",
#         "rating": 4.7,
#         "follower": 6700
#     },
#     {
#         "id": 5,
#         "name": "frieren - oltre la fine del viaggio",
#         "descr": "Frieren è una maga che fa parte della squadra di eroi che ha sconfitto il re dei demoni. Essendo un'elfa, per lei i dieci anni passati con gli altri eroi rappresentano soltanto un piccolo frammento della sua lunga vita. Ora, Frieren riflette sul significato di quelle memorie e sui vari sentimenti che prova a riguardo.",
#         "genere": "Fantasy Drama Adventure",
#         "airing_day": "Fri",
#         "season": "1",
#         "episode": "26",
#         "rating": 4.9,
#         "follower": 86600
#     },
#     {
#         "id": 6,
#         "name": "firefighters daigo ",
#         "descr": "",
#         "genere": "Drama Adventure",
#         "airing_day": "Sat",
#         "season": "1",
#         "episode": "20",
#         "rating": 4.4,
#         "follower": 2400
#     },
#     {
#         "id": 7,
#         "name": "blue exorcist",
#         "descr": "",
#         "genere": "Fantasy Adventure",
#         "airing_day": "Sat",
#         "season": "3",
#         "episode": "9",
#         "rating": 4.7,
#         "follower": 26700
#     },
#     {
#         "id": 8,
#         "name": "mashle - magic and muscles",
#         "descr": "La storia si svolge in un mondo in cui esiste la magia e viene usata per qualunque occorrenza della vita quotidiana. Mash è un giovane che vive nascosto nella foresta e trascorre le giornate impegnandosi in potenti esercizi per il corpo. Non riesce a usare la magia ma vive comunque una vita pacifica con suo padre. Un giorno però la sua vita viene messa in pericolo; E poi guardatelo.",
#         "genere": "Fantasy Adventure",
#         "airing_day": "Sat",
#         "season": "2",
#         "episode": "12",
#         "rating": 4.8,
#         "follower": 101700
#     },
#     {
#         "id": 9,
#         "name": "solo leveling",
#         "descr": "Dopo essere stato brutalmente massacrato dai mostri in un dungeon di alto rango, Jinwoo è tornato con il Sistema, un programma che solo lui poteva vedere, che lo sta facendo salire di livello in ogni modo. Ora, è ispirato a scoprire i segreti dietro i suoi poteri e il dungeon che li ha generati.",
#         "genere": "Fantasy Adventure",
#         "airing_day": "Sat",
#         "season": "1",
#         "episode": "8",
#         "rating": 4.9,
#         "follower": 174300
#     },
#     {
#         "id": 10,
#         "name": "one piece",
#         "descr": "Monkey D. Rufy vuole diventare il Re dei Pirati, e non si lascerà fermare da niente e da nessuno! La rotta è segnata, le acque insidiose della Rotta Maggiore lo aspettano, e lui non si fermerà finché non avrà trovato il più grande tesoro al mondo, il leggendario One Piece!",
#         "genere": "Fantasy Adventure",
#         "airing_day": "Sun",
#         "season": "1",
#         "episode": "629",
#         "rating": 4.9,
#         "follower": 416500
#     },
#     {
#         "id": 11,
#         "name": "the fire hunter",
#         "descr": "Al di fuori delle barriere magiche si trova un mondo invaso da bestie infuocate note come Demoni di Fuoco, e gli unici che possono proteggere l'umanità sono i Cacciatori di Fuoco. Nei boschi oscuri dove si aggirano le bestie, Toko, un giovane abitante del villaggio, viene salvato dall'attacco di uno di questi abili inseguitori, Koshi. Ma il loro incontro non è stato casuale e un nuovo destino ha inizio.",
#         "genere": "Drama Fantasy Adventure",
#         "airing_day": "Sun",
#         "season": "1",
#         "episode": "21",
#         "rating": 4.4,
#         "follower": 2300
#     },
#     {
#         "id": 12,
#         "name": "shagiri la frontier",
#         "descr": "Rakuro Hizutome è un cacciatore di giochi brutti, che gioca con il soprannome di Sunraku fino a completarli al 100%. Dopo aver completato l'ennesimo titolo, per staccare un po' la spina si fa consigliare Shangri-La Frontier, un gioco VR full-dive di prima categoria con 30 milioni di giocatori registrati. Decide quindi di mettere alla prova tutte le abilità acquisite come esperto cacciatore di kusoge all'interno di un vero e proprio gioco.",
#         "genere": "Thriller Fantasy Adventure",
#         "airing_day": "Sun",
#         "season": "1",
#         "episode": "21",
#         "rating": 4.9,
#         "follower": 58500
#     },
#     {
#         "id": 13,
#         "name": "theatre of darkness",
#         "descr": "",
#         "genere": "Dark Thriller",
#         "airing_day": "Sun",
#         "season": "1",
#         "episode": "12",
#         "rating": 4.3,
#         "follower": 1600
#     }
# ]
