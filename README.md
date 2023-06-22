# Optimisation hivernale
Le but de ce projet est de calculer le plus court chemin que doit effectuer une
ou plusieurs déneigeuses lors d'une opération de déneigement de la ville de
Montréal.

## Structure du projet
Ce projet structure en une arborescence *src* de codes et une arborescence *scripts* des scripts de démonstration

1. README.md
2. requirements.txt 
3. Optimisation_hivernale.pdf
4. AUTHORS.txt
5. scripts
    1. deneigeuse.py
    2. drone.py
    3. test_cost.py
    4. tests
        1. test_directed_noteulerien.py
        2. test_eulerien.py
        3. test_noeulerien_directed.py
        4. test_notStronglyConnected.py
        5. test_or_eulerien.py
        6. test_or_noteulerien.py
6. src
    1. deneigement.py
    2. parcours_drone.py
    3. utils.py
7. Outremont.png
8. Saint-Léonard.png
9. Verdun.png

Pour mieux comprendre le but de ce projet ainsi que les étapes aboutissant à la solution, consultez le document *Optimisation_hivernale.pdf*

## Prérequis
Pour ce projet,nous allons utiliser python pour exécuter les scripts de démonstration. Assurez-vous que **python** est bien installé.
Nous avons aussi besoin de certaines bibliothèques telles que **networkx, osmnx, matplotlib**.
Vou pouvez installer ces bibliothèques avec la commande
```
pip install -r requirements.txt
```

## Exécution
Nous avons préparé pour vous des scripts pour visualisez notre solution pour le problème de déneigement.
Pour exécuter ces scripts, déplacez au dossier *scripts*. Vous trouverez deux scripts qui s'appellent *drone.py* et *deneigeuse.py*.
Le but du script *drone.py* est de vous aider à visualiser le parcours optimal du drône qui effectue une étude complète du niveau de neige sur un quartier de la ville ou sur la ville complète. Voici la commande:
```
python3 drone.py <Nom du quartier>
```
Cela va vous donner une carte du quartier animée par le chemin que doit prendre le drône pour étudier le niveu de neige du quartier. En plus, il va afficher sur le terminal la longueur totale du parcours, le temps nécessaire et le coût pour le parcours. Vous voyez aussi un chemin complet sous forme d'une liste des arêtes dont les sommets sont des indices donnés par **osmnx**.
Par ailleurs, cette commande va aussi enregistrerle résultat de ce parcours avec la date dans un fichier qui s'appelle *result_drone.txt*. Vous retrouverez les mêmes informations affichées sur le terminal.

Ensuite, vous avez le script *deneigeuse.py* qui vous donne le résultat du déneigement effectué par les machines de la municipalité.
Voici la commande à taper:
```
python3 deneigeuse.py <Nom du quartier>
```
De même, vous verrez afficher sur le terminal la longueur du parcours, avec cette fois-i le temps et le coût de différents types de déneigeuses.
Le résultat sera enregistré dans le fichier *result_deneigeuse.txt*.

Vous pouvez aussi regarder comment on a comparé le prix de différents types de déneigeuses avec la commande:
```
python3 test_cost.py
```