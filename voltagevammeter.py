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
df_365 = pd.read_csv("Photoelectric data  - 404nm.csv")

df_435_7 = pd.DataFrame()
df_435_7 = pd.read_csv("Photoelectric data  - 435.7nm.csv")

df_546 = pd.DataFrame()
df_546 = pd.read_csv("Photoelectric data  - 546nm.csv")

df_577 = pd.DataFrame()
df_577 = pd.read_csv("Photoelectric data  - 577nm.csv")
print(df_365['Voltage V'])
print(df_365['Current (nA) 2'])
plt.scatter(df_365["Voltage V"], df_365["Current (nA) 2"])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Cutoff Voltage')
plt.title('Frequency (Hz) vs Cutoff Voltage for the Photoelectric Effect Experiment')