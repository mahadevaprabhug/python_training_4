"""
How to get/create objects
- Using class

In this section,
1. Class object
2. Instance objects
"""

print("Class object and Instance Objects")
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

print("DATA present inside each objects")
print("-"*20)
# --------------

print("Data present in class object 'Employee':", Employee)
print("Data present in instance object 'e1':", e1)
print("Data present in instance object 'e2':", e2)

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

# master class 'object'
# We have many methods in object class starting from creating objects
# All the classes including builtins/libraries/our-classes are by default
#   linked to object class and by default whatever there in object class
#   will come to all classes. This is called INHERITANCE
