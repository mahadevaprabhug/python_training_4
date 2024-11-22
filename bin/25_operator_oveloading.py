"""
Operator Overloading:

For each operator there is special name given
Example: + = __add__

And also
for some function there is special name given
Example: builtin len() = __len__
"""


print("Supported + operator")
print("-"*20)
# --------------


class Employee:
    def __init__(self, name):
        self.name = name

    def __add__(self, other): # self=e1, other=e2
        concat_result = self.name + other.name
        return concat_result


e1 = Employee("emp-1")
e2 = Employee("emp-2")


# Requirement: If we add 2 employee class objects
#   then it should concatinate both the names and return

add_result = e1 + e2 # e1.__add__(e2)
print("add_result:", add_result)

print("#"*40, end="\n\n")
###################################


print("Supported len()")
print("-"*20)
# --------------


class Employee:
    def __init__(self, name):
        self.name = name

    def __add__(self, other): # self=e1, other=e2
        concat_result = self.name + other.name
        return concat_result

    def __len__(self): # self=e1, e2
        return len(self.name)


e1 = Employee("emp-1")
e2 = Employee("emp-2")


# Requirement: If we add 2 employee class objects
#   then it should concatinate both the names and return

add_result = e1 + e2 # e1.__add__(e2)
print("add_result:", add_result)
print("Length of e1:", len(e1))


print("#"*40, end="\n\n")
###################################

print("Supported Iteration")
print("-"*20)
# --------------


class Employee:
    def __init__(self, name):
        self.name = name

    def __add__(self, other): # self=e1, other=e2
        concat_result = self.name + other.name
        return concat_result

    def __len__(self): # self=e1, e2
        return len(self.name)

    # 2 methods we need to implement for iteration
    # below method will be called 1st time & 1 time only
    def __iter__(self):
        self.index_no = 0
        return self

    # Every iteration, this method will be called
    def __next__(self):
        current_index = self.index_no
        if current_index < len(self.name):
            self.index_no += 1
            return self.name[current_index]
        else:
            raise StopIteration

e1 = Employee("emp-1")
e2 = Employee("emp-2")


# Requirement: If we add 2 employee class objects
#   then it should concatinate both the names and return

add_result = e1 + e2 # e1.__add__(e2)
print("add_result:", add_result)
print("Length of e1:", len(e1))

# Support for iterating each char in name
for i in e1:
    print("Value of i:", i)

for j in e2:
    print("Value of j:", j)

print("#"*40, end="\n\n")
###################################
