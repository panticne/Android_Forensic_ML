"""
    This file is the entrypoint to 1) parse apks and 2) pass the .csv into ML model
    It implements different optimisations and this program goal is to compare different
    model.

    This file is based on : https://github.com/urcuqui/WhiteHat/tree/master/Research/Android/scripts
                            https://github.com/MLDroid/drebin/blob/master/src/Main.py
"""
from parse import parse
from art import *

"""
If you want to implement more ML Model, you can create a file based on those example and import them here and implement
method in the main with others methods.
"""
from linearRegression import linearRegression
from randomForestClassifier import randomForestClassifier
from naivesBayes import naivesBayes
from decisionTree import decisionTree
from SVC import SVC
from kNeighborsClassifier import kNeighborsClassifier
from SVCTune import SVCGS
from kNeighborsClassifierTune import kNeighborsClassifierGS
from randomForestClassifierTune import randomForestClassifierGS
from kNeighborsClassifierRandom import kNeighborsClassifierRS
from randomForestClassifierRS import randomForestClassifierGS
from SVCRS import SVCRS
import os.path
import argparse


def main(args):
    """
    Main function for
    1) If files doesn't exists : APK Parsing and generating a file
    2) If files exists : Classification of Benign and Malware application
    :param args: arguments acquired from parse_args()
    """

    # We recover here the different parameters given in command line
    malDir = args.maldir
    malDirDest = args.maldir_dest
    goodDir = args.gooddir
    goodDirDest = args.gooddir_dest
    testSize = args.testsize
    # We force the used name for CSV files, feel free to change them. By default the parsing of AndroidManifest.xml
    # will generate those filename.
    goodCsvFile = "binaryApps_BEN.csv"
    malwareCsvFile = "binaryApps_MAL.csv"
    # This arg is used to define which method of optimisation is chosen
    # 0 = None , 1 = GridSearch, 2 = RandomSearch
    HPO = args.HPO
    # We check if filename exists in current directory, if not, we create them with parse.py
    if os.path.isfile(goodCsvFile) and os.path.isfile(malwareCsvFile):
        # We check the value of HPO
        if HPO == 0:
            SVC(testSize)
            kNeighborsClassifier(testSize)
            randomForestClassifier(testSize)
            linearRegression(testSize)
            naivesBayes(testSize)
            decisionTree(testSize)

        if HPO == 1:
            SVCGS(testSize)
            kNeighborsClassifierGS(testSize)
            randomForestClassifierGS(testSize)

        if HPO == 2:
            SVCRS(testSize)
            kNeighborsClassifierRS(testSize)
            randomForestClassifierGS(testSize)

    else:
        # We check if parameters are specified
        if malDir == None or malDirDest == None or goodDir == None or goodDirDest == None:
            print("You didn't specified all required parameters, check if you have {} and {} in your current "
                  "directory or specify parameters to create them\nYou can use \"python start.py --h\" "
                  "to get help.".format(goodCsvFile, malwareCsvFile))
        else:
            parse(malDir, malDirDest, goodDir, goodDirDest)


def menu():
    """
    This method is used to check the value specified by the user in command line
    By default values of parameters are :

    :return: ArgumentParser object which contains the parameters
    """
    args = argparse.ArgumentParser(description="Classification using Permission Android.")

    args.add_argument("--maldir", help="Absolute path to directory containing malware apks.")
    args.add_argument("--maldir_dest", help="Absolute path to directory where to store the malware apktool output.")
    args.add_argument("--gooddir", help="Absolute path to directory containing benign apks.")
    args.add_argument("--gooddir_dest", help="Absolute path to directory where to store the benign apktool output.")
    args.add_argument("--testsize", type=float, default=0.2,
                      help="Size of the test set when split (value between ]0;1[).")
    args.add_argument("--HPO", type=int, default=0,
                      help="Apply a Hyper-parameters optimization. 2 = Random Search, 1 = GridSearch and 0 = None")

    return args.parse_args()


Art = text2art('DrebinEasy')
main(menu())

