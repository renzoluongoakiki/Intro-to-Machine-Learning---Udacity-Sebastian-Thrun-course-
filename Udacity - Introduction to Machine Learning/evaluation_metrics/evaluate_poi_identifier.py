#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, random_state=42, test_size=0.3)

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
print "score DecisionTreeClassifier 70% training: ",clf.score(features_test, labels_test)
pred = clf.predict(features_test)

import numpy as np
print "Hay {} personas en el test set".format(len(labels_test))
print "Hay {} personas en el test set predichas como POI".format(np.count_nonzero(pred == 1))
print "Hay {} personas en el test set predichas como NO POI".format(np.count_nonzero(pred == 0))
print "Hay {} personas en el test set que son POI".format(labels_test.count(1))
print "Hay {} personas en el test set que son NO POI".format(labels_test.count(0))

from sklearn.metrics import confusion_matrix, recall_score, precision_score

print "Confussion Matrix:"
print confusion_matrix(labels_test, pred)
print "Recall score:",recall_score(labels_test, pred)
print "Precision score:",precision_score(labels_test, pred)