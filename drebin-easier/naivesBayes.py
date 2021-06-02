"""
This file is the implementation of basic Naives Bayes model
Source : https://github.com/mokeam/malware-analysis/blob/master/scripts/Malware_Classification_Model.py
"""
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix as cm
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import pandas as pd


def naivesBayes(size_split):
    """
    Method used to call the Naives Bayes model
    :param size_split: Size of the test dataset
    :return: None
    """
    # Read both files and merge them
    df = pd.read_csv('binaryApps_BEN.csv', sep=',')
    df2 = pd.read_csv('binaryApps_MAL.csv', sep=',')
    df = pd.concat([df, df2])

    # We create the training and validation training dataset and the test and validation test dataset
    X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 1:-1], df['malware'],
                                                        test_size=size_split, random_state=42)
    # We create the model
    gnb = GaussianNB()
    # We train the model
    gnb.fit(X_train, y_train)

    # We test the model
    y_pred = gnb.predict(X_test)

    print("Naives Bayes")
    print(" ")

    # We print the report of the model and calculate the confusion_matrix
    print(classification_report(y_pred, y_test, labels=None))
    GNB_cm = cm(y_test, y_pred)
    print(GNB_cm)

    # Show confusion matrix in a separate window
    plt.matshow(GNB_cm)
    plt.title('Naive Gauss Confusion matrix')
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()


