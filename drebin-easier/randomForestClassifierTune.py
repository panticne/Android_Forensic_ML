from sklearn.metrics import confusion_matrix as cm
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

def randomForestClassifierGS(size_split):
    df = pd.read_csv('binaryApps_BEN.csv', sep=',')

    df2 = pd.read_csv('binaryApps_MAL.csv', sep=',')

    df = pd.concat([df, df2])
    label_encoder = LabelEncoder()
    output_integer_encoded = label_encoder.fit_transform(df['malware'])
    X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 1:-1], output_integer_encoded,
                                                        test_size=size_split, random_state=42)
    rf_params = {
        'n_estimators': [10, 20, 30],
        'max_features': ["auto", "sqrt", "log2", None],
        'max_depth': [15, 20, 30, 50],
        # 'min_samples_leaf': [1,2,4,8],
        # "bootstrap":[True,False],
        "criterion": ['gini', 'entropy']
    }
    scores = ["accuracy", "f1"]

    for score in scores:
        print("# Tuning hyper-parameters for %s" % score)
        print("")

        clf = GridSearchCV(RandomForestClassifier(), rf_params, cv=5, scoring=score, n_jobs=2)
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
