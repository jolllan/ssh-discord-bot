# ssh-discord-bot
 Envoyer un message dans un channel spécifique et le bot exécute la commande.
 Le terme ssh n'est qu'imagé car le protocole n'est pas utilisé.
 
 Le fonctionnement est simple.
 Une personne spécifique dans un channel définis peut exécuter des commandes système, sur lequel le bot Python est hébergé.
 Si le message sur discord est "dir" le bot enverra le retour de la commande après le message.

## Mise en route
 - Renommer le fichier `config.py.exemple` en `config.py`
 - Créer un environnement virtuel : py/python3 -m venv venv
 - Télécharger les dépendances : `pip install -r requirements.txt`
 - Exécuter le bot.
 
 ## Fonctionnalité de commentaire:
  Il est possible d'ajouter une chaine de caractère identifiable permettant la non exécution des commandes.
  Si le message "// echo 1" est envoyé alors la commande ne s'exécute pas.
 
### *Requiert python 3.10 minimum*

