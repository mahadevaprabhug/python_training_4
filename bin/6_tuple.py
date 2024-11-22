"""
IMMUTABLE
- Tuple:
    -- We already have option to store collection of values like list of names, list of email-ids etc
    -- We can store DUPLICATE values
    -- Automatically Index number will be assigned to each values
"""

print("Tuple PART-1")
print("How to store values?")
print("-"*20)
# --------------

my_tuple = (10, 12.5, "python", "python", "Java", (100, 200))
# We can store any type of values
# It will create object of 'tuple' class
print("my_tuple:", my_tuple)

print("#"*40, end="\n\n")
###################################

print("Tuple PART-2")
print("Indexing will work similar string")
print("-"*20)
# --------------

my_tuple = (10, 12.5, "python", "python", "Java", (100, 200))
print("my_tuple:", my_tuple, end="\n\n")

print("course name:", my_tuple[2]) # "python"
print("2nd character course name:", my_tuple[2][1], end="\n\n") # "y"

print("Inner tuple:", my_tuple[-1]) # (100, 200)
print("Last value in Inner tuple:", my_tuple[-1][-1]) # (100, 200)

print("#"*40, end="\n\n")
###################################

print("Tuple PART-3")
print("Methods present in tuple class")
print("-"*20)
# --------------

print(dir(my_tuple))
# OR
# print(dir(tuple))

print("#"*40, end="\n\n")
###################################

print("Tuple PART-4")
print("'count' and 'index' methods")
print("-"*20)
# --------------

my_tuple = (10, 12.5, "python", "python", "Java", (10, 20))
print("my_tuple:", my_tuple, end="\n\n")

count_of_10 = my_tuple.count(10) # 1
count_of_10_inner_tuple = my_tuple[-1].count(10)

index_of_10 = my_tuple.index(10)
index_of_y = my_tuple[2].index('y')

print("count_of_10:", count_of_10)
print("count_of_10_inner_tuple:", count_of_10_inner_tuple)
print("index_of_10:", index_of_10)
print("index_of_y:", index_of_y)

print("#"*40, end="\n\n")
###################################
