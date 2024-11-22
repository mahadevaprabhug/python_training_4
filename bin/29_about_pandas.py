"""
Pandas Library
- It has many functions & classes in it
- Few function names are: read_csv, read_excel etc
- Few class names are: DataFrame, Series etc

About DataFrame class
- DataFrame is main class
- DataFrame class is written for working on tabular data like csv, xlsx etc
"""

print("Inside pandas library")
print("-"*20)
# --------------

import pandas as pd
print(dir(pd))

print("#"*40, end="\n\n")
###################################

print("Inside DataFrame class")
print("-"*20)
# --------------

import pandas as pd
print(dir(pd.DataFrame))

print("#"*40, end="\n\n")
###################################

print("Store Values in DataFrame Example-1")
print("-"*20)
# --------------

my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
print(my_df)

print("#"*40, end="\n\n")
###################################

print("Store Values in DataFrame Example-2")
print("-"*20)
# --------------

my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]],
                     index=["r1", "r2", "r3"],
                     columns=["c1", "c2", "c3", "c4"]
                     )
print(my_df)

print("#"*40, end="\n\n")
###################################
