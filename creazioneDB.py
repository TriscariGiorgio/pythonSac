import csv

from funzioniDB import *


if __name__ == '__main__':
    pw = ""
    db = "DAITV"
    connection = create_server_connection("localhost", "root", pw)
    esegui_query(connection, "DROP DATABASE DAITV")
    create_database(connection, "CREATE DATABASE DAITV")
    connection = create_db_connection("localhost", "root", pw, db)
    query = """SET GLOBAL max_allowed_packet = 268435456"""
    cursor = connection.cursor()
    cursor.execute(query)

    esegui_query(connection, """
        CREATE TABLE Utenti (
        ID_utente INT PRIMARY KEY AUTO_INCREMENT,
        eta int (10) NOT NULL,
        sesso char(1) check(sesso='M' OR sesso='F'),
        lavoro varchar(255) NOT NULL,
        domicilio INT(11) NOT NULL
    );
    """)
    esegui_query(connection, """
        CREATE TABLE Rating (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    utente_id INT,
    film_id INT,
    Valutazione DECIMAL(5, 1),
    Data_valutazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    esegui_query(connection, """
    CREATE TABLE Film (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Titolo VARCHAR(255),
   anno int
    );
    """)
    esegui_query(connection, """
      CREATE TABLE generi (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tipo_genere VARCHAR(255)
    );

       """)
    esegui_query(connection, """
       CREATE TABLE genere_film (
    id INT(11) PRIMARY KEY AUTO_INCREMENT,
    id_film INT(11),
    id_genere INT(11)
    );
       """)

    esegui_query(connection, """ALTER TABLE Rating
    ADD CONSTRAINT fk_utente_rating
    FOREIGN KEY (utente_id)
    REFERENCES utenti(id_utente);
    """)
    esegui_query(connection, """ALTER TABLE Rating
    ADD CONSTRAINT fk_film_rating
    FOREIGN KEY (film_id)
    REFERENCES film(id);
       """)
    esegui_query(connection, """ALTER TABLE genere_film 
    ADD CONSTRAINT fk_filmid 
    FOREIGN KEY (id_film) 
    REFERENCES Film(ID);
       """)
    esegui_query(connection, """ALTER TABLE genere_film 
    ADD CONSTRAINT fk_genereid 
    FOREIGN KEY (id_genere) 
    REFERENCES generi(id);
       """)

    with open(r"C:\Users\Giorgio\OneDrive\Desktop\DAITV_pulito_1.csv", encoding="iso-8859-1") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        reader = list(reader)

    lista_campi_film = ["titolo", "anno"]
    lista_film = []

    for i in range(len(reader)):
        lista_film.append((reader[i][1], reader[i][2]))

    inserisci_dati(connection, "film", lista_film, lista_campi_film)

    with open(r"C:\Users\Giorgio\OneDrive\Desktop\users_edit.csv", encoding="iso-8859-1") as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        reader = list(reader)

    lista_campi_utente = ["eta","sesso","lavoro","domicilio"]
    lista_utenti = []

    for i in range(len(reader)):
        lista_utenti.append((reader[i][2], reader[i][1],reader[i][4], reader[i][3]))

    inserisci_dati(connection, "utenti", lista_utenti, lista_campi_utente)

pw = ""
db = "DAITV"

connection = create_db_connection("localhost", "root", pw, db)

with open(r"C:\Users\Riccardo\Desktop\DAITASHARE\SAC\pythonProject\sac\ratings_edit.csv", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    reader = list(reader)

lista_campi_film_rating = ["utente_id", "film_id", "Valutazione", "Data_valutazione"]
lista_film_rating = []

for i in range(len(reader)):
    lista_film_rating.append((reader[i][0], reader[i][1], reader[i][2], reader[i][3]))

inserisci_dati(connection, "rating", lista_film_rating, lista_campi_film_rating)
