# Android_Forensic_ML

Vous trouverez ici les différents fichiers utilisés lors de ce projet.

## Schéma du projet

![Schéma du projet](https://github.com/panticne/Android_Forensic_ML/blob/main/images/sch%C3%A9ma.png)

1 - Extraction des APK à l'aide d'ADB

2 - Téléchargement des APK sur Androzoo

3 - Récéption des APK et stockage dans un goodDir et un malDir

4 - L'utilisateur lance le programme

5 - L'utilisateur n'a pas de dataset et va les créer en appelant parser.py

6 - Le parser récupère les APK présentent dans goodDir et malDir

7 - Une extraction du code est faîtes avec apktool et les sorties sont effacés pour ne laisse que l'AndroidManifest.xml

8 - L'utilisateur possède un dataset et va le donner pour entraîner des modèles et ces modèles seront stockés au format pickle

9 - L'utilisateur veut tester si ses applications sont des malwares ou bénignes et va les envoyer au modèle qui retournera une réponse.


## Implémentation

Vous trouverez tous les détails d'implémentation dans le [rapport](https://github.com/panticne/Android_Forensic_ML/tree/main/Documentation) et le code source dans le dossier [drebin-easier](https://github.com/panticne/Android_Forensic_ML/tree/main/drebin-easier)

