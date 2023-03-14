import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
import numpy as np
from sklearn.linear_model import LinearRegression
import math
import matplotlib.pyplot as plt
import pandas as pd

#defining the matricies with the data that was collected from our experiment / known quantities
elementaryCharge = 1.602 * math.pow(10, -19)
speedOfLight = 299792458
frequencies = np.array([speedOfLight / 365, speedOfLight / 404, speedOfLight / 435.7, 
                        speedOfLight / 546, speedOfLight / 577]).reshape((-1, 1))
cutoffVoltagesTimesEC = np.array([7.25, 7.25, 7.75, 7.5, 7.25])

#fitting linear regression 
model = LinearRegression().fit(frequencies, cutoffVoltagesTimesEC)

#printing out the slope, intercept and r^2 values for the 
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")

r_sq = model.score(frequencies, cutoffVoltagesTimesEC)
print(f"coefficient of determination: {r_sq}")

frequencies1 = np.array([speedOfLight / 365, speedOfLight / 404, speedOfLight / 435.7, 
                         speedOfLight / 546, speedOfLight / 577])
cutoffVoltagesTimesEC1 = np.array([7.25,7.25,7.75,7.5,7.25])

a, b = np.polyfit(frequencies1, cutoffVoltagesTimesEC1, 1)
plt.scatter(frequencies1, cutoffVoltagesTimesEC1)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Cutoff Voltage')
plt.title('Frequency (Hz) vs Cutoff Voltage for the Photoelectric Effect Experiment')
plt.plot(frequencies1, a*frequencies1+b)

