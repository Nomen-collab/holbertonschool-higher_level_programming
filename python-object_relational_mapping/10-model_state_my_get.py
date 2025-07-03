#!/usr/bin/python3
"""
Prints the state object with the name passed as argument from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


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
        # Créer l'URL de connexion à la base de données
        database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            mysql_username, mysql_password, database_name
        )
        
        # Créer le moteur SQLAlchemy
        engine = create_engine(database_url, pool_pre_ping=True)
        
        # Créer une session
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Requête sécurisée pour rechercher l'état par nom
        # SQLAlchemy protège automatiquement contre l'injection SQL
        # en utilisant des paramètres liés
        state = session.query(State).filter(State.name == state_name).first()
        
        # Afficher le résultat
        if state is None:
            print("Not found")
        else:
            print("{}".format(state.id))
        
        # Fermer la session
        session.close()
        
    except Exception as e:
        print("Erreur: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
