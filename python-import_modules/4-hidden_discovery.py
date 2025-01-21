#!/usr/bin/python3
import importlib.util
import sys

if __name__ == "__main__":
    # Chemin du fichier .pyc
    file_path = '/tmp/hidden_4.pyc'

    # Chargement dynamique du fichier .pyc
    spec = importlib.util.spec_from_file_location("hidden_4", file_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Récupération des noms définis dans le module et filtrage
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):  # Ignorer les noms qui commencent par "__"
            print(name)
