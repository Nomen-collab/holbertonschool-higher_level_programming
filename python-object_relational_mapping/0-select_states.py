#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Vérifier qu'on a les 3 arguments requis
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Recuperer les arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Se connecter à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    
    # Créer un curseur pour exécuter les requêtes
    cursor = db.cursor()
    
    # Exécuter la requête pour récupérer tous les états triés par id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Récupérer tous les résultats
    results = cursor.fetchall()
    
    # Afficher les résultats
    for row in results:
        print(row)
    
    # Fermer le curseur et la connexion
    cursor.close()
    db.close()
