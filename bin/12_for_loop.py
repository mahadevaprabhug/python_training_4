"""
for-loop: Iterate any collection like str, list etc
"""

print("Iterate any collection like str, list etc")
print("-"*20)
# --------------

my_string = "Python"
my_list = [100, "python", "Java"]
my_dictionary = {"course": "python", "mode": "online"}

for i in my_string:
    print("Each char in my_string:", i)

print("\n")

for j in my_list:
    print("Each Value in my_list:", j)

print("\n")

# >>> my_dictionary
# {'course': 'python', 'mode': 'online'}

# >>> my_dictionary.keys()
# dict_keys(['course', 'mode'])
# >>>
for k in my_dictionary.keys():
    print("each key using keys():", k)
    print("value for that key using keys():", my_dictionary[k])

print("\n")

# >>> my_dictionary.values()
# dict_values(['python', 'online'])
# >>>
for v in my_dictionary.values():
    print("Each Value using values():", v)

print("\n")

# >>> my_dictionary.items()
# dict_items([('course', 'python'), ('mode', 'online')])
for i in my_dictionary.items():
    print("Each item:", i)
    print("Key Each item:", i[0])
    print("Value Each item:", i[1])

print("\n")

# >>> my_dictionary.items()
# dict_items([('course', 'python'), ('mode', 'online')])
for i, j in my_dictionary.items():
    print("Each Key:", i)
    print("Each Value:", j)


print("#"*40, end="\n\n")
###################################

# 2 Cases
# Case-1: 'break': We can end for-loop inbetween
# Case-2: 'continue': We can skip current iteration and send it to next iteration

print("# Case-1: 'break': We can end for-loop inbetween")
print("-"*20)
# --------------

my_list = ["C++", "Java-1", "C", "Java-2", "Perl"]

# Requirement: Verify are there any value starting with 'Java'
for each_course in my_list:
    if each_course.startswith("Java"):
        print("Course Java Found")
        break

print("#"*40, end="\n\n")
###################################

print("Without using continue")
print("-"*20)
# --------------

my_list = ["C++", "Java-1", "C", "Java-2", "Perl"]

for each_course in my_list:

    print("current course is:", each_course)

    if each_course.startswith("Java"):
        print("This is one of the java course")
        print("This java course duration is 10 days")
        print("This is one version of java", end="\n\n")
    else:
        print("Not executing block of code written for Java", end="\n\n")

print("#"*40, end="\n\n")
###################################

print("# Case-2: 'continue': We can skip current iteration and send it to next iteration")
print("-"*20)
# --------------

my_list = ["C++", "Java-1", "C", "Java-2", "Perl"]

for each_course in my_list:
    print("current course is:", each_course)

    if not each_course.startswith("Java"):
        print("This course is not required. So skipping current iteration\n")
        continue

    print("This is one of the java course")
    print("This java course duration is 10 days")
    print("This is one version of java", end="\n\n")


print("#"*40, end="\n\n")
###################################

print("for-else block: WITHOUT USING 'break'")
print("-"*20)
# --------------

my_list = ["C++", "Java-1", "C", "Java-2", "Perl"]


for each_course in my_list:
    print("Each Course:", each_course)
else:
    print("Reached for-else block")
    print("POINT-1: 'else' block will execute after completing the for-loop")
    print("""POINT-2: if for-loop ended using 'break', 
    it will not only coming out of 'for-block' it also comes out of 'else'""")

print("#"*40, end="\n\n")
###################################

print("for-else block USING 'break'")
print("-"*20)
# --------------

my_list = ["C++", "Java-1", "C", "Java-2", "Perl"]


for each_course in my_list:
    print("Each Course:", each_course)
    if each_course == "C":
        break
else:
    print("Reached for-else block")
    print("POINT-1: 'else' block will execute after completing the for-loop")
    print("""POINT-2: if for-loop ended using 'break', 
    it will not only coming out of 'for-block' it also comes out of 'else'""")

# When to use 'for-else'?
#
# Example: Suppose we are writing each record to file and assume
#   after successful insertion of all records, we need to save
#   else we dont want to save.
#
# Then use 'for-else'
# in 'for': write a logic for writing to file
# in 'else': write a logic for save
# 'break': Use break if some write in not successful

print("#"*40, end="\n\n")
###################################
