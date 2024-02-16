from database.connessioni import *
connection = crea_connessione_db()
def film_per_anno():

    query = """
	SELECT anno, COUNT(*) AS tot_film_anno
	FROM film
	GROUP BY anno
	ORDER BY tot_film_anno DESC;
	"""

    return read_query(connection, query)

def film_per_genere():

	query = """
	SELECT tipo_genere, COUNT(genere_film.id) AS tot_film_genere
	FROM genere_film
	JOIN generi ON generi.id = genere_film.id_genere	
	GROUP BY tipo_genere
	ORDER BY tot_film_genere DESC;
	"""
	return read_query(connection, query)

def film_con_recensioni_basse():
    query = """
    SELECT f.*
    FROM Film f
    JOIN Rating r ON f.ID = r.film_id
    WHERE r.Valutazione < 3
    GROUP BY f.ID
    HAVING COUNT(DISTINCT r.utente_id) >= 250;
    """
    return read_query(connection,query)

def top_10_per_intervallo_eta_sesso():
    query = """
    	SELECT 
    f1_film.Titolo AS top_film_under_18,
    f1.valutazione_media AS top_valutazione_under_18,
    f2_film.Titolo AS top_film_18_to_24,
    f2.valutazione_media AS top_valutazione_18_to_24,
    f3_film.Titolo AS top_film_25_to_34,
    f3.valutazione_media AS top_valutazione_25_to_34,
    f4_film.Titolo AS top_film_35_to_44,
    f4.valutazione_media AS top_valutazione_35_to_44,
    f5_film.Titolo AS top_film_45_to_54,
    f5.valutazione_media AS top_valutazione_45_to_54,
    f6_film.Titolo AS top_film_over_55,
    f6.valutazione_media AS top_valutazione_over_55
FROM 
    film_rating_under_18 AS f1
    LEFT JOIN film AS f1_film ON f1_film.ID = f1.id_film
    LEFT JOIN film_rating_18_to_24 AS f2 ON f2.ID = f1.id_film
    LEFT JOIN film AS f2_film ON f2_film.ID = f2.id_film
    LEFT JOIN film_rating_25_to_34 AS f3 ON f3.ID = f1.id_film
    LEFT JOIN film AS f3_film ON f3_film.ID = f3.id_film
    LEFT JOIN film_rating_35_to_44 AS f4 ON f4.ID = f1.id_film
    LEFT JOIN film AS f4_film ON f4_film.ID = f4.id_film
    LEFT JOIN film_rating_45_to_54 AS f5 ON f5.ID = f1.id_film
    LEFT JOIN film AS f5_film ON f5_film.ID = f5.id_film
    LEFT JOIN film_rating_over_55 AS f6 ON f6.ID = f1.id_film
    LEFT JOIN film AS f6_film ON f6_film.ID = f6.id_film
ORDER BY 
    f1.valutazione_media DESC,
    f2.valutazione_media DESC,
    f3.valutazione_media DESC,
    f4.valutazione_media DESC,
    f5.valutazione_media DESC,
    f6.valutazione_media DESC
LIMIT 10;
    """
    return read_query(connection,query)

def rating_film_per_fascia_eta():
    query = """
    SELECT 
    f1_film.Titolo AS top_film_under_18,
    f1.valutazione_media AS top_valutazione_under_18,
    f2_film.Titolo AS top_film_18_to_24,
    f2.valutazione_media AS top_valutazione_18_to_24,
    f3_film.Titolo AS top_film_25_to_34,
    f3.valutazione_media AS top_valutazione_25_to_34,
    f4_film.Titolo AS top_film_35_to_44,
    f4.valutazione_media AS top_valutazione_35_to_44,
    f5_film.Titolo AS top_film_45_to_54,
    f5.valutazione_media AS top_valutazione_45_to_54,
    f6_film.Titolo AS top_film_over_55,
    f6.valutazione_media AS top_valutazione_over_55
FROM 
    film_rating_under_18 AS f1
    LEFT JOIN film AS f1_film ON f1_film.ID = f1.id_film
    LEFT JOIN film_rating_18_to_24 AS f2 ON f2.ID = f1.id_film
    LEFT JOIN film AS f2_film ON f2_film.ID = f2.id_film
    LEFT JOIN film_rating_25_to_34 AS f3 ON f3.ID = f1.id_film
    LEFT JOIN film AS f3_film ON f3_film.ID = f3.id_film
    LEFT JOIN film_rating_35_to_44 AS f4 ON f4.ID = f1.id_film
    LEFT JOIN film AS f4_film ON f4_film.ID = f4.id_film
    LEFT JOIN film_rating_45_to_54 AS f5 ON f5.ID = f1.id_film
    LEFT JOIN film AS f5_film ON f5_film.ID = f5.id_film
    LEFT JOIN film_rating_over_55 AS f6 ON f6.ID = f1.id_film
    LEFT JOIN film AS f6_film ON f6_film.ID = f6.id_film
WHERE 
    f1.valutazione_media IS NOT NULL 
    AND f2.valutazione_media IS NOT NULL 
    AND f3.valutazione_media IS NOT NULL 
    AND f4.valutazione_media IS NOT NULL 
    AND f5.valutazione_media IS NOT NULL 
    AND f6.valutazione_media IS NOT NULL 
ORDER BY 
    f1.valutazione_media ,
    f2.valutazione_media ,
    f3.valutazione_media ,
    f4.valutazione_media ,
    f5.valutazione_media ,
    f6.valutazione_media; 
    """
    return read_query(connection,query)


def iscritti_per_provincia():
    query = """
    SELECT provincia, COUNT(*) AS numero_iscritti
    FROM Utenti
    GROUP BY provincia
    ORDER BY numero_iscritti DESC
    LIMIT 20;
    """
    return read_query(connection,query)

def abbonati_per_lavoro():
    query = """
    SELECT lavoro, COUNT(*) AS numero_abbonati
    FROM Utenti
    GROUP BY lavoro
    ORDER BY numero_abbonati DESC
    ;
    """
    return read_query(connection,query)