#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)
    
    # Get arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)
    
    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query for the state with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()
    
    # Check if the state exists
    if state_to_update:
        # Update the name to "New Mexico"
        state_to_update.name = "New Mexico"
        
        # Commit the changes
        session.commit()
    
    # Close the session
    session.close()
