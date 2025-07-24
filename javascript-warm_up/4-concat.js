#!/usr/bin/node
// Le module process fournit des informations et des contrôles sur le processus Node.js actuel.
// process.argv est un tableau contenant les arguments de la ligne de commande.
// Le premier élément (index 0) est le chemin de l'exécutable node.
// Le deuxième élément (index 1) est le chemin du fichier de script exécuté.
// Les arguments passés par l'utilisateur commencent à l'index 2.

// Récupère le premier argument passé par l'utilisateur (à l'index 2).
// Si l'argument n'est pas fourni, sa valeur sera 'undefined'.
const arg1 = process.argv[2];

// Récupère le deuxième argument passé par l'utilisateur (à l'index 3).
// Si l'argument n'est pas fourni, sa valeur sera 'undefined'.
const arg2 = process.argv[3];

// Affiche les deux arguments dans le format spécifié en utilisant des template literals (guillemets inversés).
// JavaScript convertira automatiquement 'undefined' en chaîne de caractères "undefined" si l'argument est manquant.
console.log(`${arg1} is ${arg2}`);
// Le fichier se termine ici avec un seul saut de ligne final.
