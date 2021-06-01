from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression as LG
from sklearn.metrics import confusion_matrix as cm
import pandas as pd
import matplotlib.pyplot as plt

def linearRegression(size_split):

    df = pd.read_csv('binaryApps_BEN.csv', sep=',')

    df2 = pd.read_csv('binaryApps_MAL.csv', sep=',')

    df = pd.concat([df, df2])

    label_encoder = LabelEncoder()
    output_integer_encoded = label_encoder.fit_transform(df['malware'])
    print(df)
    print(output_integer_encoded)
    X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 1:-1], output_integer_encoded,
                                                        test_size=size_split, random_state=42)

    # Train our model with LogisticRegression
    clf = LG().fit(X_train, y_train)

    # Model Prediction
    y_pred = clf.predict(X_test)

    print("Logistic Regression")

    print(" ")
    LG_cm = cm(y_test, y_pred)

    print(LG_cm)

    print(classification_report(y_pred, y_test, labels=None))

    plt.matshow(LG_cm)
    plt.title('LG Confusion matrix')
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
