"""
This file is the implementation of basic Random Forest Classifier model
Source : https://github.com/mokeam/malware-analysis/blob/master/scripts/Malware_Classification_Model.py
"""
from sklearn.metrics import confusion_matrix as cm
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import matplotlib.pyplot as plt


def randomForestClassifier(size_split):
    """
    Method used to call the Random Forest Classifier model
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

    RFC_clf = RandomForestClassifier()
    # We create the model
    RFC_clf = RFC_clf.fit(X_train, y_train)

    # We now test the model
    y_pred = RFC_clf.predict(X_test)

    print("Random Forest")
    print(" ")

    # We print the report of the model and calculate the confusion_matrix
    RFC_cm = cm(y_test, y_pred)
    print(classification_report(y_pred, y_test, labels=None))
    print(RFC_cm)
    # Show confusion matrix in a separate window
    plt.matshow(RFC_cm)
    plt.title('RFC Confusion matrix')
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()


