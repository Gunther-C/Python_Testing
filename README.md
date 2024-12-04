
## Debugging-Tests/feature-update
**`feature-update` est dédiée à l'amélioration de la stabilité et des performances de l'application par le biais de tests et de débogages rigoureux.**
- Mise à jour des dépendances `requirements.txt`. 
- Installation des outils de test `locust`, `pytest`.

---

## Debugging-Tests/feature-update/feature-update_bugfix-email-error
**`feature-update_bugfix-email-error` est dédiée à l'application de tests et de débogages sur l'adresse email des clubs.**

- Création d'un fichier `pytest.ini` a la racine du projet.
  - Configuration `pytest`.  
  - Création d'un `rapport html`.  
  

- Création d'un fichier `locustfile.py` a la racine du projet.
  ```bash
  locust -f locustfile.py --host http://127.0.0.1:5000 --users 6 --spawn-rate 1
  ```


- Création des packages de tests `pytest`.
  - Création d'un fichier `test_unit.py`.
  - Création d'un fichier `conftest.py`.
  - Création d'un fichier `mocks.py`.
  ```bash
  tests/
  ├── __init__.py
  ├── conftest.py
  ├── mocks.py
  └── unit/
      ├── __init__.py
      └── test_unit.py
  ```

- Debug `index.html`
- Debug `server.py`