---
title: marie theory
---

#### introduction

cercle quintes

![mm 7](/img/mm_7.png)
{:.ioda}

permet de repérer les degrés = accord qui vont bien ensemble

![mm 6](/img/mm_6.png)
{:.ioda}

en mode mineur

![mm 5](/img/mm_5.png)
{:.ioda}

#### création

on découpe m en i-v-i
et donc mm en i-v-i-i-v-i
puis on observe les regroupements faisables

![mm](/img/mm.png)
{:.ioda}

#### simplification

regroupons-les dans un tableau

![mm 2](/img/mm_2.png)
{:.ioda}

---

effaçons les répétitions ainsi que ceux semblables par permutation circulaire

![mm 3](/img/mm_3.png)
{:.ioda}

12 donc encore un cercle

#### esthétisation

deux ensembles de règles

mouvement de la fondamentale (+ 1, -2, -4)

quelques propriétés des dégrés

![mm 4](/img/mm_4.png)
{:.ioda}

pourquoi
v et vii majeurs en min (harmonique / mélodique)

#### programmation

générons-en quelques unes

```python
from itertools import cycle
from random import choice

progs = {
    2: [
        "i-vi".split("-"),
        "iv-i".split("-"),
    ],
    3: [
        "i-v-i".split("-"),
        "i-vii-vi".split("-"),
        "iv-ii-vi".split("-"),
    ],    
    4: [
        "i-v-ii-vi".split("-"),
        "i-vi-iv-i".split("-"),
        "i-vii-v-i".split("-"),
        "iv-ii-v-i".split("-"),
    ],    
    5: [
        "i-v-i-i-vi".split("-"),
        "i-v-i-iv-i".split("-"),
        "i-v-ii-v-i".split("-"),
    ],
}

roots = "f_c_g_d_a_e_b_f#_c#_g#_d#_a#".split("_")
circle = cycle(roots)

def get_chords(root='f', mode='major'):
    while next(circle) is not root:
        pass
    degrees = {}
    if mode == 'major':
        degrees['i'] = root
        degrees['v'] = next(circle)
        degrees['ii'] = next(circle) + "m"
        degrees['vi'] = next(circle) + "m"
        degrees['iii'] = next(circle) + "m"
        degrees['vii'] = next(circle) + "°"
        for _ in range(5):
            next(circle)
        degrees['iv'] = next(circle)
    elif mode == 'minor':
        degrees['i'] = root + "m"
        degrees['v'] = next(circle) + "m"
        degrees['ii'] = next(circle) + "°"
        for _ in range(5):
            next(circle)
        degrees['vi'] = next(circle)
        degrees['iii'] = next(circle)
        degrees['vii'] = next(circle)
        degrees['iv'] = next(circle) + "m"    
    return degrees
    
    
root = choice(roots)
mode = choice(['major', 'minor'])
degrees = get_chords(root=root, mode=mode)

prog_size = choice([*progs.keys()])
prog = choice(progs[prog_size])

print("key", degrees['i'])
print("prog", prog)
print("---")
for degree in prog:
    chord = degrees[degree]
    print(chord)

```

#### composition

comment écouter

si vous voulez continuer en python
https://pypi.org/project/synthesizer/

si vous voulez coder un synth -> circle of filth

sinon midi / fl

sinon piano
