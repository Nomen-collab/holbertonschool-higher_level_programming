#!/usr/bin/python3
"""
Script qui liste tous les objets State contenant la lettre 'a' 
de la base de données hbtn_0e_6_usa
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
        
        # Requête pour récupérer tous les états contenant la lettre 'a'
        # Utilisation de like() pour filtrer les noms contenant 'a'
        states_with_a = session.query(State).filter(
            State.name.like('%a%')
        ).order_by(State.id).all()
        
        # Afficher les résultats
        for state in states_with_a:
            print("{}: {}".format(state.id, state.name))
        
        # Fermer la session
        session.close()
        
    except Exception as e:
        print("Erreur: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
