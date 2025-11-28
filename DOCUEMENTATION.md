# Projet : Agent de pentest

Ce projet à pour but d'automatiser un pentest avec 4 catégories différentes : détection de flux, application web, réseau, global.

## Languages de programmation
- Python
- HTML
- CSS
- Javascript
- SQL

## Librairies
- Flask
- Celery
- Redis

## OS
Utilisation de Exegol dans docker car tous les outils de pentest sont déjà installés.

## Aperçu du projet
Le but de ce projet est d'héberger une machine "Exegol" et une base postgres sur docker. L'utilisateur utilisera le projet sur exegol, avec une interface web. Il entrera une cible, sélectionnera un des modes vu précédemment, puis lancera le pentest. L'orchestrator, LLM, va automatiquement distribuer les taches aux différents services (nmap, gobuster, ...), jusqua pouvoir faire un rapport sur les vulnérabilitées.

## Les variables
Pour des raisons pratiques, les variables auront un formatage bien précis.
Exemple : 
- Variable de nom de service
    - SN_NMAP
    - SN_SQLMAP
    - SN_GOBUSTER
- Noms pour les api : 
    - /api/call_gemini

## API
Pour l'API nous avons choisit FastAPI sur le script api.py.

```python
@app.get("/api/gemini")
def read_gemini(message: str = None):
    if message is None:
        message = get_gemini_response("Pour un pentest sur site web, quels sont les outils les plus utilisés ?")
    return {"message": message}
```

Ce code va nous permettre d'envoyer des messages à gémini, qui sera le coeur de notre orchestrator