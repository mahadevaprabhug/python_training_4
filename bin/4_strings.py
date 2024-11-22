"""
IMMUTABLE
- String:
    -- We already have option to store collection of characters like name, email-id etc
    -- Automatically Index number will be assigned to each character
"""

print("Strings PART-1")
print("How to store the values?")
print("-"*20)
# --------------

a = 'PERSON'
b = 'PERSON\'S'
c = "PERSON'S"
d = """PERSON'S HEIGHT IS XYZ" (" represents inch)"""
e = '''PERSON'S HEIGHT IS XYZ" (" represents inch)'''

# In all the above cases, it will create object 'str' and store the values

print(a, b, c, d, e)
# default sep=" " ONE SPACE, means in output put ONE space between each values
print(a, b, c, d, e, sep="\n")

print("#"*40, end="\n\n")
###################################

print("Strings PART-2")
print("How to store the values?")
print("-"*20)
# --------------

x = 10
y = 20
z = x + y

my_string = f"Add of {x} and {y} is {z}"
# f-> format
# f-> replaces {variable name} with its value
print("my_string:", my_string)

print("#"*40, end="\n\n")
###################################

print("Strings PART-3")
print("How to store the values?")
print("-"*20)
# --------------

my_file_path_1 = "D:\newfolder\test.py" # \n\t will get replaced
print("my_file_path_1=", my_file_path_1, end="\n\n")

my_file_path_2 = r"D:\newfolder\test.py" # \n\t will NOT get replaced
# r -> RAW STRING
print("my_file_path_2=", my_file_path_2, end="\n\n")

my_file_path_3 = repr(my_file_path_1)
print("my_file_path_3:", my_file_path_3)

print("#"*40, end="\n\n")
###################################

print("Strings PART-4")
print("Indexes: We can access each character using index number")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 5_strings.xlsx

print("Accessing 2nd Character using +ve index number:", my_string[1])
print("Accessing 2nd Character using -ve index number:", my_string[-7], end="\n\n")

# print("Accessing 100th Character using +ve index number:", my_string[100]) # ERROR
print("#"*40, end="\n\n")
###################################

print("Strings PART-5")
print("Getting sub-string")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 5_strings.xlsx

print("Substring from index 1 to 6 using +ve index:", my_string[1:6])
print("Substring from index 1 to 6 using -ve index:", my_string[-7:-2], end="\n\n")

print("Substring from index 1 to END using +ve index:", my_string[1:])
print("Substring from index 1 to END using -ve index:", my_string[-7:], end="\n\n")

print("Substring from BEGINNING to 6 using +ve index:", my_string[:6])
print("Substring from BEGINNING to 6 using -ve index:", my_string[:-2], end="\n\n")

print("Same string:", my_string[:], end="\n\n")

print("#"*40, end="\n\n")
###################################

print("Strings PART-6")
print("Step Value: We can skip characters in between")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 5_strings.xlsx

print("Substring from index 1 to 6 using +ve index default step=1:", my_string[1:6])
print("Substring from index 1 to 6 using -ve index default step=1:", my_string[-7:-2], end="\n\n")
# step=1 which means, from 1 to 6, give me all the character:

print("Substring from index 1 to 6 using +ve index step=1:", my_string[1:6:1])
print("Substring from index 1 to 6 using -ve index step=1:", my_string[-7:-2:1], end="\n\n")
# step=1 which means, from 1 to 6, give me all the character:

print("Substring from index 1 to 6 using +ve index step=2:", my_string[1:6:2])
print("Substring from index 1 to 6 using -ve index step=2:", my_string[-7:-2:2], end="\n\n")

print("#"*40, end="\n\n")
###################################


print("Strings PART-7")
print("Reverse direction")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer 5_strings.xlsx

# my_string[6:1] # WRONG WRONG WRONG

# Procedure
# start index should be 6
# start index should be 1
# step value should be -ve

print("substring from index-6 to 1 using +ve index number:", my_string[6:1:-1])
print("substring from index-6 to 1 using -ve index number:", my_string[-2:-7:-1], end="\n\n")

print("substring from index-6 to 1 using +ve index number step by 2:", my_string[6:1:-2])
print("substring from index-6 to 1 using -ve index number step by 2:", my_string[-2:-7:-2], end="\n\n")

print("#"*40, end="\n\n")
###################################

print("Methods present inside 'str' class")
print("-"*20)
# --------------

print(dir(my_string))

# OR
# print(dir(str))

# Why different naming convention like __
# __ names are system defined names
# __ are mapped to either some functions like len() OR some operators like +, -
# Example-1
# + is mapped to __add__, If we use + then internally it will call __add__
# len() is mapped to __len__, If we use + then internally it will call __add__
# my_string[0] is mapped to __getitem__, If we use + then internally it will call __add__

print("#"*40, end="\n\n")
###################################

print("Startswith() method")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

result = my_string.startswith("WEL") # True/False
print("result:", result)

print("#"*40, end="\n\n")
###################################
