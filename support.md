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
