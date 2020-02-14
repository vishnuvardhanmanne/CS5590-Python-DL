import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score, GridSearchCV, train_test_split

dataset = pd.read_csv('glass.csv')
X = dataset.drop('Type', axis=1)
y = dataset['Type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)

classifier = SVC(kernel='linear')
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(metrics.accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))
