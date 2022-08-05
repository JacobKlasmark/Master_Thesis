import numpy as np
import sys
import matplotlib.pyplot as plt
import time

from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import train_test_split
from scipy import sparse
from scipy.sparse import csr_matrix

#Machine learning models
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

data_file_path = "/home/kali/Master_Thesis/dataset2/3_3_20k_dataset/3_3_20k_svm"
X, y = load_svmlight_file(data_file_path)
y = y.astype(int)
y_sparse = sparse.csr_matrix(y)
y_sparse = y_sparse[0]
y_sparse = y_sparse.transpose()

X_train, X_test, y_train, y_test = train_test_split(X, y_sparse, test_size=0.2, random_state=4) 

del X
del y_sparse
del y

#clf_1 = MultinomialNB()
#clf_1 = LogisticRegression()
#clf_1 = LinearSVC()
#clf_1 = RandomForestClassifier()

y_train = csr_matrix.toarray(y_train)
y_train = y_train.flatten()
y_test = csr_matrix.toarray(y_test)
y_test = y_test.flatten()

#MultinomialNB
grid = {
    'alpha': [0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000],
    'fit_prior': [True, False]
}

#LinearSVC
grid = {
    'penalty': ['l2'], 
    'loss': ['hinge'], 
    'dual': [True], 
    'C': [0.1, 5, 10, 50, 100, 1000],
    'max_iter': [100] 
}

#LogisticRegression
grid = {
    'penalty': ['l2'],
    'dual': [False],
    'C': [0.01, 0.1, 1, 10, 100, 1000],
    'random_state': [4],
    'max_iter': [100],
    'solver': ['saga'],
    'multi_class': ['multinomial']
}

#RandomForestClassifier
grid = {
    'n_estimators': [100, 200, 600, 1000],
    'max_features': ['sqrt'],
    'max_depth': [50, 60, 70, 80, 90, 100, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1,2,4],
    'bootstrap': [False],
    'max_samples': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, None],
    'random_state': [4]

}
'''
'''

start = time.time()
clf = GridSearchCV(clf_1, grid, n_jobs=1, cv=5, verbose=3).fit(X_train, y_train)

print("best estimators")
print(clf.best_estimator_)
print("best_params ")
print(clf.best_params_)
print("best_score")
print(clf.best_score_)

y_pred = clf.predict(X_test)
end = time.time()

del X_train
del y_train
title = "Normalized confusion matrix"
disp = ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred,
    cmap=plt.cm.Blues,
    normalize="true",
)
plt.show()

correct = ((y_test == y_pred).sum()).item()

print(correct)
total = X_test.shape[0]
print(total)
ratio = correct / total
print(ratio)

model_file_path = '/home/kali/Master_Thesis/saved_models/3_3_20k_RandomForest.sav'
pickle.dump(clf, open(model_file_path, 'wb'))
