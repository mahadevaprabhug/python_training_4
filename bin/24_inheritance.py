"""
Inheritance:
1. multilevel inheritance
2. multiple inheritance
"""

print("1. multilevel inheritance")
print("-"*20)
# --------------


# Assume this is existing class
class Salary:
    def add_salary(self, sal):
        self.salary = sal
    def get_salary(self):
        return self.salary


# Client requirement:
# 1. add methods to add/view tax
# 2. rewrite get_salary() methods to return (salary-tax)

# Salary: parent/super-class
# Employee: Child/sub-class
class Employee(Salary):
    # 1. add methods to add/view tax
    def add_tax(self, tax):
        self.tax = tax

    def get_tax(self):
        return self.tax

    # 2. rewrite get_salary() methods to return (salary-tax)
    # POLYMORPHISM: We can use same name as super class method names
    def get_salary(self):
        return self.salary - self.tax

e1 = Employee()
e1.add_salary(20000)
e1.add_tax(2000)

print("Salary:", e1.get_salary())
print("tax:", e1.get_tax())

print("#"*40, end="\n\n")
###################################

print("Making use of super class method as well")
print("-"*20)
# --------------

# Assume this is existing class
class Salary:
    def add_salary(self, sal):
        self.salary = sal
    def get_salary(self):
        return self.salary

class Employee(Salary):
    # 1. add methods to add/view tax
    def add_tax(self, tax):
        self.tax = tax

    def get_tax(self):
        return self.tax

    # 2. rewrite get_salary() methods to return (salary-tax)
    # POLYMORPHISM: We can use same name as super class method names
    def get_salary(self):
        # 1-way to access super class method
        x = super().get_salary()
        # OR
        x = Salary.get_salary(self)
        return self.salary - self.tax

e1 = Employee()
e1.add_salary(20000)
e1.add_tax(2000)

print("Salary:", e1.get_salary())
print("tax:", e1.get_tax())


print("#"*40, end="\n\n")
###################################


print("1. multilevel inheritance: Method Resoultion Order")
print("-"*20)
# --------------

print(Employee.mro())

print("#"*40, end="\n\n")
###################################

print("2. multiple inheritance: Method Resoultion Order")
print("-"*20)
# --------------

class A:
    pass

class B:
    pass

class C(A,B):
    pass

print(C.mro())

print("#"*40, end="\n\n")
###################################
