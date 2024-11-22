"""
Generators: We can create object whenever we need
"""

print("WITHOUT using generators")
print("-"*20)
# --------------


def my_square_function(my_list):
    squared_values_list = []
    for i in my_list:
        squared_values_list.append(i*i)
    return squared_values_list


L = [10, 20, 30, 40]
squared_L = my_square_function(L)

for i in squared_L:
    print("Squared Value:", i)

print("#"*40, end="\n\n")
###################################

print("Using generators")
print("-"*20)
# --------------


def my_square_function(my_list):
    for i in my_list:
        yield i * i


L = [10, 20, 30, 40]
generator_object = my_square_function(L)

for i in generator_object:
    print("Squared Value:", i)

print("#"*40, end="\n\n")
###################################
