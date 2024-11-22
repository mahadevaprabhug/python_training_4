"""
Here, we are keeping all
1. variables
2. functions
3. classes
which we are planning to use in more than one program.

This file is also called as PYTHON-MODULE or PYTHON-LIBRARY
"""

# variables
course = "python"


# functions
def add(a, b):
    return a + b


# classes
class Employee:
    def add_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
