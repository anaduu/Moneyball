import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math 
import csv
import os 
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus
DATA_LOCATION = "data/main_players.csv"
FIRST_ATTRIBUTE = "LS"
SECOND_ATTRIBUTE = "ST"
treci="RS"
cetvrti="LW"
peti="LF"
sest="CF"
sedam="RF"
osam="RW"
devet="LAM"
deset="CAM"
jed="RAM"
dva="LM"
tri="CM"
cet="RCM"
pet="RM"
ses="LWB"
sed="LDM"
osa="CDM"
dev="RDM"
dvades="RWB"
djed="LB"
ddva="LCB"
dtri="CB"
dcet="RCB"
dpet="RB"
dses="LCM"
dsed="FKAccuracy"
ddev="Finishing"
trides="Aggression"
trijed="Interceptions"
tridva="Marking"
tritri="StandingTackle"
tricet="SlidingTackle"
tripet="LongShots"
trises="Dribbling"
dosa="Overall"
datas = pd.read_csv(DATA_LOCATION)
data1 = datas[[FIRST_ATTRIBUTE, SECOND_ATTRIBUTE, treci,cetvrti,peti,peti,sest,sedam,osam,devet,deset,jed,dva,tri,cet,pet,ses,sed,osa,dev,dvades,djed,ddva,dtri,dcet,dpet,dses,dsed,ddev,trides,trijed,tridva,tritri,tricet,dosa]]
datas1=pd.read_csv("data/end_players.csv")
data2=datas[[FIRST_ATTRIBUTE, SECOND_ATTRIBUTE, treci,cetvrti,peti,peti,sest,sedam,osam,devet,deset,jed,dva,tri,cet,pet,ses,sed,osa,dev,dvades,djed,ddva,dtri,dcet,dpet,dses,ddev,trides,trijed,tridva,tritri,tricet,tripet,trises,dosa]]
print(data1.head())
#split dataset in features and target variable
feature_cols = [FIRST_ATTRIBUTE, SECOND_ATTRIBUTE, treci,cetvrti,peti,peti,sest,sedam,osam,devet,deset,jed,dva,tri,cet,pet,ses,sed,osa,dev,dvades,djed,ddva,dtri,dcet,dpet,dses,ddev,trides,trijed,tridva,tritri,tricet,tripet,trises]
X_train = datas[feature_cols] # Features
y_train = datas.pozicija # Target variable
X_test  = datas1[feature_cols]
y_test  = datas1.pozicija 
clf = DecisionTreeClassifier(criterion="entropy", max_depth=5)

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

