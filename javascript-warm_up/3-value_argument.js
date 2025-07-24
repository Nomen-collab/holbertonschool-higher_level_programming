#!/usr/bin/node
// Le module process fournit des informations et des contrôles sur le processus Node.js actuel.
// process.argv est un tableau contenant les arguments de la ligne de commande.
// Le premier élément (index 0) est le chemin de l'exécutable node.
// Le deuxième élément (index 1) est le chemin du fichier de script exécuté.
// Les arguments passés par l'utilisateur commencent à l'index 2.

// Vérifie la présence des arguments en accédant directement aux index.
if (process.argv[2] === undefined) {
  // Si process.argv[2] n'existe pas, cela signifie qu'aucun argument n'a été passé.
  console.log('No argument');
} else if (process.argv[3] === undefined) {
  // Si process.argv[2] existe mais process.argv[3] n'existe pas,
  // cela signifie qu'un seul argument a été passé.
  console.log('Argument found');
} else {
  // Si process.argv[3] existe, cela signifie que plusieurs arguments ont été passés.
  console.log('Arguments found');
}
// Le fichier se termine ici avec un seul saut de ligne final.
