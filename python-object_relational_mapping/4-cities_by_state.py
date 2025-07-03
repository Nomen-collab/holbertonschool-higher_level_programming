#!/usr/bin/python3
"""
Script qui liste toutes les villes de la base de données hbtn_0e_4_usa
avec les informations de leur état correspondant.
"""

try:
    import MySQLdb
except ImportError:
    import pymysql
    pymysql.install_as_MySQLdb()
    import MySQLdb
import sys


def main():
    """
    Fonction principale qui se connecte à MySQL et liste toutes les villes
    """
    # Vérifier le nombre d'arguments
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_user> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)
    
    # Récupérer les arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    try:
        # Se connecter à la base de données MySQL
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name
        )
        
        # Créer un curseur
        cursor = db.cursor()
        
        # Requête SQL pour récupérer toutes les villes avec leurs états
        # JOIN entre les tables cities et states
        query = """
        SELECT cities.id, cities.name, states.name 
        FROM cities 
        JOIN states ON cities.state_id = states.id 
        ORDER BY cities.id ASC
        """
        
        # Exécuter la requête (une seule fois comme demandé)
        cursor.execute(query)
        
        # Récupérer tous les résultats
        results = cursor.fetchall()
        
        # Afficher les résultats
        for row in results:
            print(row)
        
        # Fermer les connexions
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
