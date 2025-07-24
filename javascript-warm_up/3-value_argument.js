#!/usr/bin/node
// Le module process fournit des informations et des contrôles sur le processus Node.js actuel.
// process.argv est un tableau contenant les arguments de la ligne de commande.
// Le premier élément (index 0) est le chemin de l'exécutable node.
// Le deuxième élément (index 1) est le chemin du fichier de script exécuté.
// Les arguments réels commencent à l'index 2.
// Donc, le nombre d'arguments passés par l'utilisateur est la longueur totale de process.argv moins 2.
const numberOfArguments = process.argv.length - 2;

// Vérifie le nombre d'arguments et affiche le message approprié.
if (numberOfArguments === 0) {
  console.log('No argument');
} else if (numberOfArguments === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
// Le fichier se termine ici avec un seul saut de ligne final.
