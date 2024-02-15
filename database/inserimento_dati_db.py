import csv

from connessioni import *

def insersci_dati_da_csv():
    connection=crea_connessione_db()

    with open(r"/dati/DAITV_pulito_1.csv", encoding="iso-8859-1") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        reader = list(reader)

    lista_campi_film = ["id","titolo", "anno"]
    lista_film = []

    for i in range(len(reader)):
        lista_film.append((reader[i][0],reader[i][1], reader[i][2]))

    inserisci_dati(connection, "film", lista_film, lista_campi_film)

    with open(r"/dati/UTENTI_NUOVO.csv", encoding="iso-8859-1") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        reader = list(reader)

    lista_campi_utente = ["eta","sesso","lavoro","domicilio","Provincia"]
    lista_utenti = []

    for i in range(len(reader)):
        lista_utenti.append((reader[i][2], reader[i][1],reader[i][4], reader[i][3],reader[i][5]))

    inserisci_dati(connection, "utenti", lista_utenti, lista_campi_utente)


    with open(r"/dati/ratings_edit.csv", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        reader = list(reader)

    lista_campi_film_rating = ["utente_id", "film_id", "Valutazione", "Data_valutazione"]
    lista_film_rating = []

    for i in range(len(reader)):
        lista_film_rating.append((reader[i][0], reader[i][1], reader[i][2], reader[i][3]))

    inserisci_dati(connection, "rating", lista_film_rating, lista_campi_film_rating)

