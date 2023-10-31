---
title: trois sur cinq
layout: post
---

#### youpi

[youpi youpi mon jeu est fini](https://le.guide/autre/jeux/siisters.html)

vous pouvez aller y jouer

parlons ici du processus de dev

#### intro

faire un jeu web, c'était un des cinq défis (rappelez-vous)

deux motivations :

- c'est **essentiel** au game design.
le but du jeu (avec un grand j), ce n'est pas de gagner, c'est d'être joué.
comme je ne suis qu'un honnête pygame kiddie,
j'avais du mal à partager mes jeux
autrement qu'en les décrivant.
donc : utliser ce ronflant décodeur universel
qu'est le browser.
- c'est un plan de première boîte **solide**.
des tas de startup recyclent des ui vilainement simples,
faciles à renta en slappant stripe dessus,
et fignolent l'ux (ou la finalité)
une fois le premier client accroché.

bibi m'a demandé si je pouvais réaliser un app de survey web.

et typiquement, les services existants
hésiteraient pas à te faire un pricing premium
pour te donner l'heure.

mais ça a servi de déclencheur : allez on s'y met.

#### un

d'abord, il a fallu s'attaquer à l'horreur : **javascript**.

j'en avais besoin pour utiliser un composant que je voulais
dans mon ui finale : [globe.gl](https://globe.gl/)

c'était pas si pénible à utiliser.
en fait, c'est surtout la découverte des **requêtes ajax** qui a carry.
ce truc permet de garder pas mal de logique côté python.

pour faire une ui réactive, on a changé le css des blocks à la main.
heureusement j'ai utilisé beaucoup d'identifiants et peu de classes.
merci la philosophie **pico css**.

merci aussi la **flexbox**. 
ce truc est super.
j'ai mis longtemps à comprendre,
jusqu'à ce que je réalise que l'inspecteur du navigateur
(ctrl+shift+i)
permet de jouer avec.

oui car, et c'est important, j'ai commencé par host directement le truc.
j'ai utilisé **pythonanywhere**, 
parce que je connaissais déjà render
et que je savais pas si github pages allait marcher.

du coup, je devais reload le site à chaque changement.
log des tas de trucs dans la console.
attendre une plombe pour les logs d'erreur.
j'ai bien galéré,
**à ne pas refaire.**

#### deux

une fois qu'on avait un squelette graphique
suffisamment passable,
avec quelques dummy data,
il a fallu remplir le jeu.

on a allègrement scrapé wikipedia,
la page qui liste les villes jumelles d'un pays,
depuis la page qui liste ces pages (c'est clair ?).

rien que du classique : ``requests`` et ``bs4``.

pour m'être renseigné,
c'est du scraping à l'ancienne, mais ça suffisait.

ensuite il me fallait la géoloc de chaque ville.

pour celles qui avaient une fiche wiki,
généralement c'était dedans.
mais il en manquait une centaine.

j'ai donc fait un script avec ``selenium``
pour utiliser un site spécialisé géoloc.
ça s'est passé sans encombre.

au total, on a récupéré **16000** villes,
et pas loin de **80000** jumelages.

découverte amusante (non),
wiki peut dire que la ville a est jumelée avec la b,
mais pas de b à a.

#### trois

vous avez remarqué ?

jusqu'ici, pas une ligne de code.
croyez-moi il est dégueu.
vous n'avez qu'à aller voir celui du jeu.

j'ai donc fini en corrigeant moultes bugs,
en simplifiant à la machette,
et en passant un polish graphique.

j'ai demandé à bing create pour le logo.
il m'a halluciné un *"siisters"*,
qui a remplacé l'ancien nom, *"jumelio"*.

et pour finir, on s'est amusé.
finalement, c'est assez joli,
et un peu marrant.

#### concluons

déjà, c'était du boulot.
vous avez lu mon post précédent ?
depuis j'ai mis une limite de temps d'écran.
1h de jeux, 1h de propagande **max**.
ça a bien aidé.

ensuite, c'est dur de dev en dilettante.
on part avec une direction aléatoire,
on finit par batailler dans le spaghetti code.

j'aurais aimé m'appuyer encore plus sur python,
mais au moins j'ai évité les frameworks js
et c'est déjà pas mal.

je sais écrire du js maintenant (un peu),
mais je n'ai aucune idée de la puissance réelle de ``jquery``.

enfin : je n'ai pas traité la partie intéressante.

d'une part, pas de **visualisation de données**,
modéliser les jumelages en graphe,
étudier les chemins, les stratégies etc.
ça me viendra sûrement avec l'[advent of code](https://adventofcode.com/) le mois prochain.

et puis, pas de **game design**.
il n'a pas de courbe de difficulté,
aucune aide à l'apprentissage,
il est pas giga marrant...

c'est dur.
je vois des jeux magnifiques sortir :
balatro,
folder dungeon,
chants of sennaar...

quel art.

j'ai envie de recommencer.
j'ai une idée. deux.
on verra.

et j'ai fait une pastèque en 3 try au jeu de la pastèque.

c'est pas mal.

*update : bibi l'a fait en deux*
