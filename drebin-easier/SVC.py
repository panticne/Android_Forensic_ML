"""
This file is the implementation of basic SVC model
Source : https://github.com/mokeam/malware-analysis/blob/master/scripts/Malware_Classification_Model.py
"""
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn import svm


def SVC(size_split):
    """
    Method used to call the SVC model
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

    # We normalize and standardize the value with all the dataset
    # Source : https://stackoverflow.com/questions/40758562/can-anyone-explain-me-standardscaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # We create the SVC classifier and apply, poly will generate really bad prediction, the tuning will found the
    # appropriated kernel
    classifier = svm.SVC(kernel = 'poly')
    # We train the model
    classifier.fit(X_train, y_train)

    # We now test the model
    y_pred = classifier.predict(X_test)

    print("SVC")
    print(" ")

    # We print the report of the model and calculate the confusion_matrix
    print(classification_report(y_pred, y_test, labels=None))
    SVC_cm = confusion_matrix(y_test, y_pred)
    print(SVC_cm)
    # Show confusion matrix in a separate window
    plt.matshow(SVC_cm)
    plt.title('SVC matrix')
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
    print("")

