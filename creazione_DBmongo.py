import pymongo
from funzioniDAITV import *
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["DAITV"]
mycol = mydb["customers"]
ris=film_per_anno()
print(ris)