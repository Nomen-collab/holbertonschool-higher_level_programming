#!/usr/bin/node
// Le module process fournit des informations et des contrôles sur le processus Node.js actuel.
// process.argv est un tableau contenant les arguments de la ligne de commande.
// Le premier élément (index 0) est le chemin de l'exécutable node.
// Le deuxième élément (index 1) est le chemin du fichier de script exécuté.
// Les arguments passés par l'utilisateur commencent à l'index 2.

// Récupère le premier argument passé par l'utilisateur.
const firstArg = process.argv[2];

// Tente de convertir l'argument en un entier.
// parseInt convertit la chaîne jusqu'à ce qu'elle rencontre un caractère non numérique.
// Si la chaîne ne commence pas par un nombre, ou est vide, parseInt renverra NaN.
const convertedNumber = parseInt(firstArg);

// Vérifie si la valeur convertie est un nombre valide (pas NaN).
// Number.isNaN() est utilisé pour vérifier spécifiquement si la valeur est NaN,
// car NaN n'est pas égal à lui-même (NaN !== NaN).
if (Number.isNaN(convertedNumber)) {
  console.log('Not a number');
} else {
  // Si c'est un nombre valide, l'affiche au format demandé.
  console.log(`My number: ${convertedNumber}`);
}
// Le fichier se termine ici avec un seul saut de ligne final.
