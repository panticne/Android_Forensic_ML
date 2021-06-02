# Détection basée sur les droits

Installation des librairies
```
pip install -r requirements.txt 
```
(Insérer le workflow une fois qu'il est fait)

Le code est automatique, il suffit de lancer le fichier : start.py

Si vous ne possédez aucun datasets, importer le nombre d'APK bénigne que vous souhaitez ainsi que le nombre d'APK malicieux que vous avez besoin 
afin d'entraîner les modèles dans deux dossiers séparés (maldir et goodir).

Vous pouvez utiliser le dataset présent dans ce dossier.

Voici la liste des différents paramètres nécessaires :

```
// Plus d'actu"--type", type= int, default= 0, help="Type of Classification to be performed (0 for LinearRegression, 1 for RandomForestClassifier, 2 for Naives Bayes, 3 for Decision Tree, 4 for kNeighbors and 5 for SVC")
"--perm", default= "/home/osboxes/Desktop/APK/MAL", help= "Absolute path to directory containing malware apks")
"--maldir", default= "/home/osboxes/Desktop/APK/MAL", help= "Absolute path to directory containing malware apks")
"--maldir_dest", default= "/home/osboxes/Desktop/APK/MAL/OUTPUT", help= "Absolute path to directory where to store the malware output")
"--gooddir", default= "/home/osboxes/Desktop/APK/", help= "Absolute path to directory containing benign apks")
"--gooddir_dest", default= "/home/osboxes/Desktop/APK/OUTPUT", help= "Absolute path to directory where to store the benign output")
"--gs", --gs", type= int, default= 0, help= ""2 Random Search, 1 If you want to use tuning with GridSearch 0 instead")

```

Exemple de commande :

```
python start.py --maldir /home/osboxes/Desktop/APK/MAL/ --maldir_dest /home/osboxes/Desktop/MAL_Extract/ --gooddir /home/osboxes/Desktop/APK/ --gooddir_dest /home/osboxes/Desktop/BEN_Extract/ --gs 0
```

TODO : Laisser le choix ou non de créer les données car si pas de CSV -> les crée automatiquement
