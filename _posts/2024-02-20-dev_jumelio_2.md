---
title: dev - jumelio 2
layout: post
---

> i'm ceo, bitch

faire un site c'est chiant.
chiant de fou.

j'ai mis longtemps avant de trouver le bon workflow
alors je le partage.

---

déjà il faut héberger le site.
eh oui acheter un nom de domaine suffit pas.

j'ai testé quelques trucs : namecheap, name, ovh, ionos...
y'en a aucun de vraiment bien.

le host, j'utilise [pythonanywhere](https://www.pythonanywhere.com/).
ils font le ssl avec renew auto let's encrypt.
ils font le [wsgi](https://wsgi.readthedocs.io/en/latest/learn.html) à ma place.
je peux faire tourner des cronjobs.
1 giga storage.
my dream.

tout ça pour cinq balles par mois, ça les vaut large.
j'avais commencé à me faire la main sur leur version gratuite avec le uno magique,
j'ai sauté le pas.

et quand on paye on s'bouge.

---

pour host le code, je fais un repo github privé.

je l'édite via [cursor ai](https://cursor.sh/) avec l'extension vscode github repos.

ensuite je fais un git pull depuis une console bash dans python anywhere.
bien évidemment j'ai setup une clé ssh pour ça dans mon profil.

c'est tolérable.

---

le backend, c'est du flask classique.

ensuite j'utilise [htmx](https://htmx.org/).

en gros, c'est des raccourcis qu'on met sur un bloc html pour faire une requête ajax.
ils définissent aussi un bloc cible :
l'idée générale étant de renvoyer du html dedans.

il y a plein d'essais très intéressants sur leur site,
je vous laisse les lire.

tout ce que je renvoie est "boosté" pour faire du progressive enhancement.
je suis particulièrement attaché à l'idée que le site marche en mode dégradé :

``` python
def is_htmx():
    return 'hx-request' in request.headers

def hx_boost_content(route, *args, **kwargs):
    if is_htmx():
        return render_block(route, "content", *args, **kwargs)
    else:
        return render_template(route, *args, **kwargs)
```

je sais pas si ce que j'écris est débile ou non.

---

le html c'est chiant à écrire.

je suis parti avec [jinja2_fragments](https://github.com/sponsfreixes/jinja2-fragments) 
(la méthode render_block vient de là).
mais j'arrive pas à la faire marcher à plein potentiel je pense.

ceci j'ai repéré [un autre truc](https://github.com/basxsoftwareassociation/htmlgenerator?tab=readme-ov-file)...
mon instinct me dit que c'est ça le futur.

qui vimera verra.

---

le routing maintenant.

une requete get initalise le jeu.
ensuite un jeu c'est appuyer sur des boutons non ?

en fonction du nom du bouton je peux retourner l'html que je veux, où je veux :
en l'occurence, tout dans le body vu qu'on est sur une suite d'écrans.

ça donne un truc comme ça :

```python
@app.route('/jumelio', methods=['GET', 'POST'])
def jumelio():
    if request.method == "GET":
        return hx_boost_content('jumelio.html')
    elif request.method == "POST":
        match request.values.get('button'):
            case "start":
                return hx_boost_content('jumelio_game.html', params)
            case "answer 1" | "answer 2" | "answer 3":
                return hx_boost_content('jumelio_answer.html', params)
            case _:
                return 404
```

pourquoi faire simple.


---

j'ai pas fait de database. fuck it.
un fichier python qui contient les dict que je veux.
à la limite un txt mais faut le lire, relou.

j'aurais aimé tester [tinydb](https://tinydb.readthedocs.io/en/latest/index.html) 
mais bon si y'a pas besoin ?

---

un autre sujet : le free tier et le tier payant.

sur uno magique j'ai mis un pauvre lien soutenir qui redirige vers stripe.
c'est pas mal stripe de l'avis d'autres gens,
"mais faut regarder lemon squeezie".
on regardera, mais bon...

vous connaissez l'arnaque aux émirats ? non ? vous devriez...

en attendant j'ai pas de système premium.
tout est gratuit faute de mieux. profitez.

---

[enfin, la forme.](https://www.decathlon.fr/)

ça, pas de mystère, faut faire tester.
[des talks sympas](https://www.youtube.com/watch?v=YISKcRDcDJg) peuvent aider.

j'utilise pico css par réflexe sur les premiers mètres.
simple, rapide, responsive, fait le job.

du custom css si besoin.
je preview dans le navigateur, j'ajuste, je push, je pull.

ça reste chiant.

bientôt on pourra mettre un dessin dans l'ia et ça sortira tout.
html css, et on raccroche les wagons avec htmx.
my dream.

en attendant...

on apprend tailwinds ?
