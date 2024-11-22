"""
IMMUTABLE
- Frozenset:
    -- We already have option to store collection of values like list of names, list of email-ids etc
    -- We can ONLY store UNIQUE values
    -- No index number to each value
"""

print("Frozenset PART-1")
print("Store the values")
print("-"*20)
# --------------

my_fs_1 = frozenset()
print("my_fs_1:", my_fs_1)

my_fs_2 = frozenset([10, 10, "python", "python", "Java", "Java"])
print("my_fs_2:", my_fs_2)

my_tuple = tuple(my_fs_2)
my_list = list(my_fs_2)

print("my_tuple:", my_tuple)
print("my_list:", my_list)

print("#"*40, end="\n\n")
###################################

print("Frozenset PART-2")
print("Methods present in frozenset class")
print("-"*20)
# --------------

print(dir(my_fs_1))
# OR
# print(dir(frozenset))

print("#"*40, end="\n\n")
###################################


print("Frozenset PART-3")
print("'union', 'intersection', 'difference' methods")
print("-"*20)
# --------------

my_course_1 = frozenset(["java", "python", "c", "c++"])
my_course_2 = frozenset(["c", "c++", "shell", "perl"])
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
