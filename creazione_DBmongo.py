import pymongo
from funzioniDAITV import *
def film_anno_mongo():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["DAITV"]
    mycol = mydb["film_anno"]

    risultato_finale = []
    risultato = film_per_anno()

    for x in risultato:
        risultato_finale.append({"anno": x[0], "tot_film": x[1]})
    mycol.insert_many(risultato_finale)

def film_genere_mongo():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["DAITV"]
    mycol = mydb["film_genere"]

    risultato_finale = []
    risultato = film_per_genere()
    for x in risultato:
        risultato_finale.append({"genere": x[0], "tot_film": x[1]})
    mycol.insert_many(risultato_finale)

def film_con_recensioni_basse_mongo():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["DAITV"]
    mycol = mydb["film_recensioni_basse"]

    risultato_finale = []
    risultato = film_con_recensioni_basse()
    for x in risultato:
        risultato_finale.append({"titolo": x[1], "anno": x[2], "valutazione": x[3]})
    mycol.insert_many(risultato_finale)

def top_10_per_intervallo_eta_sesso_mongo():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["DAITV"]
    mycol = mydb["top_10_eta_sesso"]


    risultato_finale = []
    risultato = top_10_per_intervallo_eta_sesso()
    for x in risultato:
        for i in range(len(x)-1):
            if isinstance(x[i],str):
                risultato_finale.append({"titolo": x[i], "valutazione": x[i+1]})
    mycol.insert_many(risultato_finale)

def rating_film_per_fascia_eta_mongo():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["DAITV"]
    mycol = mydb["film_fascia_eta"]

    risultato_finale = []
    risultato = rating_film_per_fascia_eta()
    for x in risultato:
        for i in range(len(x) - 1):
            if isinstance(x[i], str):
                risultato_finale.append({"titolo": x[i], "valutazione": x[i + 1]})
    mycol.insert_many(risultato_finale)

def iscritti_per_provincia_mongo():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["DAITV"]
    mycol = mydb["iscritti_provincia"]

    risultato_finale = []
    risultato = iscritti_per_provincia()
    for x in risultato:
        risultato_finale.append({"provincia": x[0], "numero_iscritti": x[1]})
    mycol.insert_many(risultato_finale)

def abbonati_per_lavoro_mongo():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["DAITV"]
    mycol = mydb["abbonati_lavoro"]

    risultato_finale = []
    risultato = abbonati_per_lavoro()
    for x in risultato:
        risultato_finale.append({"lavoro": x[0], "numero_iscritti": x[1]})
    mycol.insert_many(risultato_finale)