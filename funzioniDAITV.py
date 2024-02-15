
from database.connessioni import *
connection=crea_connessione_db()
def film_per_anno():
    query = """
	SELECT anno, COUNT(*) AS tot_film_anno
	FROM film
	GROUP BY anno
	ORDER BY tot_film_anno DESC;
	"""
    return read_query(connection, query)
