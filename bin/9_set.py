"""
IMMUTABLE
- set:
    -- We already have option to store collection of values like list of names, list of email-ids etc
    -- We can ONLY store UNIQUE values
    -- No index number to each value
"""

print("set PART-1")
print("Store the values")
print("-"*20)
# --------------

my_fs_1 = set()
print("my_fs_1:", my_fs_1)

my_fs_2 = set([10, 10, "python", "python", "Java", "Java"])
print("my_fs_2:", my_fs_2)

my_fs_3 = {10, 10, "python", "python", "Java", "Java"}
print("my_fs_3:", my_fs_3)

my_tuple = tuple(my_fs_2)
my_list = list(my_fs_2)

print("my_tuple:", my_tuple)
print("my_list:", my_list)

print("#"*40, end="\n\n")
###################################

print("set PART-2")
print("Methods present in set class")
print("-"*20)
# --------------

print(dir(my_fs_1))
# OR
# print(dir(set))

print("#"*40, end="\n\n")
###################################


print("set PART-3")
print("'union', 'intersection', 'difference' methods")
print("-"*20)
# --------------

my_course_1 = set(["java", "python", "c", "c++"])
my_course_2 = set(["c", "c++", "shell", "perl"])
print("my_course_1:", my_course_1)
print("my_course_2:", my_course_2)

all_courses = my_course_1.union(my_course_2)
common_courses = my_course_1.intersection(my_course_2)
only_in_course_1 = my_course_1.difference(my_course_2)

print("all_courses:", all_courses)
print("common_courses:", common_courses)
print("only_in_course_1 not in course_2:", only_in_course_1)

print("#"*40, end="\n\n")
###################################

print("set PART-4")
print("Add/Remove/Update")
print("-"*20)
# --------------

my_courses = {"java", "python", "c", "c++"}
print("my_courses:", my_courses, end="\n\n")

# Add
my_courses.add("Perl")
print("my_courses after adding perl:", my_courses, end="\n\n")

# Remove
my_courses.remove("Perl")
print("my_courses after removing perl:", my_courses, end="\n\n")

# Update
new_set = {"shell", "go", "pascal"}
my_courses.update(new_set)
print("my_courses after update/MERGE:", my_courses, end="\n\n")

print("#"*40, end="\n\n")
###################################
