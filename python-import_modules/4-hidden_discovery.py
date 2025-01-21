#!/usr/bin/python3

import sys
import types

if __name__ == "__main__":
    # Charger le module compilé
    module_name = "hidden_4"
    module_path = "/tmp/hidden_4.pyc"

    # Charger le module en utilisant imp
    sys.path.insert(0, "/tmp/")  # Ajouter le dossier /tmp au path pour l'importation
    hidden_module = __import__(module_name)

    # Filtrer les noms qui ne commencent pas par '__' et trier par ordre alphabétique
    names = dir(hidden_module)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)

