# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/175zc-_pYrp8yGVawz_bQotpbYJR0YW2Y
"""

# Use the !wget command to download a file
!wget -O "./pima-indians-diabetes-database.csv" "https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database.csv"

from google.colab import files
u= files.upload()

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import export_graphviz
import graphviz

col_names=['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']
pima = pd.read_csv("diabetes.csv",header = None,names=col_names)
pima_df = pima.head()
print(pima_df)

feature_cols =['pregnant','insulin','bmi','age','glucose','bp','pedigree']
X = pima[feature_cols]
y = pima.label

feature_cols = ['pregnant','insulin','bmi','age','glucose','bp','pedigree']
X = pima[feature_cols]
y = pima.label

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3, random_state = 1)

clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

dot_data = export_graphviz(clf,out_file=None,feature_names=X_train.columns,class_names=[str(x) for x in clf.classes_],filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("decision_tree")
graph.view("decision_tree")

clf = DecisionTreeClassifier(criterion = "entropy", max_depth=3)
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

dot_data = export_graphviz(clf,out_file=None,feature_names=X_train.columns,class_names=[str(x) for x in clf.classes_],filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("decision_tree")
graph.view("decision_tree")