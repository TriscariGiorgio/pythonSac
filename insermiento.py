from creazioneDB import connection

import csv

from funzioniDB import inserisci_dati

with open(r"C:\Users\Giorgio\OneDrive\Desktop\DAITV_pulito_1.csv", encoding="iso-8859-1") as f:
    reader = csv.reader(f, delimiter=";")
    next(reader)
    reader = list(reader)

lista_campi_film = ["titolo", "anno"]
lista_film = []

for i in range(len(reader)):
    lista_film.append((reader[i][1], reader[i][2]))

inserisci_dati(connection, "film", lista_film, lista_campi_film)