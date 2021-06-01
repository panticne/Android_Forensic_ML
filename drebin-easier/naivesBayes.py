from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix as cm
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import pandas as pd


def naivesBayes(size_split):
    df = pd.read_csv('binaryApps_BEN.csv', sep=',')

    df2 = pd.read_csv('binaryApps_MAL.csv', sep=',')

    df = pd.concat([df, df2])
    label_encoder = LabelEncoder()
    output_integer_encoded = label_encoder.fit_transform(df['malware'])
    X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 1:-1], output_integer_encoded,
                                                        test_size=size_split, random_state=42)
    # Naives Bayes algorithm
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)

    # y_pred
    y_pred = gnb.predict(X_test)

    print(" ")

    print(classification_report(y_pred, y_test, labels=None))
    GNB_cm = cm(y_test, y_pred)
    print(" ")
    print(GNB_cm)

    # Show confusion matrix in a separate window
    plt.matshow(GNB_cm)
    plt.title('Naive Gauss Confusion matrix')
    plt.colorbar()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()

