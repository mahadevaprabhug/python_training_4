"""
Decorator: Function which is having common function functionalitis
which we need to use it in many other functions
"""

print("WITHOUT using decorators")
print("-"*20)
# --------------


def add(a, b):
    print("Result is:")
    print(a+b)
    print("End of the result")


def sub(a, b):
    print("Result is:")
    print(a-b)
    print("End of the result")


add(10, 20)
sub(10, 20)

print("#"*40, end="\n\n")
###################################

print("Using decorators: PARTIAL IMPLEMENTATION")
print("-"*20)
# --------------


# Function as per decorator design pattern
def my_decorator(my_function): # my_function=add
    def decorated_function(x, y): # x=10, y=20
        print("Result is:")
        function_result = my_function(x, y) # add(10,20)
        print(function_result)
        print("End of the result")
    return decorated_function



def add(a, b):
    return a+b

decorated_function_ref = my_decorator(add)
# decorated_function_ref WILL BE HAVING decorated_function REFERENCE
decorated_function_ref(10, 20)
# ---------------------

def sub(a, b):
    return a-b

decorated_function_ref = my_decorator(sub)
# decorated_function_ref WILL BE HAVING decorated_function REFERENCE
decorated_function_ref(10, 20)
# ---------------------

def sub2(a, b):
    return a-b-b

decorated_function_ref = my_decorator(sub2)
# decorated_function_ref WILL BE HAVING decorated_function REFERENCE
decorated_function_ref(10, 20)
# ---------------------

def sub3(a, b):
    return a-b-b-a

decorated_function_ref = my_decorator(sub3)
# decorated_function_ref WILL BE HAVING decorated_function REFERENCE
decorated_function_ref(10, 20)
# ---------------------

print("THIS IS PARTIAL IMPLEMENTATION")

print("#"*40, end="\n\n")
###################################

print("Using decorators: FINAL IMPLEMENTATION")
print("-"*20)
# --------------


# Function as per decorator design pattern
def my_decorator(my_function): # my_function=add
    def decorated_function(x, y): # x=10, y=20
        print("Result is:")
        function_result = my_function(x, y) # add(10,20)
        print(function_result)
        print("End of the result")
    return decorated_function


@my_decorator
def add(a, b):
    return a+b

add(10, 20)

# @my_decorator will take care of executing below 2 steps
# decorated_function_ref = my_decorator(add)
# decorated_function_ref(10, 20)
# ---------------------


@my_decorator
def sub(a, b):
    return a-b

sub(10, 20)

# @my_decorator will take care of executing below 2 steps
# decorated_function_ref = my_decorator(sub)
# decorated_function_ref(10, 20)
# ---------------------

@my_decorator
def sub2(a, b):
    return a-b-b

sub2(10, 20)

# @my_decorator will take care of executing below 2 steps
# decorated_function_ref = my_decorator(sub2)
# decorated_function_ref(10, 20)
# ---------------------


def sub3(a, b):
    return a-b-b-a

sub3(10, 20)

# @my_decorator will take care of executing below 2 steps
# decorated_function_ref = my_decorator(sub3)
# decorated_function_ref(10, 20)
# ---------------------

print("#"*40, end="\n\n")
###################################
