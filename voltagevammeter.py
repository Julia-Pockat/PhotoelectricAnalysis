import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
import numpy as np
from sklearn.linear_model import LinearRegression
import math
import matplotlib.pyplot as plt
import pandas as pd

# work for plotting the retarding voltage vs picoammeter reading 

#creating dataframes with the data
df_365 = pd.DataFrame()
df_365 = pd.read_csv("Photoelectric data  - 365nm.csv")

df_404 = pd.DataFrame()
df_404 = pd.read_csv("Photoelectric data  - 404nm.csv")

df_435_7 = pd.DataFrame()
df_435_7 = pd.read_csv("Photoelectric data  - 435.7nm.csv")

df_546 = pd.DataFrame()
df_546 = pd.read_csv("Photoelectric data  - 546nm.csv")

df_577 = pd.DataFrame()
df_577 = pd.read_csv("Photoelectric data  - 577nm.csv")
print(df_577)

plt.scatter(df_365["Voltage V"], df_365["Current (nA) 2"], c='b')
plt.scatter(df_404["Voltage V"], df_404["Current (nA) 3"], c='r')
plt.scatter(df_435_7["Voltage V"], df_435_7["Current (nA) 2"], c='y')
plt.scatter(df_546["Voltage V"], df_546["Current (nA) 2"], c='#ff7f0e')
plt.scatter(df_577["Voltage V"], df_577["Current (nA) 1"])

plt.xlabel('Picoammeter Reading (nA)')
plt.ylabel('Voltage V')
plt.title('Picoammeter Reading (nA) vs Voltage V for the Photoelectric Effect Experiment')