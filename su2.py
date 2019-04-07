import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


DATA_LOCATION = "data1.csv"
FIRST_ATTRIBUTE = "Finishing"
SECOND_ATTRIBUTE = "Overall"

datas = pd.read_csv(DATA_LOCATION)
data1 = datas[[FIRST_ATTRIBUTE, SECOND_ATTRIBUTE]]

K = data1.values
plt.scatter(K[:,0], K[:,1], color = 'g')
plt.show()
