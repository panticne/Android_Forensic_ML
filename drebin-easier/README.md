# Description

Cet outil a été développé afin de :
- Parser une liste d'APK bénin et une liste d'APK malicieux et y attribuer une séquence en fonction des permissions
- Stocker les résultats précédents dans des fichiers .cls
- Utiliser les .cls afin d'entraîner plusieurs modèles et afficher leurs résultats (Sans optimisation des hypers paramètres, avec Grid Search CV des hypers paramètres et Random Search CV des hypers paramètres

# Environnement 

Le projet a été réalisé sur une VM Ubuntu (https://www.osboxes.org/ubuntu/)

Le code a été développé sur l’IDE PyCharm Community (https://www.jetbrains.com/fr-fr/pycharm/download/#section=windows)

Version de python : 2.7.17

Version de pip : 9.0.1


# Installation

Il vous faudra ensuite lancer la commande suivante :
```
pip install -r requirements.txt
```

Afin de pouvoir parser des APK il vous faudra également pouvoir lancer apktool, pour l'installer :
```
sudo apt-get install -y apktool
```

# Paramètres 
```
"--maldir", help="Absolute path to directory containing malware apks.")
"--maldir_dest", help="Absolute path to directory where to store the malware apktool output.")
"--gooddir", help="Absolute path to directory containing benign apks.")
"--gooddir_dest", help="Absolute path to directory where to store the benign apktool output.")
"--testsize", help="Size of the test set when split (value between ]0;1[).")
"--HPO", help="Apply a Hyper-parameters optimization. 2 = Random Search, 1 = GridSearch and 0 = None")
```
# Exemples de commande

Pour créer les csv :
```
python start.py --maldir /home/osboxes/Desktop/APK/MAL/ --maldir_dest /home/osboxes/Desktop/MAL_Extract/ --gooddir /home/osboxes/Desktop/APK/ --gooddir_dest /home/osboxes/Desktop/BEN_Extract/ --HPO 2
```

Pour lancer les modèles :
```
python start.py --HPO 1
```
