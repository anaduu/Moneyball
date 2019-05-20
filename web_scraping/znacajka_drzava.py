import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math 
class par:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        else:
            return self.x < other.x
def udaljenost(a,b):
                    sol=0
                    for i in range(0,26):
                        sol=sol+((K[b][i]-K[a][i])**2)
                    return sol**(1/float(2))


DATA_LOCATION = "data1.csv"
FIRST_ATTRIBUTE = "Overall"
SECOND_ATTRIBUTE = "Nationality"
datas = pd.read_csv(DATA_LOCATION)
data1 = datas[[FIRST_ATTRIBUTE, SECOND_ATTRIBUTE]]

K = data1.values
#plt.scatter(K[:,0], K[:,1], K[:,2],color = 'g')
#plt.show()
drzave ={""}
for i in range(1,len(K)):
    drzave.add(K[i][1])
print(len(drzave))
for k in drzave:
    for i in range(1,len(K)):
        if(K[i][1]==k):

    print(k)
print(drzave[0])
