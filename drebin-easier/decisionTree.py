from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix as cm

def decisionTree(size_split):
    df = pd.read_csv('binaryApps_BEN.csv', sep=',')

    df2 = pd.read_csv('binaryApps_MAL.csv', sep=',')

    df = pd.concat([df, df2])
    label_encoder = LabelEncoder()
    output_integer_encoded = label_encoder.fit_transform(df['malware'])
    X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 1:-1], output_integer_encoded,
                                                        test_size=size_split, random_state=42)
    # Decision Tree Classifier
    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)


    y_pred = clf.predict(X_test)
    # accuracy

    print(classification_report(y_pred, y_test, labels=None))
    DTC_cm = cm(y_test, y_pred)

    print(" ")
    
    print(DTC_cm)
    # Show confusion matrix in a separate window
    plt.matshow(DTC_cm)
    plt.title('Decistion Tree matrix')
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
