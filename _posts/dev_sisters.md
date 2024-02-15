---
title: dev sisters
layout: post
---

début full js la planète three.js
une galère mais ajax puis htmx
(pas possible avec la planète i guess)
logique aux fraises, pb interface
refaire en htmx
idée game design papa: bacon number
recherche djikstra (aoc lol)
payer pour modifier départ arrivée ?
score sur cinq à la suite ?
partage sur les rs ? pas chaud

300 villes 800 mega
5223_8005_10_ 400kb * 16000 (15969) = 6GB
on creuse ? on dégage les villes pas connus ?
les deux
les villes connues pour le free tier
le calcul networkx pour le paying

on fait le dict alias avant de construire le graphe
pour pas utf8 dégueu
400KB et un lookup O1

edge vs adj
meme perfs, adj un peu mieux, un peu plus petit
go adj

40s les 1000 requests soit 40ms la requete

on teste ? puis dict simplifié ?

hmmm. on a beaucoup de None et de 5+. 
Analysons:
jumelage
Counter({1: 8084, 2: 2537, 3: 1468, 4: 1005, 5: 716, 6: 525, 7: 370, 8: 274, 9: 181, 10: 155, 11: 104, 12: 82, 13: 66, 14: 60, 15: 44, 18: 34, 17: 30, 16: 27, 19: 21, 21: 18, 22: 17, 30: 16, 27: 16, 20: 16, 24: 15, 28: 13, 23: 11, 25: 10, 26: 9, 29: 7, 32: 6, 33: 5, 31: 4, 36: 3, 34: 2, 37: 2, 39: 2, 35: 2, 61: 1, 56: 1, 41: 1, 46: 1, 78: 1, 40: 1, 74: 1, 58: 1, 55: 1, 72: 1, 53: 1, 48: 1})
78 c'est shangai

et tous les liens
Counter({'none': 86363566, 8: 35278954, 9: 31765528, 7: 28890802, 10: 22622506, 6: 16319350, 11: 13569530, 12: 7055768, 5: 6047612, 13: 3227604, 4: 1453258, 14: 1316364, 15: 492220, 3: 271116, 16: 178628, 17: 61920, 2: 47920, 18: 21128, 1: 15969, 19: 6658, 20: 1964, 21: 492, 22: 88, 23: 16})

visualisons

ça pue. enlevons les 8084 boucles de 1 et reessayons

nouveau dico...
Graph with 15181 nodes and 39830 edges
sis
Counter({2: 2537, 3: 1468, 4: 1005, 5: 716, 6: 525, 7: 370, 8: 274, 9: 181, 10: 155, 11: 104, 12: 82, 13: 66, 14: 60, 15: 44, 18: 34, 17: 30, 16: 27, 19: 21, 21: 18, 22: 17, 30: 16, 27: 16, 20: 16, 24: 15, 28: 13, 23: 11, 25: 10, 26: 9, 29: 7, 32: 6, 33: 5, 31: 4, 36: 3, 34: 2, 37: 2, 39: 2, 35: 2, 61: 1, 56: 1, 41: 1, 46: 1, 78: 1, 40: 1, 74: 1, 58: 1, 55: 1, 72: 1, 53: 1, 48: 1})
paths
Counter({6: 26505128, 5: 19078630, 7: 9780802, 4: 4349330, 8: 1287414, 3: 532022, 'none': 456456, 9: 113262, 2: 55606, 1: 7885, 10: 6480, 11: 204, 12: 6})

bon ça bug j'ai chié mes alias
je recommence, je prune le graph de tout ce qui a moins de 2 aretes

Graph with 7885 nodes and 16648 edges
Counter({2: 2424, 3: 1370, 1: 837, 4: 790, 5: 558, 6: 371, 0: 288, 7: 261, 8: 208, 9: 144, 10: 108, 11: 90, 12: 52, 13: 51, 14: 47, 16: 32, 15: 31, 18: 25, 17: 24, 20: 18, 30: 18, 19: 17, 21: 14, 27: 14, 22: 13, 24: 12, 28: 11, 23: 9, 32: 7, 26: 7, 29: 6, 25: 5, 31: 3, 34: 2, 33: 2, 57: 2, 36: 2, 52: 1, 40: 1, 58: 1, 42: 1, 61: 1, 70: 1, 53: 1, 39: 1, 48: 1, 37: 1, 51: 1, 35: 1})
Counter({7: 12635500, 8: 11409008, 6: 9247382, 'none': 8017352, 9: 7681206, 10: 4268816, 5: 4098514, 11: 2058374, 4: 1092652, 12: 876816, 13: 343386, 3: 199040, 14: 131166, 15: 48722, 2: 33294, 16: 16824, 1: 7885, 17: 5220, 18: 1570, 19: 396, 20: 90, 21: 12})

pas mal !!
en splittant sur 7-, 8+:
7-: 27314267
8+: 26841606
none: 8017352

plutôt equilibré, 3/3/1

est-ce que le dico complet marche ? (quel taille)
on dirait pas

dev htmx mais c'est un autre post
