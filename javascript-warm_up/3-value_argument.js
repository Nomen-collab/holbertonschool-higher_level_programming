#!/usr/bin/node
// Le module process fournit des informations et des contrôles sur le processus Node.js actuel.
// process.argv est un tableau contenant les arguments de la ligne de commande.
// Le premier élément (index 0) est le chemin de l'exécutable node.
// Le deuxième élément (index 1) est le chemin du fichier de script exécuté.
// Les arguments passés par l'utilisateur commencent à l'index 2.

// Vérifie si le premier argument utilisateur (à l'index 2) existe.
if (process.argv[2] === undefined) {
  // Si process.argv[2] n'existe pas, cela signifie qu'aucun argument n'a été passé.
  console.log('No argument');
} else {
  // Si process.argv[2] existe, affiche sa valeur.
  console.log(process.argv[2]);
}
// Le fichier se termine ici avec un seul saut de ligne final.
