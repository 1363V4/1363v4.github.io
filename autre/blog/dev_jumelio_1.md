---
title: dev - jumelio 1
layout: post
---

je lance une petite série de dev blog.
paradoxalement, ils ne contiendront pas de code ou très peu.
c'est pas si intéressant et ça coûterait du temps de le nettoyer.

---

j'avais une idée de jeu qui consisterait à se déplacer dans le réseau formé
par ces alliances d'opportunités qu'ont les villes entre elles,
appelées "jumelages".

comme documenté avant dans [trois sur cinq](trois_sur_cinq.html),
j'avais fait un prototype.

je peux pas dire MVP vu que c'était carrément pas viable :
personne comprenait le jeu.

sauf mon patient papa, qui a fini par trouver une meilleure manière de le présenter.
j'ai reconnu le concept de [the oracle of bacon](https://www.oracleofbacon.org/).

c'est parti.

---

je dois penser aux performances de l'app. puis-je précalculer tous les tracés ?

je fais un essai et je tomberais sur un fichier de 6GB, avec une compression simple (remplacer le str d'une ville par un int).
le fichier alias pèse 240KB.

c'est trop pour mon hosting plan. 
je suis limité à 1GB.
je vais donc les calculer live, probablement pour les utilisateurs payants.

pour les utilisateurs gratuits, je précalculerai les chemins de capitale à capitale.

---

je sauvegarde le réseau. quel format choisir ? liste d'adjacence ou liste de paires ?

après test, ils ont les mêmes performances pour mon use case :
ils trouvent un plus court chemin d'une ville à l'autre en 40ms.
adj est un peu plus petit, un peu plus performant : je garde.

et maintenant un peu de stat.

---

comme on peut le voir, la plupart des villes sont des _dead ends_.
elles ne sont connectées qu'à une ville :

![jumelio1.png](/img/jumelio/jumelio1.png)
{:.ioda}

(on voit pas bien mais y'a une ville avec 78 jumelages... devinez laquelle)

ces villes, elles font chier tout le monde.
pour le calcul, pour le précalcul.
et si on les virait ?

regardons aussi la longueur moyenne des chemins :

![jumelio2.png](/img/jumelio/jumelio2.png)
{:.ioda}

un max de chemins impossibles.

---

je passe d'un graphe avec 16 000 villes à 7885.
on respire déjà mieux.

visualisons à nouveau :

![jumelio3.png](/img/jumelio/jumelio3.png)
{:.ioda}

![jumelio4.png](/img/jumelio/jumelio4.png)
{:.ioda}

c'est déjà mieux.

il reste des chemins impossibles.
j'aurais pu les virer au lieu de virer les villes isolées mais je vais faire autre chose.

on peut demander au joueur si le chemin est plus ou moins long que 7.
grosso modo le milieu de la bosse.

la répartition est grosso modo la suivante :

- 3/7 à moins de 7
- 3/7 à plus de 7
- 1/7 impossible

ça fait un petit effet aléatoire supplémentaire, j'aime bien.

c'est la pire option en termes de probas, mais elle existe.
la pièce peut retomber sur la tranche et te niquer.
c'est tout bête mais en termes de game design je pense que ça compte.

et voilà : plus d'interface _in the way_.
tu cliques un bouton, t'as une chance sur deux, parfois une surprise.
un peu de lore saupoudré dessus pour habiller le tout.
au bout de cinq essais ça coupe. une autre ?

la boucle est lancée.

---

et donc ?

je me chauffe à faire des jeux online.
j'ai décomposé le process en 3 étapes :

- être chaud en game design (ce post)
- mettre le jeu sur le web
- train une ia dessus

deuxième post sera sur la partie web.

pouche bleu lâche un com.
