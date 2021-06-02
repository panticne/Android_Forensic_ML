from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.metrics import confusion_matrix as cm
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

def kNeighborsClassifierGS(size_split):
    df = pd.read_csv('binaryApps_BEN.csv', sep=',')

    df2 = pd.read_csv('binaryApps_MAL.csv', sep=',')

    df = pd.concat([df, df2])
    label_encoder = LabelEncoder()
    output_integer_encoded = label_encoder.fit_transform(df['malware'])
    X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 1:-1], output_integer_encoded,
                                                        test_size=size_split, random_state=42)
    rf_params = {
        'n_neighbors': [2, 3, 5, 10, 15, 20],
    }
    scores = ["accuracy", "f1"]

    for score in scores:
        print("# Tuning hyper-parameters for %s" % score)
        print("")

        clf = GridSearchCV(KNeighborsClassifier(), rf_params, cv=5, scoring=score, n_jobs=2)
        clf.fit(X_train, y_train)

        print("Best parameters set found on development set:")
        print("")
        print(clf.best_estimator_)
        print(clf.best_params_)
        print("")
        print("Grid scores on development set:")
        print("")
        print(clf.best_score_)
        print("")

        print("Detailed classification report:")
        print("")
        print("The model is trained on the full development set.")
        print("The scores are computed on the full evaluation set.")
        print("")
        y_true, y_pred = y_test, clf.predict(X_test)
        print(classification_report(y_true, y_pred))

        K_cm = cm(y_test, y_pred)

        print(" ")

        print(K_cm)
        # Show confusion matrix in a separate window
        plt.matshow(K_cm)
        plt.title("K-N 3 matrix")
        plt.colorbar()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.show()
        print("")
        print("")
