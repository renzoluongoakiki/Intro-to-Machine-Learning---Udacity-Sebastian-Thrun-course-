#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
# Nano sacando el outlier agrego 1 linea
data_dict.pop("TOTAL",0)
# Termina codigo Nano
data = featureFormat(data_dict, features)


### your code below
print data.max()

salary_1M_bonus_5M = []
for key in data_dict:
	salary = data_dict[key]['salary']
	bonus = data_dict[key]['bonus']
	if salary>1000000 and salary!="NaN" and bonus>5000000 and bonus!="NaN":
		salary_1M_bonus_5M.append((key, salary, bonus))

print salary_1M_bonus_5M

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# Otra forma de quedarse con los 2 salarios mas altos (http://napitupulu-jon.appspot.com/posts/outliers-ud120.html#TOTAL)
"""
outliers = []
for key in data_dict:
    val = data_dict[key]['salary']
    if val == 'NaN':
        continue
    outliers.append((key,int(val)))

pprint(sorted(outliers,key=lambda x:x[1],reverse=True)[:2])
"""

# Termina codigo Nano

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


