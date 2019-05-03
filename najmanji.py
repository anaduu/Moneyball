import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import mean
from numpy import std
from scipy.stats import shapiro
from scipy.stats import normaltest
DATA_LOCATION = "data1.csv"
FIRST_ATTRIBUTE = "Overall"

datas = pd.read_csv(DATA_LOCATION)
data1 = datas[FIRST_ATTRIBUTE]
print(std(data1))
print(mean(data1))
# normality test
stat, p = normaltest(data1)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Sample looks Gaussian (fail to reject H0)')
else:
	print('Sample does not look Gaussian (reject H0)')
pd.read_csv('data1.csv', quoting=2)['Overall'].hist(bins=49)
plt.show()


