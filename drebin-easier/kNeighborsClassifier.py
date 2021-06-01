from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix as cm


def kNeighborsClassifier(size_split):
    df = pd.read_csv('binaryApps_BEN.csv', sep=',')

    df2 = pd.read_csv('binaryApps_MAL.csv', sep=',')

    df = pd.concat([df, df2])
    label_encoder = LabelEncoder()
    output_integer_encoded = label_encoder.fit_transform(df['malware'])
    X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, 1:-1], output_integer_encoded,
                                                        test_size=size_split, random_state=42)
    for i in range(3, 30, 3):
        neigh = KNeighborsClassifier(n_neighbors=i)
        neigh.fit(X_train, y_train)
        y_pred = neigh.predict(X_test)

        print("kneighbors {}".format(i))

        print(classification_report(y_pred, y_test, labels=None))
        K_cm = cm(y_test, y_pred)

        print(" ")
        
        print(K_cm)
        # Show confusion matrix in a separate window
        plt.matshow(K_cm)
        plt.title("K-N {} matrix".format(i))
        plt.colorbar()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.show()
        print("")
