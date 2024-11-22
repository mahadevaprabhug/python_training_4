"""
MUTABLE
- List:
    -- We already have option to store collection of values like list of names, list of email-ids etc
    -- We can store DUPLICATE values
    -- Automatically Index number will be assigned to each values
"""

print("list PART-1")
print("How to store values?")
print("-"*20)
# --------------

my_list = [10, 12.5, "python", "python", "Java", (100, 200)]
# We can store any type of values
# It will create object of 'list' class
print("my_list:", my_list)

print("#"*40, end="\n\n")
###################################

print("list PART-2")
print("Indexing will work similar string")
print("-"*20)
# --------------

my_list = [10, 12.5, "python", "python", "Java", (100, 200)]
print("my_list:", my_list, end="\n\n")

print("course name:", my_list[2]) # "python"
print("2nd character course name:", my_list[2][1], end="\n\n") # "y"

print("Inner list:", my_list[-1]) # (100, 200)
print("Last value in Inner list:", my_list[-1][-1]) # (100, 200)

print("#"*40, end="\n\n")
###################################

print("list PART-3")
print("Methods present in list class")
print("-"*20)
# --------------

print(dir(my_list))
# OR
# print(dir(list))

print("#"*40, end="\n\n")
###################################

print("list PART-4")
print("'count' and 'index' methods")
print("-"*20)
# --------------

my_list = [10, 12.5, "python", "python", "Java", (10, 20)]
print("my_list:", my_list, end="\n\n")

count_of_10 = my_list.count(10) # 1
count_of_10_inner_list = my_list[-1].count(10)

index_of_10 = my_list.index(10)
index_of_y = my_list[2].index('y')

print("count_of_10:", count_of_10)
print("count_of_10_inner_list:", count_of_10_inner_list)
print("index_of_10:", index_of_10)
print("index_of_y:", index_of_y)

print("#"*40, end="\n\n")
###################################


print("list PART-5")
print("ADD/UPDATE/REMOVE")
print("-"*20)
# --------------

my_list = [10, 12.5, "python", "python", "Java", (10, 20)]
print("my_list:", my_list, end="\n\n")


# Add "PERL"
my_list.append("Perl") # [10, 12.5, "python", "python", "Java", (10, 20), "Perl]
print("my_list after adding perl:", my_list, end="\n\n")

# Update 12.5 to "C++"
my_list[1] = "C++"
print("my_list after updating 12.5 to c++:", my_list, end="\n\n")

# Delete
my_list.pop(2)
print("my_list after removing index 2:", my_list, end="\n\n")

print("#"*40, end="\n\n")
###################################

print("list PART-6")
print("trying 'insert' method")
print("-"*20)
# --------------

my_list = [10, 12.5, "python", "python", "Java", (10, 20)]
print("my_list:", my_list, end="\n\n")

my_list.insert(-1, 1000)
print("my_list after insert:", my_list, end="\n\n")

print("#"*40, end="\n\n")
###################################

