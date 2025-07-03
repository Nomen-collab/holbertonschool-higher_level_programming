#!/usr/bin/python3
"""
Script qui affiche le premier objet State de la base de données hbtn_0e_6_usa
Usage: ./script.py <mysql_username> <mysql_password> <database_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Fonction principale du script"""
    # Vérifier le nombre d'arguments
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)
    
    # Récupérer les arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    try:
        # Créer l'URL de connexion à la base de données
        database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            mysql_username, mysql_password, database_name
        )
        
        # Créer le moteur SQLAlchemy
        engine = create_engine(database_url, pool_pre_ping=True)
        
        # Créer une session
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Requête pour récupérer le premier état (plus petit ID)
        # Utilisation de first() au lieu de all() pour ne récupérer qu'un seul résultat
        first_state = session.query(State).order_by(State.id).first()
        
        # Afficher le résultat
        if first_state is None:
            print("Nothing")
        else:
            print("{}: {}".format(first_state.id, first_state.name))
        
        # Fermer la session
        session.close()
        
    except Exception as e:
        print("Erreur: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
