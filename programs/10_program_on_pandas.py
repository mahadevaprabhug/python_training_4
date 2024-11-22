"""
Get data from database and
write to
db_dump_1.csv
db_dump_2.xlsx
db_dump_3.json
db_dump_4.xml
"""

print("Get data from database")
print("-"*20)
# --------------

import sqlite3
my_db_connection = sqlite3.connect("my_database.sqlite3")

import pandas as pd
my_db_df = pd.read_sql("SELECT * FROM MY_TABLE", my_db_connection)
print(my_db_df)

print("#"*40, end="\n\n")
###################################

print("Type of my_db_df")
print("-"*20)
# --------------

print(type(my_db_df))

print("#"*40, end="\n\n")
###################################

print("Remove duplicate rows")
print("-"*20)
# --------------

my_db_df = my_db_df.drop_duplicates()
print(my_db_df)

print("#"*40, end="\n\n")
###################################

print("Replace 'No Image' with 'abc.jpg'")
print("-"*20)
# --------------

my_db_df = my_db_df.replace(['No Image'], "abc.jpg")
print(my_db_df)

print("#"*40, end="\n\n")
###################################

print("Get list of columns")
print("-"*20)
# --------------

print(my_db_df.columns)

print("#"*40, end="\n\n")
###################################

print("Add new column IP_WITH_PORT")
print("-"*20)
# --------------

my_db_df["IP_WITH_PORT"] = my_db_df["IP"] + ":8080"
# If column present then update else add new column
print(my_db_df)

print("#"*40, end="\n\n")
###################################

print("Slicing Example")
print("-"*20)
# --------------

try:
    # my_db_df[rows,columns]
    print("One cell:", my_db_df.iloc[0,0])
    print("One row:", my_db_df.iloc[0,:])
    print("One columns:", my_db_df.iloc[:,0])
except Exception as e:
    print("Error occurred while slicing and details:", e)

print("#"*40, end="\n\n")
###################################

print("write to files")
print("-"*20)
# --------------

# db_dump_1.csv
my_db_df.to_csv("db_dump_1.csv", index=None)

# db_dump_2.xlsx
my_db_df.to_excel("db_dump_2.xlsx", index=None)

# db_dump_3.json
my_db_df.to_json("db_dump_3.json")

# db_dump_4.xml
my_db_df.to_xml("db_dump_4.xml")

# Convert row to column
temp_df = my_db_df.T
temp_df.to_json("db_dump_5.json")

print("""
Below files are created
db_dump_1.csv
db_dump_2.xlsx
db_dump_3.json
db_dump_4.xml
db_dump_5.json
please check
""")

print("#"*40, end="\n\n")
###################################
