"""
How to put data inside object

In this section,
1. Class variables
2. Instance variables
"""

print("Creating Objects")
print("-"*20)
# --------------


class Employee:
    pass
# use dummy keyword 'pass' to keep any block empty like if-block, etc
# Even though it is empty class, it is valid class. Means we can create objects


e1 = Employee()
e2 = Employee()

# Total 3 objects
# CLASS OBJECT: 'Employee' in the name of class, ONE object is getting created
# INSTANCE OBJECT: 'e1' & 'e2' which we created

print("#"*40, end="\n\n")
###################################

print("Store the data")
print("-"*20)
# --------------

Employee.company_name = "XYZ Company"
# company_name is new variable, It will create inside object and store the value

e1.name = "emp-1"
# name is new variable, It will create inside object and store the value

e2.name = "emp-1"
# name is new variable, It will create inside object and store the value

print("#"*40, end="\n\n")
###################################

print("DATA present inside each objects")
print("-"*20)
# --------------

print("Data present in class object 'Employee':", Employee.company_name)
print("Data present in instance object 'e1':", e1.name)
print("Data present in instance object 'e2':", e2.name)

print("#"*40, end="\n\n")
###################################

print("METHODS/VARIABLES present inside each objects")
print("-"*20)
# --------------

print("METHODS/VARIABLES present inside class object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS/VARIABLES present inside instance object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS/VARIABLES present inside instance object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
###################################

# About 'CLASS OBJECT' 'Employee'
# --------------
# - It is common space for all instance objects
# - whatever we store inside class object, by default it will available in
#   all instance objects
###################################