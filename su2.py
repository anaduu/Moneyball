import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
def density_of_points(x,y):
     xy = np.vstack([x,y])
     z = gaussian_kde(xy)(xy) # Calculate the point density
     idx = z.argsort() # Sort the points by density, so that the densest points are plotted last
     x, y, z = x[idx], y[idx], z[idx]
     return (x,y,z)

DATA_LOCATION = "data1.csv"
FIRST_ATTRIBUTE = "Finishing"
SECOND_ATTRIBUTE = "Overall"

datas = pd.read_csv(DATA_LOCATION)
data1 = datas[[FIRST_ATTRIBUTE]]
data2 = datas[[SECOND_ATTRIBUTE]]

x = data1.values
y = data2.values



plt.scatter(x, y, z='viridis', s=20, edgecolor='',cmap='viridis')
