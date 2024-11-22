"""
while-loop: Execute loop based on the condition
"""

print("while-loop example")
print("-"*20)
# --------------

x = 0
while x < 10:
    print("Value of x is:", x)
    print("Value of x is:", x)
    print("Value of x is:", x, end="\n\n")
    x = x + 1

print("#"*40, end="\n\n")
###################################

# 2 Cases
# Case-1: 'break': We can end while-loop inbetween
# Case-2: 'continue': We can skip current iteration and send it to next iteration

print("# Case-1: 'break': We can end while-loop inbetween")
print("-"*20)
# --------------

my_list = ["C++", "Java-1", "C", "Java-2", "Perl"]

# Requirement: Verify are there any value starting with 'Java'
index_no = 0
while index_no < len(my_list):
    if my_list[index_no].startswith("Java"):
        print("Course Java Found")
        break
    index_no += 1


# for each_course in my_list:
#     if each_course.startswith("Java"):
#         print("Course Java Found")
#         break
#

print("#"*40, end="\n\n")
###################################

print("# Case-2: 'continue': We can skip current iteration and send it to next iteration")
print("-"*20)
# --------------

my_list = ["C++", "Java-1", "C", "Java-2", "Perl"]

index_no = 0
while index_no < len(my_list):

    print("current course is:", my_list[index_no])

    if not my_list[index_no].startswith("Java"):
        print("This course is not required. So skipping current iteration\n")
        index_no += 1
        continue

    print("This is one of the java course")
    print("This java course duration is 10 days")
    print("This is one version of java", end="\n\n")
    index_no += 1

print("#"*40, end="\n\n")
###################################

print("while-else block: WITHOUT USING 'break'")
print("-"*20)
# --------------

my_list = ["C++", "Java-1", "C", "Java-2", "Perl"]


index_no = 0
while index_no < len(my_list):
    print("Each Course:", my_list[index_no])
    index_no += 1
else:
    print("Reached while-else block")


# for each_course in my_list:
#     print("Each Course:", each_course)
# else:
#     print("Reached for-else block")

print("#"*40, end="\n\n")
###################################
