# TP Docker - API Flask avec MySQL et phpMyAdmin

## Description

Ce projet contient une API REST simple développée avec Flask qui interagit avec une base de données MySQL.  
L'ensemble est orchestré avec Docker Compose, incluant un service phpMyAdmin pour la gestion de la base.

---

## Structure du projet

```

compose-api-lab/
├── app/
│   └── api.py            # Code de l'API Flask
├── docker-compose.yml    # Configuration des services Docker
├── Dockerfile            # Image Docker pour l'API Flask
├── requirements.txt      # Dépendances Python
├── .env.example          # Exemple de variables d'environnement
└── .gitignore            # Ignorer fichiers sensibles et volumes

````

---

## Variables d'environnement

Créer un fichier `.env` à partir de `.env.example` et renseigner vos propres mots de passe et noms.

```env
MYSQL_ROOT_PASSWORD=rootpass
MYSQL_DATABASE=tpdb
MYSQL_USER=tpuser
MYSQL_PASSWORD=tppass
````

---

## Commandes pour démarrer le projet

```bash
docker-compose up -d --build
```

---

## Vérification

* Accéder à l’API : [http://localhost:5000/utilisateurs](http://localhost:5000/utilisateurs)
  Réponse attendue :

  ```json
  {"message": "Hello from MySQL!"}
  ```

* Accéder à phpMyAdmin : [http://localhost:8080](http://localhost:8080)
  Utiliser les identifiants définis dans `.env`

---

## Commandes utiles

* Afficher les conteneurs actifs :

  ```bash
  docker ps
  ```

* Voir les logs (exemple pour le service API) :

  ```bash
  docker logs compose-api-lab-api-1 --tail 20
  ```

* Arrêter tous les services :

  ```bash
  docker-compose down
  ```

---

## Livrables

* Le dépôt Git complet sans le fichier `.env`
* Captures d’écran :

  * API fonctionnelle dans le navigateur
  * Résultat de `docker ps`
  * Logs récents avec `docker-compose logs --tail=20`

---
