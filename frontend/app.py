import json

from flask import Flask, jsonify, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configura la connessione al database MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'daitv'
}


# Funzione per creare una connessione al database
def create_db_connection():
    return mysql.connector.connect(**db_config)


# Funzione per eseguire query SQL
def execute_query(query, params=None):
    connection = create_db_connection()
    cursor = connection.cursor(dictionary=True)
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

@app.route('/')
def home():
    return render_template('home.html')

#  Rotte dell'API
@app.route('/data/generi', methods=['GET'])
def get_data_genere():
    query = """SELECT tipo_genere FROM `generi` 
     """
    items = execute_query(query)
    return items

@app.route('/generi')
def show_genere():
    genere = get_data_genere()
    return render_template('generi.html', genere= genere )

@app.route('/data/film', methods=['GET'])
def get_data_film_val():
    page = request.args.get('page', default=1, type=int)
    per_page = 100
    offset = (page - 1) * per_page
    query = f"""SELECT film.Titolo, AVG(Valutazione) AS val_med 
                FROM rating JOIN film 
                ON film.ID = rating.film_id 
                GROUP BY film.Titolo
                LIMIT {per_page} OFFSET {offset}"""
    items = execute_query(query)
    return items

@app.route('/films/film')
def show_film():
    page = request.args.get('page', default=1, type=int)
    tutti = get_data_film_val()
    num_pages = 18  # Placeholder, replace with actual calculation
    return render_template('tutti_film.html', tutti=tutti, page=page, num_pages=num_pages)

@app.route('/data/tutti/film', methods=['GET'])
def get_tutti_film(page=1, order_direction='asc'):
    items_per_page = 200
    offset = (page - 1) * items_per_page
    query = f"""SELECT film.Titolo, film.anno
                FROM film """
    query += f"ORDER BY film.Titolo {order_direction.upper()} "
    query += f"LIMIT {items_per_page} OFFSET {offset}"
    items = execute_query(query)
    return items

@app.route('/film')
def show_tutti_film():
    page = request.args.get('page', default=1, type=int)
    tutti = get_tutti_film(page)
    # Calculate total number of pages (num_pages) - You may have to adjust this calculation based on your total items and items per page
    num_pages = 18 # Placeholder, replace with actual calculation
    return render_template('tutti_film.html', tutti=tutti, page=page, num_pages=num_pages)

@app.route('/film/filter')
def filter_film():
    page = request.args.get('page', default=1, type=int)
    order_direction = request.args.get('order_direction', default='desc')
    print("Order Direction:", order_direction)  # Debug statement
    tutti = get_tutti_film(page, order_direction)
    num_pages = 18  # Placeholder, replace with actual calculation
    return render_template('tutti_film.html', tutti=tutti, page=page, num_pages=num_pages, order_direction=order_direction)


if __name__ == '__main__':
    app.run(debug=True)