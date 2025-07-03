#!/usr/bin/python3
"""
Script qui affiche toutes les valeurs de la table states
où le nom correspond à l'argument fourni.
Protégé contre les injections SQL avec des requêtes paramétrées.
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
    Fonction principale qui se connecte à MySQL et filtre les états
    de manière sécurisée
    """
    # Vérifier le nombre d'arguments
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_user> <mysql_password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    
    # Récupérer les arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    
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
        
        # Requête SQL sécurisée avec paramètre
        # Le %s sera remplacé de manière sécurisée par MySQLdb
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        
        # Exécuter la requête avec le paramètre
        # MySQLdb va automatiquement échapper les caractères dangereux
        cursor.execute(query, (state_name,))
        
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
