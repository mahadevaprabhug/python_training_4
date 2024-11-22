"""
multithreading: Split One-Process into multiple pieces, each piece is called thread
and run parallelly

BUT, in python multithreading is NOT PARALLEL. Only one thread will execute at a time

Then waht is the use of multithreading?
- If some thread is waiting for some resources
    then during that waiting time, it will execute another thread.
    SO
    we are making use waiting time
"""

print("WITHOUT using multithreading")
print("-"*20)
# --------------

import time
start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)

def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L = [10, 20, 30, 40, 50]

my_square_function(L)
my_cube_function(L)

end_time = time.time()
print("Total Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
###################################

print("Using multithreading")
print("-"*20)
# --------------

import time
start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)

def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L = [10, 20, 30, 40, 50]

from threading import Thread
my_thread_1 = Thread(target=my_square_function, args=(L,))
my_thread_2 = Thread(target=my_cube_function, args=(L,))

my_thread_1.start()
# It will just start thread execution and proceed to next line
# means, it will not wait for thread executing to complete
my_thread_2.start()

# To get end time properly, let us make both threads wait here
# to complete its execution
my_thread_1.join()
my_thread_2.join()

end_time = time.time()
print("Total Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
###################################

print("WITH DELAY: WITHOUT using multithreading")
print("-"*20)
# --------------

import time
start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)

def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40, 50]

my_square_function(L)
my_cube_function(L)

end_time = time.time()
print("Total Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
###################################

print("WITH DELAY: Using multithreading")
print("-"*20)
# --------------

import time
start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)

def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40, 50]

from threading import Thread
my_thread_1 = Thread(target=my_square_function, args=(L,))
my_thread_2 = Thread(target=my_cube_function, args=(L,))

my_thread_1.start()
# It will just start thread execution and proceed to next line
# means, it will not wait for thread executing to complete
my_thread_2.start()

# To get end time properly, let us make both threads wait here
# to complete its execution
my_thread_1.join()
my_thread_2.join()

end_time = time.time()
print("Total Time Taken:", end_time-start_time, " Seconds")

print("#"*40, end="\n\n")
###################################
