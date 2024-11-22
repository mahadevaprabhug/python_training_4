"""
Exceptions Handling
"""

# print("Without handling exceptions")
# print("-"*20)
# # --------------
#
# a = 10
# b = 0
# result = a/b
# print("result:", result)
#
# print("#"*40, end="\n\n")
# ###################################

print("Handling exceptions")
print("-"*20)
# --------------

try:
    pass # If any error comes in this block then instead of terminating send it to except block
except:
    pass # Here we will write a logic to take care of error happened in try


try:
    a = 10
    b = 0
    result = a/b
    print("result:", result)
except:
    print("Reached except block")

print("#"*40, end="\n\n")
###################################


print("Handling exceptions")
print("-"*20)
# --------------

try:
    pass # If any error comes in this block then instead of terminating send it to except block
except:
    pass # Here we will write a logic to take care of error happened in try


try:
    a = 10
    b = 0
    result = a/b
    print("result:", result)
except:
    print("Reached except block")

print("#"*40, end="\n\n")
###################################

# About 'Exception' classes
# --------------
# - If we want to handle exception then we need to handle exception classes
#
# - If we dont have exception class for perticular error then what will happen?
#   - Answer: It will termintate all-of-sudden/abruptly
#
# - In above try-except, we didnt use any class so how it is getting handled
#   - default 'except' internally it will use exception class 'Exception' which is
#       already there in builtins
#
# - Few exception classes are present in builtins
#
# - For remaining errors, we need to write exception classes
#
# - Master class is 'Exception', which will be able to accept/receive all type
#   error
###################################

print("Handling with class names")
print("-"*20)
# --------------


try:
    a = 10
    b = 0
    result = a/b
    print("result:", result)
except ZeroDivisionError: # 1-way we can only specify class name
    print("Reached ZDE block")
except NameError as ne: # 2-way, we can also capture error class object
    print("Reached NE block. Value of ne is:", ne)

print("#"*40, end="\n\n")
###################################

print("try-except-without 'else'")
print("-"*20)
# --------------

try:
    try:
        print("Reached try block")
        my_file_handle = open(r"D:\sdsdsd\ererer.txt", "w")
    except (FileNotFoundError, IndexError):
        print("Reached else block")
        # exit()
    try:
        print("'else' block is continutation of 'try'")
        my_file_handle.write("Hello")
        my_file_handle.close()
    except Exception as e:
        print("Gor error while writing and message is:", e)

except Exception as e:
    print("Got some error:", e)

print("#"*40, end="\n\n")
###################################


print("try-except-else")
print("-"*20)
# --------------

try:
    print("Reached try block")
    my_file_handle = open(r"D:\sdsdsd\ererer.txt", "w")
    print("eeeeeeeeeeeeeeeeReached else block")
    print("'else' block is continutation of 'try'")
    my_file_handle.write("Hello")
    my_file_handle.close()

except FileNotFoundError:
    print("Reached except block")
else:
    try:
        print("Reached else block")
        print("'else' block is continutation of 'try'")
        my_file_handle.write("Hello")
        my_file_handle.close()
    except Exception as e:
        print("Gor error while writing and message is:", e)

# In simple, 'else' block is continutation of try block
# if 'try' success 'except' will get skipped and 'else' will execute
# if 'try' failed 'else' will get skipped and 'except' will execute

print("#"*40, end="\n\n")
###################################


print("try-except-else-finally")
print("-"*20)
# --------------

try:
    print("Reached try block")
    my_file_handle = open(r"D:\sdsdsd\ererer.txt", "w")
except FileNotFoundError:
    print("Reached except block")
else:
    print("Reached else block")
    my_file_handle.write("Hello")
finally:
    print("Reached finally block")
    try:
        my_file_handle.close()
        print("file closed")
    except Exception as e:
        print("Not able to close file because:", e)

# finally block will always execute even if 'try'/'except'/'else' fails

print("#"*40, end="\n\n")
###################################

print("User Defined Exception Class Example-1")
print("-"*20)
# --------------

# mandatory step: Our class should be sub-class of 'Exception' class
# OR if some classes are already subclass of 'Exception' then we can
#   use those classes to create our class.
#   example: builtin exception classes are already subclass of 'Exception'


class MyError(Exception):
    pass
# It is valid exception class. So we can handle using this class


try:
    x = 10
    if x == 10:
        raise MyError
    if x > 10:
        raise MyError
    if x < 10:
        raise MyError
except MyError:
    print("Reached MyError except block")

print("#"*40, end="\n\n")
###################################

print("User Defined Exception Class Example-2")
print("-"*20)
# --------------

# Requirement: Send some message while throwing exception
# example: raise MyError("Here value 10")


class MyError(Exception):
    def __init__(self, msg):
        self.error_message = msg

try:
    x = 10
    if x == 10:
        raise MyError("Here value of x is 10 so raising MyError")
    if x > 10:
        raise MyError("Here value of x is gt 10 so raising MyError")
    if x < 10:
        raise MyError("Here value of x is lt 10 so raising MyError")
except MyError as me:
    print("Reached MyError except block and Error details:", me.error_message)

print("#"*40, end="\n\n")
###################################
