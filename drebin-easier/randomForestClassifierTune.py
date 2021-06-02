"""
This file is the implementation of GridSearch with Random Forest Classifier model
Source :    https://github.com/LiYangHart/Hyperparameter-Optimization-of-Machine-Learning-Algorithms
            https://github.com/sontung/drebin-malwares
"""
from sklearn.metrics import confusion_matrix as cm
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt


def randomForestClassifierGS(size_split):
    """
    Method used to call the Random Forest Classifier model with Grid Search
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
    # We specify the parameters that we want to test
    # Check here to see the parameters of Random Forest
    # https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
    rf_params = {
        'n_estimators': [10, 20, 30],
        'max_features': ["auto", "sqrt", "log2", None],
        'max_depth': [15, 20, 30, 50],
        "criterion": ['gini', 'entropy']
    }
    # We specify the scoring that we try to optimize
    # Check here to see which score you can add in the list
    # https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter
    scores = ["precision", "accuracy", "f1"]

    # We calculate the scoring
    for score in scores:
        print("# Tuning hyper-parameters for %s" % score)
        print("")

        # We create the GridSearch and train the model
        clf = GridSearchCV(RandomForestClassifier(), rf_params, cv=5, scoring=score, n_jobs=2)
        clf.fit(X_train, y_train)

        print("Best parameters set found on development set:")
        print("")
        # By default refit is True, then when you call one of those attribute, the refit is made with the best
        # parameters.
        print(clf.best_estimator_)
        print(clf.best_params_)
        print("")
        print("Grid scores on development set:")
        print("")
        print(clf.best_score_)
        print("")

        print("Detailed classification report:")
        print("")
        print("The model is selected with the best specified parameters")
        print("")

        # We test now the model and print classification report and confusion matrix
        y_true, y_pred = y_test, clf.predict(X_test)
        print(classification_report(y_true, y_pred))
        print("")
        RFC_cm = cm(y_test, y_pred)

        print(" ")

        print(RFC_cm)
        print(classification_report(y_pred, y_test, labels=None))

        # Show confusion matrix in a separate window
        plt.matshow(RFC_cm)
        plt.title('RFC Confusion matrix')
        plt.colorbar()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.show()

