"""
Functions with variable arguments
1. Variable positional arguments
2. Variable keyword arguments
"""

print("1. Variable positional arguments")
print("-"*20)
# --------------


def add(*a):
    print("Values Received:", a)



add()
add(10, 20)
add(10, 20, 30, 40)
add(10, 20, 30, 40)

print("#"*40, end="\n\n")
###################################

print("2. Variable keyword arguments")
print("-"*20)
# --------------


def get_employee_profile(**profile_data):
    print("profile_data:", profile_data)


get_employee_profile()
get_employee_profile(name="emp-1")
get_employee_profile(name="emp-1", company="comp-1", phone="111111")

print("#"*40, end="\n\n")
###################################

# We can combine all type of arguments in one function
# following below order
###################################
# IN FUNCTION DEFINITION
#
# 1st put all positional arguments IF ANY
#
# then
#
# put variable positional argument IF ANY
#
# then
#
# put all keyword argument IF ANY
#
# then
#
# put variable keyword argument IF ANY
#
###################################


###################################
# Examples: Arguments Combinations
###################################
# 1.
# a & b are POSITIONAL or KEYWORD
# def add(a,b)
#
# 2.
# a & b are STRICTLY POSITIONAL
# def add(a,b,/)
#
# 3.
# a & b are Strictly KEYWORD
# def add(*, a,b)
#
# 4.
# a & b are STRICTLY POSITIONAL
# c & d are POSITIONAL or KEYWORD
# def add(a, b, /, c, d)
#
# 5.
# a & b are STRICTLY POSITIONAL
# c & d are STRICTLY KEYWORD
# def add(a, b, *, c, d)
#
# 6.
# a is variable positional arguments
# def add(*a)
#
# 7.
# a is variable keyword arguments
# def add(**a)
#
# 8.
# a is variable positional arguments
# b is variable keyword arguments
# def add(*a, **b)
#
# 9.
# a & b are POSITIONAL
# c is variable POSITIONAL
# def add(a, b, *c)
#
# 10.
# d & e are keyword arguments
# c is variable POSITIONAL
# def add(*c, d, e)
#
# 11
# All in one
# def add(a, b, *c, d, e, **f)
###################################


###################################
# Variable Scopes
###################################
# 1. Local Scope
#   - We can access inside function only
#
# 2. Enclosed Scope
#   - We can access inside function
#   - We can access inside nested function
#
# 3. Global Scope
#   - We can access anywhere in the program, it can be inside
#       inside any block like if, for, function etc
#       or outside any block
#
# 4. Built-in
#   - When we access any variable it will check in all the
#       scopes and if not found then it will check in builtins
#       then throw error if not found
###################################

