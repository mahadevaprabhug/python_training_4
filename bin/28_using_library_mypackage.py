"""
PACKAGES:
We can keep modules in folders & subfolders
these folders & subfolders are called PACKAGES
"""

print("1-way to import")
print("-"*20)
# --------------

import mypackage.db.mymodule

print("course name:", mypackage.db.mymodule.course)

add_result = mypackage.db.mymodule.add(100, 200)
print("add_result:", add_result)

e = mypackage.db.mymodule.Employee()
e.add_name("emp-1")
print("emp Name:", e.get_name())

print("#"*40, end="\n\n")
###################################

print("2-way to import")
print("-"*20)
# --------------

import mypackage.db.mymodule as mm

print("course name:", mm.course)

add_result = mm.add(100, 200)
print("add_result:", add_result)

e = mm.Employee()
e.add_name("emp-1")
print("emp Name:", e.get_name())

print("#"*40, end="\n\n")
###################################

print("3-way to import")
print("-"*20)
# --------------

# def f():
#     from mymodule import course, Employee, add
#     # course, Employee, add will come to current scope : local, so inside function only we can access

from mypackage.db.mymodule import course, Employee, add
# course, Employee, add will come to current scope : global

print("course name:", course)

add_result = add(100, 200)
print("add_result:", add_result)

e = Employee()
e.add_name("emp-1")
print("emp Name:", e.get_name())

print("#"*40, end="\n\n")
###################################

print("4-way to import")
print("-"*20)
# --------------

# def f():
#     from mymodule import course, Employee, add
#     # course, Employee, add will come to current scope : local, so inside function only we can access

from mypackage.db.mymodule import course as c, Employee as E, add as a
# course, Employee, add will come to current scope : global

print("course name:", c)

add_result = a(100, 200)
print("add_result:", add_result)

e = E()
e.add_name("emp-1")
print("emp Name:", e.get_name())

print("#"*40, end="\n\n")
###################################

