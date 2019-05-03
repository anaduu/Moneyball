from random import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import mean
from numpy import std
from scipy.stats import shapiro
from scipy.stats import normaltest
DATA_LOCATION = "data1.csv"
FIRST_ATTRIBUTE = "ID"

datas = pd.read_csv(DATA_LOCATION)
data1 = datas[FIRST_ATTRIBUTE]
import random
print (random.choice(data1)
