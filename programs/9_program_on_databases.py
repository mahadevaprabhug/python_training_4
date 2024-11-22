"""
Get data from log file

then

extract IP & PICS using regex

then

Write extracted data to database
"""

"""
How to communicate with Databases in python?

python-program  <--communicate using library-->  any database(sql/No-sql)

Example:
python-program  <--communicate using library(cx-oracle)-->  Oracle database
python-program  <--communicate using library(mysql.connector)-->  MySQL database
python-program  <--communicate using library(sqlite3)-->  SQLite database
"""

"""
We need one database.
- We can use SQLite database
- SQLite database lightweight database
- SQLite database is not running any database server,
    it is serverless database. It will just create one database file
"""

"""
How to install/communicate with SQLite database?

2 Ways
1-way: Using SQLIte database software
2-way: Without using SQLIte database software. Using python library (sqlite3) we can create & communicate
        with database.
"""

print("Create database and table if not present")
print("-"*20)
# --------------

import sqlite3

print("Creating/Connecting to database")
my_db_connection = sqlite3.connect("my_database.sqlite3")
print("Done\n")

print("Create cursor object in order to execute SQL queries & fetch results")
my_db_cursor = my_db_connection.cursor()
print("Done\n")

print("Create table if not present")
my_query = """
CREATE TABLE IF NOT EXISTS MY_TABLE(
IP VARCHAR(100),
PICS VARCHAR(100)
)
"""
my_db_cursor.execute(my_query)
print("Done\n")

print("#"*40, end="\n\n")
###################################

print("Get data from web_server.log")
print("-"*20)
# --------------

my_log_file_handle = open(r"../log/web_server.log", "rb")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
###################################

print("Extract IP, PICS and write to database")
print("-"*20)
# --------------

import re

for each_value in log_file_content:
    match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(GET|POST|PUT|PATCH|DELETE)\s+/(pics/(\w+\.(gif|jpg)))?.*\s+HTTP.*', each_value)
    if match_result is not None:
        ip = match_result.group(1)
        ip = ip.decode()
        img = match_result.group(4)
        if img is not None:
            img = img.decode()
        else:
            img = "No Image"
        my_query = f"INSERT INTO MY_TABLE VALUES('{ip}', '{img}')"
        print("Executing Query:", my_query)
        my_db_cursor.execute(my_query)
        print("One Record Inserted")
my_db_connection.commit()
print("All records are inserted. Please check my_database")

print("#"*40, end="\n\n")
###################################

print("get data from database")
print("-"*20)
# --------------

my_query = "SELECT * FROM MY_TABLE"
my_db_cursor.execute(my_query)
my_db_result = my_db_cursor.fetchall()
print(my_db_result)
print(dir(my_db_connection))
my_db_connection.close()

print("#"*40, end="\n\n")
###################################
