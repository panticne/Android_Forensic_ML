"""
This file is the implementation of basic Linear Regression model
Source : https://github.com/mokeam/malware-analysis/blob/master/scripts/Malware_Classification_Model.py
"""
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as LG
from sklearn.metrics import confusion_matrix as cm
import pandas as pd
import matplotlib.pyplot as plt

def linearRegression(size_split):
    """
    Method used to call the Linear Regression Model
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

    # We create and test the model
    clf = LG().fit(X_train, y_train)

    # We now test the model
    y_pred = clf.predict(X_test)

    # We print the report of the model and calculate the confusion_matrix
    print("Linear Regression")
    print(" ")
    LG_cm = cm(y_test, y_pred)
    print(classification_report(y_pred, y_test, labels=None))
    print(LG_cm)
    
    plt.matshow(LG_cm)
    plt.title('LG Confusion matrix')
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()

