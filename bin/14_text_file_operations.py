"""
Text file Operations:
Text files with any extension like .txt, .log
"""

"""
We need to follow 3 steps
1. Connect to file
2. Read/Write
3. Disconnect
"""

"""
We have functions for all 3 steps
1. Connect to file
    - open() function
2. Read/Write
    - For Writing: 1) write 2) writelines 3) print-function
    - For Reading: 1) read 2) readlines 3) readline
3. Disconnect
    - close() function
"""

print("All write operations")
print("-"*20)
# --------------

# 1. Connect to file
# --------------
my_file_handle = open("my_out_file.txt", "w")
# mode 'w': Write only, It will create new file, IMPORTANT-It will erase existing content
# mode 'r': Read only, It will not create new file if file not present
# mode 'a': Append only, It will create new file ONLY if file not present

# mode 'w+': RW, It will create new file, IMPORTANT-It will erase existing content
# mode 'r+': RW, It will not create new file if file not present
# mode 'a+': RW, It will create new file ONLY if file not present

# mode 'wb': Write only, It will create new file, IMPORTANT-It will erase existing content
# mode 'rb': Read only, It will not create new file if file not present
# mode 'ab': Append only, It will create new file ONLY if file not present


# 2. Write
# --------------

# Our Data
x = 10
y = "python"

# 1) write # It will take only one string
my_file_handle.write(str(x)+"\n")
my_file_handle.write(y+"\n")

# 2) writelines: Collection of strings like list/tuple etc
L = [str(x)+"\n", y+"\n"]
my_file_handle.writelines(L)

# 3) print-function
print(x, y, 20, "python", sep="\n", file=my_file_handle)

# 3. Disconnect
# --------------
my_file_handle.close()

print("""
Created my_out_file.txt,
Please check
""")

print("#"*40, end="\n\n")
###################################

print("Reading from file using 1) read")
print("-"*20)
# --------------

# 1. Connect to file
# --------------
my_file_handle = open("my_out_file.txt", "r")

# 2. Read
# --------------
file_content = my_file_handle.read()
# It read entire file content and return in ONE string
print("file_content:", file_content, end="\n\n")
print("file_content in raw format:", repr(file_content), end="\n\n")

# 3. Disconnect
# --------------
my_file_handle.close()

print("#"*40, end="\n\n")
###################################


print("Reading from file using 2) readlines")
print("-"*20)
# --------------

# 1. Connect to file
# --------------
my_file_handle = open("my_out_file.txt", "r")

# 2. Read
# --------------
file_content = my_file_handle.readlines()
# It read entire file content in list
print("file_content:", file_content, end="\n\n")


# 3. Disconnect
# --------------
my_file_handle.close()

print("#"*40, end="\n\n")
###################################


print("Reading from file using 3) readline")
print("-"*20)
# --------------

# 1. Connect to file
# --------------
my_file_handle = open("my_out_file.txt", "r")

# 2. Read
# --------------
file_content = my_file_handle.readline()
print("1st Line:", file_content, end="\n\n")

file_content = my_file_handle.readline()
print("2nd Line:", file_content, end="\n\n")

file_content = my_file_handle.readline()
print("3rd Line:", file_content, end="\n\n")

# 3. Disconnect
# --------------
my_file_handle.close()

print("#"*40, end="\n\n")
###################################

print("Reading from file using 3) readline using for-loop")
print("-"*20)
# --------------

# 1. Connect to file
# --------------
my_file_handle = open("my_out_file.txt", "r")

# 2. Read
# --------------
for each_line in my_file_handle:
    print("each_line:", each_line)

# 3. Disconnect
# --------------
my_file_handle.close()

print("#"*40, end="\n\n")
###################################
