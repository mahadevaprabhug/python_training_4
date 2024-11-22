"""
In this section,
Case-2: How to pass values to variable present inside the function

3 ways to pass values
1-way: We can pass only values OR values in the form of arg=value
2-way: We can restrict to pass only values
3-way: We can restrict to pass values in the form of arg=value
"""

print("1-way: We can pass only values OR values in the form of arg=value")
print("POSITIONAL or KEYWORD argument")
print("-"*20)
# --------------


def employee(name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


# Only Values we can specify
received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

# OR, we can specify argument name
received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value)

print("#"*40, end="\n\n")
###################################

print("2-way: We can restrict to pass only values")
print("ONLY POSITIONAL ARGUMENT")
print("-"*20)
# --------------

# / is just a syntax to tell is only POSITIONAL ARGUMENT
# / is not counted as argument
# / we are not passing any values to /


def employee(name, company, /):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


# Only Values we can specify
received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

# THIS WILL NOT WORK
# OR, we can specify argument name
# received_value = employee(name="emp-1", company="comp-1")
# print("received_value:", received_value)

print("#"*40, end="\n\n")
###################################

print("3-way: We can restrict to pass values in the form of arg=value")
print("ONLY KEYWORD ARGUMENT")
print("-"*20)
# --------------

# * is just a syntax to tell it is only KEYWORD ARGUMENT
# * is not counted as argument
# * we are not passing any values to *


def employee(*, name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


# THIS WILL NOT WORK
# Only Values we can specify
# received_value = employee("emp-1", "comp-1")
# print("received_value:", received_value)


# OR, we can specify argument name
received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value)

print("#"*40, end="\n\n", sep="\n")
###################################


