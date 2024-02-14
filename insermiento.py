
import csv

from funzioniDB import *
if __name__ == '__main__':
    pw = ""
    db = "DAITV"
    connection = create_db_connection("localhost", "root", pw, db)


    with open(r"C:\Users\Riccardo\Desktop\DAITASHARE\SAC\pythonProject\sac\pythonSac\DAITV_pulito_1.csv", encoding="iso-8859-1") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        reader = list(reader)

    lista_generi=[i for film in reader for i in film[3].split(",")]
    lista_generi=list(set(lista_generi))

    lista_generi_finita=[(x,) for x in lista_generi]

    inserisci_dati(connection,"generi",lista_generi_finita,["tipo_genere"])

    lista_film_genere=[]
    for film in reader:
        for i in film[3].split(","):
            lista_film_genere.append([film[0],i])


    lista_film_genere_finito=[]
    for x in lista_film_genere:
        lista_film_genere_finito.append(
            (int(x[0]), read_query(connection, f"""SELECT id FROM generi WHERE tipo_genere="{x[1]}";""")[0][0]))

    inserisci_dati(connection,"genere_film",lista_film_genere_finito,["id_film","id_genere"])

