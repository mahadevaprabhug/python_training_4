"""
How to add methods

In this section,
1. class methods
2. instance methods
"""

print("Creating Objects")
print("-"*20)
# --------------


class Employee:

    @classmethod # This will take care of passing class-object to cls even if we call this method with e1 & e2
    def store_company_name(cls, cname):
        cls.company_name = cname

    @classmethod
    def get_company_name(cls):
        return cls.company_name

    def store_employee_name(self, ename):
        self.emp_name = ename

    def get_employee_name(self):
        return self.emp_name


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

Employee.store_company_name("XYZ Company")
# Internally object 'Employee' will be passed to 'cls'
# We, no need to pass anything to 'cls'
# So, 'cls' is to keep object

e1.store_employee_name("emp-1")
# Internally object 'e1' will be passed to 'self'

e2.store_employee_name("emp-2")
# Internally object 'e2' will be passed to 'self'

print("#"*40, end="\n\n")
###################################

print("DATA present inside each objects")
print("-"*20)
# --------------

print("Data present in class object 'Employee':", Employee.get_company_name())
print("Data present in instance object 'e1':", e1.get_employee_name())
print("Data present in instance object 'e2':", e2.get_employee_name())

print("#"*40, end="\n\n")
###################################

