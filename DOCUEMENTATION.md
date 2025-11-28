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
Le but de ce projet est d'héberger une machine "Exegol" et une base postgres sur docker. L'utilisateur utilisera le projet sur exegol, avec une interface web. Il entrera une cible, sélectionnera un des modes vu précédemment, puis lancera le pentest. L'orchestrator, LLM, va automatiquement distribuer les taches aux différents services (nmap, gobuster, ...), jusqu'a pouvoir faire un rapport sur les vulnérabilitées.