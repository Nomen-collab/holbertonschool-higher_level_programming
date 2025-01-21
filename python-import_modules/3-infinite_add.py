#!/usr/bin/python3
import sys

if __name__ == "__main__":
    result = 0  # Initialisation du résultat à 0
    # Parcourir tous les arguments passés (en excluant le script lui-même)
    for arg in sys.argv[1:]:
        result += int(arg)
    print(result)  # Afficher le résulta
