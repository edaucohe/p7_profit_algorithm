# Project 7 - Profit algorithm

## Description

"Project 7 - Profit algorithm" est un programme à réaliser dans le cadre de la formation diplômante d'OpenClassrooms "Développeur d'application Python".

Ce projet a comme but de mettre en place un algorithme afin d'optimiser un script d'investissement.

Ce projet est composé de trois étapes :
- Programme brut.
- Programme optimisé.
- Backtesting.

### Programme brut
Premièrement, il faut créer un programme capable de trouver le meilleur investissement sans se soucier de
l'algorithme mis en place. Les seules contraintes à tenir en compte sont :
- Chaque action ne peut être achetée qu'une seule fois.
- Nous ne pouvons pas acheter une fraction d'action.
- Nous pouvons dépenser au maximum 500 euros par client.

Nota : Il y a un total de vingt actions, chaque action a un nom, un coût et un pourcentage de bénéfice
et il faut explorer toutes les combinaisons possibles.

### Programme optimisé
Deuxièmement, il faut créer un programme optimisé grâce à la mise en place d'un algorithme,
ainsi que prendre en compte les actions à récupérer depuis des fichiers .csv.
Les contraintes sont les mêmes que dans le cas précédent, mais il faut aussi :
- Fournir une réponse en moins d'une seconde.

Nota : On utilisera les mêmes actions que dans le cas précédent, c'est-à-dire, les mêmes
vingt actions.

### Backtesting et optimisation
Finalement, et afin de tester l'exactitude du programme, il faut faire une comparaison 
côte à côte entre les résultats de l'algorithme optimisé et un ensemble de données fournies.

Nota : Les données fournies se trouvent dans deux fichiers .csv, le premier avec mille-une action
et le deuxième avec mille actions. Chaque action a un nom, un coût et un pourcentage de bénéfice 
et il n'y a plus besoin d'explorer toutes les combinaisons possibles.

## Installation

Python version : 3.9
<création du venv>

Les dépendances sont listées dans le fichier `requirements.txt`.
Lancez :

```
pip install -r requirements.txt
```

## Setup

Rien à signaler

## Use
Lancez le script :

```
python main.py
```

## Helpful links

Utilisation de la librairie 'itertools' :

https://moonbooks.org/Articles/Comment-trouver-toutes-les-combinaisons-possibles-depuis-une-liste-delements-en-python-/

Graphique de complexité 'Big-O' :

https://www.bigocheatsheet.com/

Explication de l'algorithme du 'sac-à-dos' :

https://www.youtube.com/watch?v=wDsZhd1wEuk&list=PLnGpUjdYRdmN-46-mzVU9l5f2kggdset-&index=19&t=1524s&ab_channel=Algomius

