# Android_Forensic_ML

Vous trouverez ici les différents fichiers utilisés lors de ce projet.

## Extraction des APK

Dans un premier temps, le projet a été tourné sur l'analyse des outils de forensique existants selon une liste de critère défini dans le  [rapport](https://github.com/panticne/Android_Forensic_ML/tree/main/Documentation).

Suite à cette analyse, une tentative d'exploitation de fichiers APK de téléphone Android a été faites. L'extraction se fait à l'aide de plusieurs outils :

- [adb](https://developer.android.com/studio/command-line/adb)
- [Andriller](https://github.com/den4uk/andriller)
- [AirDroid](https://play.google.com/store/apps/details?id=com.sand.airdroid&hl=fr_CH&gl=US)
- [ApkExtractor](https://play.google.com/store/apps/details?id=com.iraavanan.apkextractor&hl=en)
- [FileManager](https://play.google.com/store/apps/details?id=com.alphainventor.filemanager&hl=en_IN)

La meilleure solution est d'utiliser adb afin de récupérer les fichiers dont nous avons besoin. Par contre, afin de récupérer toutes les apk sans distinction, il devient nécessaire de rooter son téléphone, ce qui peut être contraignant selon le cas de figure.

Andriller est un très bon outil, mais n'est pas initialement conçu pour extraire des APK, l'application va backup le téléphone à l'aide de "Android Backup" et va ensuite effectuer ses analyses. Cette application permet aussi de casser les mots de passe et de décoder les bases de données présentes sur le téléphone afin de les parcourirs (Whatsapp).

Les trois dernières solutions nécessistent d'avoir la main mise sur le téléphone mais leur utilisation restent très simple. Une fois les applications téléchargées, il devient possible d'obtenir les APK sur un PC en se branchant simplement en USB dessus.

Vous trouverez tous les détails dans le rapport de ce projet.

## Datasets

Les dataset suivants ont été utilisés :


- [Drebin Dataset](https://www.sec.tu-bs.de/~danarp/drebin/)
- [Androzoo](https://androzoo.uni.lu/)


Vous aurez besoin de vous identifier auprès des ces universités afin de pouvoir obtenir un accès aux données. Vous trouverez plus d'information sur ces dataset dans cette section [Dataset](https://github.com/panticne/Android_Forensic_ML/tree/main/Code/datasets) ainsi que dans le rapport.

Androzoo permet, à l'aide de son API, de télécharger près de 15,430,831 APK identifiable à l'aide de plusieurs critères. J'ai pu grâce à cette api créer mes propres datasets afin de tester ma supposition.

J'ai pour le moment crée 2 ensembles de datasets
- 500 malwares et 500 goodwares
- 1000 malwares et 1000 goodwares

## Création des CSV

L'idée du projet est de voir si l'utilisation de l'analyse des permissions utilisées par des applications permet de définir si cette dernière est mallicieuse ou non. Pour s'y faire, je me suis basé sur les travaux de [urcuqui](https://github.com/urcuqui/WhiteHat/tree/master/Research/Android).

## Modèles

Les différents modèles ainsi que leurs résultats sont présents dans les différents [Notebook](https://github.com/panticne/Android_Forensic_ML/tree/main/Code/Notebook)
