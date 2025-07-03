#!/usr/bin/python3
"""
Script that takes an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Vérifier qu'on a les 4 arguments requis
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    
    # Récupérer les arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
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
    
    # Créer la requête SQL avec format et l'entrée utilisateur
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    
    # Exécuter la requête
    cursor.execute(query)
    
    # Récupérer tous les résultats
    results = cursor.fetchall()
    
    # Afficher les résultats
    for row in results:
        print(row)
    
    # Fermer le curseur et la connexion
    cursor.close()
    db.close()
