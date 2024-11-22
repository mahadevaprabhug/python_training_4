"""
Seaborn: Plotting Graphs
"""

print("Inside Seaborn Library")
print("-"*20)
# --------------

import seaborn as sns
print(dir(sns))

print("#"*40, end="\n\n")
###################################

print("Get data from iris.csv")
print("-"*20)
# --------------

import pandas as pd
my_iris_data_df = pd.read_csv("Iris.csv")
print(my_iris_data_df.head(5)) # Top five rows

print("#"*40, end="\n\n")
###################################

print("Plotting graph Violin plot")
print("-"*20)
# --------------

import seaborn as sns
import matplotlib.pyplot as plt

sns.violinplot(data=my_iris_data_df, x="Species",y="SepalLengthCm")
plt.show()

print("#"*40, end="\n\n")
###################################


print("Plotting graph scatterplot")
print("-"*20)
# --------------

import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(data=my_iris_data_df, x="SepalWidthCm",y="SepalLengthCm")
plt.show()

print("#"*40, end="\n\n")
###################################
