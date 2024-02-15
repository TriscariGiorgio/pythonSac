from connessioni import *


def crea_tabelle_sql(filesql):
    connection=crea_connessione_db()
    with open(f"{filesql}", encoding="iso-8859-1") as f:
        testo = f.read()
    lista_testo = testo.split("--")
    lista_testo_finita = []
    for _ in lista_testo:
        lista_testo_finita.append(_.strip())

    lista_insert = []
    lista_create = []
    lista_alter = []
    lista_update = []
    lista_delete = []
    lista_drop=[]
    for x in lista_testo_finita:
        if x.startswith("CREATE TABLE"):
            lista_create.append(x)
        elif x.startswith("ALTER TABLE"):
            lista_alter.append(x)
        elif x.startswith("INSERT INTO"):
            lista_insert.append(x)
        elif x.startswith("UPDATE"):
            lista_update.append(x)
        elif x.startswith("DELETE"):
            lista_delete.append(x)
        elif x.startswith("DROP TABLE"):
            lista_drop.append(x)


    for x in lista_create:
        commands = x.split(';')
        for command in commands:
            if command.strip():  # Ignora le righe vuote
                esegui_query(connection, f"{command}")

    for x in lista_insert:
        commands = x.split(';')
        for command in commands:
            if command.strip():  # Ignora le righe vuote
                esegui_query(connection, f"{command}")

    for x in lista_update:
        commands = x.split(';')
        for command in commands:
            if command.strip():  # Ignora le righe vuote
                esegui_query(connection, f"{command}")

    for x in lista_alter:
        commands = x.split(';')
        for command in commands:
            if command.strip():  # Ignora le righe vuote
                esegui_query(connection, f"{command}")

    for x in lista_drop:
        commands = x.split(';')
        for command in commands:
            if command.strip():  # Ignora le righe vuote
                esegui_query(connection, f"{command}")

def inserisci_dati_sql(filesql):
    with open(f"{filesql}", encoding="iso-8859-1") as f:
        testo = f.read()
    lista_testo = testo.split("--")
    lista_testo_finita = []
    for _ in lista_testo:
        lista_testo_finita.append(_.strip())

