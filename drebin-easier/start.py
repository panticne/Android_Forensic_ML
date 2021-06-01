from parse import parse
#from RandomClassification import RandomClassification
#from HoldoutClassification import HoldoutClassification
from art import *
from linearRegression import linearRegression
from randomForestClassifier import randomForestClassifier
from naivesBayes import naivesBayes
from decisionTree import decisionTree
from SVC import SVC
from kNeighborsClassifier import kNeighborsClassifier
import os.path
import psutil, argparse

def main(args, FeatureOption):
    '''
    Main function for malware and goodware classification
    :param args: arguments acquired from command lines(refer to ParseArgs() for list of args)
    :param FeatureOption: False
    '''
    type_model = args.type
    malDir= args.maldir
    malDirDest = args.maldir_dest
    goodDir= args.gooddir
    goodDirDest = args.gooddir_dest
    testSize = args.testsize
    goodCsvFile = "binaryApps_BEN.csv"
    malwareCsvFile = "binaryApps_MAL.csv"

    if os.path.isfile(goodCsvFile) and os.path.isfile(malwareCsvFile):
        print("File exist")
        #LinearRegression
        if type_model == 0:
            linearRegression(testSize)
        #RandomForestClassifier
        if type_model == 1:
            randomForestClassifier(testSize)
        #Naives Bayes
        if type_model == 2:
            naivesBayes(testSize)
        #Decision tree
        if type_model == 3:
            decisionTree(testSize)
        if type_model == 4:
            kNeighborsClassifier(testSize)
        #SVC
        if type_model == 5:
            SVC(testSize)

    else:
        parse(malDir, malDirDest, goodDir, goodDirDest)


def menu():

    args =  argparse.ArgumentParser(description="Classification using Permission Android")
    args.add_argument("--type", type= int, default= 0,
                      help="Type of Classification to be performed (0 for Random Classification, 1 for Holdout Classification")
    args.add_argument("--perm", default= "/home/osboxes/Desktop/APK/MAL",
                      help= "Absolute path to directory containing malware apks")
    args.add_argument("--maldir", default= "/home/osboxes/Desktop/APK/MAL",
                      help= "Absolute path to directory containing malware apks")
    args.add_argument("--maldir_dest", default= "/home/osboxes/Desktop/APK/MAL/OUTPUT",
                      help= "Absolute path to directory where to store the malware output")
    args.add_argument("--gooddir", default= "/home/osboxes/Desktop/APK/",
                      help= "Absolute path to directory containing benign apks")
    args.add_argument("--gooddir_dest", default= "/home/osboxes/Desktop/APK/OUTPUT",
                      help= "Absolute path to directory where to store the benign output")
    args.add_argument("--testsize", type= float, default= 0.2,
                      help= "Size of the test set when split by Scikit Learn's Train Test Split module")

    return args.parse_args()

if __name__ == "__main__":
    Art = text2art('DrebinEasy')
    main(menu(), True)

