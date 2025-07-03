#!/usr/bin/python3
"""
That contains the class definition of the State and an instance Base = declarative_base() 
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class State(Base):
    """
    State class that defines the structure of states table
    
    """
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    
    def __repr__(self):
        """Représentation of the string of the objet state"""
        return f"<State(id={self.id}, name='{self.name}')>"


if __name__ == "__main__":
    print("Classe State définie avec succès!")
    print("Ce fichier peut être importé avec: from model_state import Base, State")
