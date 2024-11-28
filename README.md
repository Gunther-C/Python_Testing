
# Gudlift : Debugging-Tests 
# (Feature-Update)
**Cette branche `Feature-Update` est dédiée à l'amélioration de la stabilité et des performances de l'application par le biais de tests et de débogages rigoureux.**
- Mise à jour des dépendances `requirements.txt`. 
- Installation des outils de test `locust`, `pytest` et `pytest-html`.

---
### Prérequis : 
**_Assurez-vous d'avoir Python 3.x installé sur votre machine :_** 
>       python --version 
___

## Cloner le Dépôt :
```bash
  git clone https://github.com/Gunther-C/Python_Testing.git
```
_(download ZIP)_ :
```bash
 https://github.com/Gunther-C/Python_Testing/archive/refs/heads/Debugging-Tests/feature-update.zip
```
---

## Créer et Activer un Environnement Virtuel :
### Naviguez dans le répertoire racine du projet :
```bash
   cd <nom-du-répertoire>
```
### Création
```bash
python -m venv .venv 
```
### Activation
>_Selon votre système_
> 1.     .venv\Scripts\activate.bat   
> 2.     source .venv/Scripts/Activate
> 3.     source .venv/bin/activate  
>_(Vous trouverez plus d'informations sur le site de [Stackoverflow](https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows/18713789#18713789))_  
---

## Installation des Dépendances
```bash
pip install -r requirements.txt
```
- Dépendances de tests inclus dans `requirements.txt` : 
  - `locust` pour les tests de charge
  - `pytest` pour les tests unitaires...
  - `pytest-html`.
---
