"""
Conditional Block 'if': Execute block of code ONLY if given condition is True
else skip entire block
"""

print("Using 'if' block")
print("-"*20)
# --------------

x = 10
if x == 10:
    print("Value of x is 10")
    print("Value of x is 10")
    print("Value of x is 10")

if x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")
    print("Value of x is gt 10")

if x < 10:
    print("Value of x is lt 10")
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
###################################

print("Using 'if-elif' block")
print("-"*20)
# --------------

x = 10
if x == 10:
    print("Value of x is 10")
    print("Value of x is 10")
    print("Value of x is 10")

elif x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")
    print("Value of x is gt 10")

elif x < 10:
    print("Value of x is lt 10")
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
###################################

print("Using 'if-elif-else' block")
print("-"*20)
# --------------

x = 10
if x == 10:
    print("Value of x is 10")
    print("Value of x is 10")
    print("Value of x is 10")

elif x > 10:
    print("Value of x is gt 10")
    print("Value of x is gt 10")
    print("Value of x is gt 10")

else:
    print("Value of x is lt 10")
    print("Value of x is lt 10")
    print("Value of x is lt 10")

print("#"*40, end="\n\n")
###################################

print("'if-block' with string, list, tuple, Any other collections")
print("-"*20)
# --------------

my_string = "Python"
my_list = [100, "python", "Java"]
my_dictionary = {"course": "python", "mode": "online"}

if my_string.startswith("Py") and ("tho" in my_string):
    print("All string conditions are True")

if "python" in my_list:
    print("Value 'python' found in list")


# >>> my_dictionary
# {'course': 'python', 'mode': 'online'}

# >>> my_dictionary.keys()
# dict_keys(['course', 'mode'])
# >>>
if "course" in my_dictionary.keys():
    print("Key found")

# >>> my_dictionary.values()
# dict_values(['python', 'online'])
# >>>
if "python" in my_dictionary.values():
    print("Value 'python' found")

# >>> my_dictionary.items()
# dict_items([('course', 'python'), ('mode', 'online')])
if ('mode', 'online') in my_dictionary.items():
    print("Item ('mode', 'online') Found")

print("#"*40, end="\n\n")
###################################
