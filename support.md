# Formation Python/Django

Une formation pratique sur  Django, un framework Python très populaire.

## Tableau des matieres

- [Installation de Python](#Installation-de-Python)
- [Installation de Visual Studio Code](#Installation-de-Visual-Studio-Code)
- [Mettre en place son projet](#Mettre en place son projet)

## Installation de Python

Pour pouvoir utiliser Django, vous avez besoin d'installer Python.
Pour l'installer rendez-vous au site [Python.org](https://python.org) et suivre les instrcutions.

## Installation de Visual Studio Code

Visual Studio ou VS Code, c'est un éditeur de code simple et facile à utiliser.
Pour l'installer, visitez [vscode](https://vscode.com)

## Mettre en place son projet

Une fois tout est bien installé, les choses pratiques demerrent.

Créer un dossier nommé, projet_multiservice puis entrez dessus.

```bash
mkdir projet_multiservice && projet_multiservice
```

Dans le dossier, nous allons creer notre premier projet.
Ne vous inquietez pas, le processus est simple, Django gere tous les aspects de creation de projet.

Juste suivez moi.

### Utiliser un gestionnaire de package

Creer un environtement virtuel, il permet de mieux versionner vos application.

```bash
python3 -m venv monenv
```

Activez le

```bash
monenv/bin/activate
```

### Installer Django

```bash
pip install django
```

### Generer le projet

```bash
django-admin startproject multiservice .
```

### Tester votre projet

Lancez le serveur depuis votre terminal/CMD

```bash
python manage.py runserver
```

Ouvrez votre navigateur et vous rendre au [http://localhost:8000](http://localhost:8000)

## Creer votre premiere application

Sur Django, un projet peut contenir plusieures applications et une application peut etre mis sur differents projets.

Lancez cette commande pour generer une nouvelle application

```bash
python manage.py startapp product
```

Formation Django  + certificat
Introduction et installation des pré-requis
Que ce qu'on va créer ?
Installation de python sur Windows
Installation de python sur Mac
Installation de python sur Linux
Installation de django
Installation de vs-code
Les bases de Python
Variables et types de données
Les opérateurs mathématiques
Les structures de données
Les structures de répétition
Les structures conditionnels
Initialisation de votre premier projet (account)
Votre premier projet django
Application vs projet en Django
Créer les applications requises
Tester l'application (Admin et page d'accueil)
Authentification avec Django
Customiser l'authentification de django en utilisant votre email
Créer le managers pour l'authentification
Créer un utilisateur et tester l'administration
Authentifier un utilisateur
Inscrire un nouvel utilisateur
Créer votre deuxième application Product
Créer les différentes Table en se basant sur un diagramme UML
Ajouter un produit
Modifier un produit
Supprimer un produit
Créer  votre 3eme application Transaction
Ajouter les tables
Ajouter une nouvelle dépense
Ajouter une nouvelle vente
Créer une API Rest
Installation de Django Rest Framework
Sérialiser les données
Ajouter les views & Urls
Tester votre API avec Postman
Déploiement
Acheter un serveur vps
Configurer le serveur
Mettre l'application sur Github
Installer les dépendances
Configurer Gunicorn
Configurer Nginx

