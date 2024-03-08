---
title: dev - jumelio 3
layout: post
---

en soit le projet, il s'agit juste de:

- faire un frontend htmx
    - tu envoies un state il fait l'échiquier
    - les cases peuvent être colorées si on peut s'y déplacer
- faire un moteur python spécial échecs poissons
- faire un env gym dessus
    - fen state to fen state
    - all possible actions
    - done if checkmate
    - valeurs de récompense
- exporter le gym ??
- faire un mode pvp
- faire un tier payant

facile quoi.

---

j'ai fait le premier point.
un chessboard avec que des div c'est possible.
[et je le prouve.](https://www.legires.fr/echecs)

---

alors tailwind c'est du bait ?
moi j'aime bien div1, div2, etc.
enfin je pense qu'on peut faire mieux.
mais il parait que l'ia connait bien tailwind ??
on verra où sera rome.

en tout cas, on a bel et bien utilisé htmlgenerator plutôt que fragments.
et c'était bel et bien bieng.

---

pour le moteur, j'ai pris python chess.

je pense pas le fork mais le réécrire en m'inspirant.
plein de trucs dont j'ai pas besoin.

---

on essaie de train une ia avec gym?
on a lu
[les tutos](https://gymnasium.farama.org/tutorials/training_agents/blackjack_tutorial/)
puis on a regardé
[un exemple classique](https://github.com/genyrosk/gym-chess)
et on avance doucement.

par exemple, sur l'exemple classique,
je peux piquer les 
[valeurs de move](https://github.com/genyrosk/gym-chess/blob/master/gym_chess/envs/chess_v1.py)
même si je sais pas comment elles se calculent.

j'avance vite, je coupe les coins, c'est du prototypage.
j'ai vu une
[bonne vidéo](https://www.youtube.com/watch?v=o5K0uqhxgsE)
sur le sujet qui m'a décomplexé.

---

on y coupe pas, il faut refaire l'engine.
l'avantage c'est que j'ai pas à chercher les bons moves,
gym va le faire.
mais je dois faire le moteur.

sur chessprogramming ils disent
le plus important c'est le 
[board state](https://www.chessprogramming.org/Board_Representation)
et le plus simple c'est le mailbox
(en même temps
[l'encoding optimal bon...](https://ai.stackexchange.com/questions/27336/how-does-the-alpha-zeros-move-encoding-work)
)

---

bon. courage.

tout ça c'est giga chiant.
je préférerais juste jouer en physique.
créer un club. sentir ça en vrai.
mais faut bien s'y coller.

ce qui motive c'est que je m'indépendance.
ce qui motive pas,
c'est que même avec ça 
[je mange une distance.](https://github.com/thomasahle/fastchess/blob/master/fastchess.py)
30% accuracy avec juste une mult de mat...
et en utilisant une lib de texte ?
putain j'aimerais me neuradownload cette shit dans le crâne.

le point positif c'est que j'ai eu une autre idée :
un board qui bouge d'une pièce par heure.
tu peux miser ce que tu veux sur un coup
(en crypto par exemple).
le coup le plus cher l'emporte.
à la fin les gagnants gagnent la mise des perdants.
et le twist :
tu peux miser pour n'importe quel coup.

c'est de l'edging appliqué.
hehehe.

bon.

je re, j'vais edge.
