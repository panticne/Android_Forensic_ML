from sklearn.metrics import confusion_matrix as cm
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import matplotlib.pyplot as plt

def randomForestClassifier(size_split):
    df = pd.read_csv('binaryApps_BEN.csv', sep=',')

    df2 = pd.read_csv('binaryApps_MAL.csv', sep=',')

    df = pd.concat([df, df2])
    label_encoder = LabelEncoder()
    output_integer_encoded = label_encoder.fit_transform(df['malware'])
    X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 1:-1], output_integer_encoded,
                                                        test_size=size_split, random_state=42)
    RFC_clf = RandomForestClassifier()
    RFC_clf = RFC_clf.fit(X_train, y_train)

    # Model Prediction
    y_pred = RFC_clf.predict(X_test)

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
