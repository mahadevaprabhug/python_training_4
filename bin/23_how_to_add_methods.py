"""
How to add methods PART-2
In this section,
1. Rewriting(Overriding) object class methods
    __new__: Constructor
    __init__: Initializer
    When we create objects, both will execute, 1st __new__ then __init__
    In this example, we are planning to override __init__
2. static method
"""

print("Creating Objects")
print("-"*20)
# --------------


class Employee:

    # 1 - New thing
    def __init__(self, ename):
        self.emp_name = ename

    # 2nd new thing
    company_name = "XYZ Company"
    # This will get created inside class object

    @classmethod
    def get_company_name(cls): # CLASS OBJECT will be passed in 1st argument
        return cls.company_name

    def get_employee_name(self): # INSTANCE object will be passed in 1st argument
        return self.emp_name

    # 3rd New thing
    @staticmethod
    def get_avg_salary(sal1,sal2): # No object(INSTANCE/CLASS) will be passed in 1st argument
        return (sal1+sal2)/2


e1 = Employee("Emp-1") # __init__
e2 = Employee("Emp-2")

# Total 3 objects
# CLASS OBJECT: 'Employee' in the name of class, ONE object is getting created
# INSTANCE OBJECT: 'e1' & 'e2' which we created

print("#"*40, end="\n\n")
###################################

print("DATA present inside each objects")
print("-"*20)
# --------------

print("Data present in class object 'Employee':", Employee.get_company_name())
print("Data present in instance object 'e1':", e1.get_employee_name())
print("Data present in instance object 'e2':", e2.get_employee_name())
print("Avg Salary:", Employee.get_avg_salary(1000, 2000))

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
