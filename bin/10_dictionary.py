"""
MUTABLE
- Dictionary:
    -- We already have option to store collection of values like list of names, list of email-ids etc
    -- We can store DUPLICATE values
    -- We can/need to provide our own index to each value. Called KEY/VALUE
"""

print("Dictionary PART-1")
print("Store values")
print("-"*20)
# --------------

my_dictionary_1 = {0:"python", 1:10, 2:"online"}

# FOR KEYS: We can use any IMMUTABLE VALUES like numbers, strings, tuples
my_dictionary_2 = {"course":"python", "duration":10, "mode":"online"}

# FOR VALUES: We can keep any type of values in dictionary
my_dictionary_3 = {
    "duration":10,
    "course":"python",
    "mode":["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

# In all above, object of 'dict' class will be created

print("my_dictionary_1:", my_dictionary_1)
print("my_dictionary_2:", my_dictionary_2)
print("my_dictionary_3:", my_dictionary_3)

print("#"*40, end="\n\n")
###################################

print("Dictionary PART-2")
print("We can access individual values")
print("-"*20)
# --------------

my_dictionary = {
    "duration":10,
    "course":"python",
    "mode":["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

print("Duration:", my_dictionary["duration"], end="\n\n") # 10

print("course:", my_dictionary["course"]) # "python"
print("2nd character in course:", my_dictionary["course"][1], end="\n\n") # "y"

print("Mode:", my_dictionary["mode"]) # ["online", "offline"]
print("2nd Mode:", my_dictionary["mode"][1]) # "offline"
print("4th char in 2nd Mode:", my_dictionary["mode"][1][3], end="\n\n") # "l"

print("Trainer:", my_dictionary["trainer"]) # {"fname": "abc", "lname": "xyz"}
print("Lname of the Trainer:", my_dictionary["trainer"]["lname"]) # "xyz"
print("2nd char in Lname of the Trainer:", my_dictionary["trainer"]["lname"][1], end="\n\n") # "y"

print("#"*40, end="\n\n")
###################################

print("Dictionary PART-3")
print("Methods present in dictionary class")
print("-"*20)
# --------------

print(dir(my_dictionary))
# OR
# print(dir(dict))

print("#"*40, end="\n\n")
###################################

print("Dictionary PART-4")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# --------------

my_dictionary = {"course":"python", "duration":10, "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# ADD/UPDATE: If key present then update else ADD
my_dictionary["location"] = "India"
new_value = {"trainer": "abc", "duration":1000}
my_dictionary.update(new_value)
print("my_dictionary after adding / updating:", my_dictionary, end="\n\n")

# REMOVE
my_dictionary.pop("mode")
print("my_dictionary after removing 'mode':", my_dictionary, end="\n\n")

my_dictionary.popitem()
print("my_dictionary after removing last element:", my_dictionary, end="\n\n")

print("#"*40, end="\n\n")
###################################
