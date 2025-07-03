#!/usr/bin/python3
"""
Script that takes the name of a state as an argument and lists all cities of that state, in this database hbtn_0e_4_usa

"""

import sys
import MySQLdb


def main():
    """Fonction principale du script"""
    # Vérifier le nombre d'arguments
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    
    # Récupérer les arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    
    try:
        # Se connecter à la base de données MySQL
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )
        
        # Créer un curseur
        cursor = db.cursor()
        
        # Exécuter la requête SQL avec protection contre l'injection SQL
        # Utilisation d'une requête avec JOIN pour récupérer les villes de l'état spécifié
        query = """
        SELECT cities.name 
        FROM cities 
        JOIN states ON cities.state_id = states.id 
        WHERE states.name = %s 
        ORDER BY cities.id ASC
        """
        
        cursor.execute(query, (state_name,))
        
        # Récupérer tous les résultats
        results = cursor.fetchall()
        
        # Afficher les résultats
        for row in results:
            print(row[0])
        
        # Fermer le curseur et la connexion
        cursor.close()
        db.close()
        
    except MySQLdb.Error as e:
        print("Erreur MySQL: {}".format(e))
        sys.exit(1)
    except Exception as e:
        print("Erreur: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
