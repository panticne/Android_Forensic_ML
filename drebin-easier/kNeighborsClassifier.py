"""
This file is the implementation of basic k-Neighbors Classifier model
Source : https://github.com/mokeam/malware-analysis/blob/master/scripts/Malware_Classification_Model.py
"""
from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix as cm


def kNeighborsClassifier(size_split):
    """
    Method used to call the k-Neighbors Classifier model
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
    # We initiate it with 3 neighbors
    neigh = KNeighborsClassifier()

    # We train the model
    neigh.fit(X_train, y_train)
    # We test the model
    y_pred = neigh.predict(X_test)

    print("k-Neighbors 3")
    print(" ")

    # We print the report of the model and calculate the confusion_matrix
    print(classification_report(y_pred, y_test, labels=None))
    K_cm = cm(y_test, y_pred)
    print(K_cm)

    # Show confusion matrix in a separate window
    plt.matshow(K_cm)
    plt.title("K-N 3 matrix")
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
    print("")

