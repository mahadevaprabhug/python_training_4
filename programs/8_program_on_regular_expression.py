"""
Get data web_server.log

then

extract and ONLY print IP & PICS

In free time, extract DATE & URL
"""

print("Get data from web_server.log")
print("-"*20)
# --------------

my_log_file_handle = open(r"../log/web_server.log", "rb")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
###################################

print("Check whether it is IP address line or not?")
print("-"*20)
# --------------

import re

for each_value in log_file_content:
    # Ex:-1
    # match_result = re.match(b'\d\d\d\.\d{3}\.(\d|\d\d|\d\d\d)\.', each_value)
    # Ex:-2
    # match_result = re.match(b'\d\d\d\.\d{3}\.\d{1,3}\.[0-9][0-9][0-9]', each_value)
    # Ex:-3
    match_result = re.match(br'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*', each_value)
    # b -> bytes
    # r -> raw string
    print("each value:", each_value)
    print("match_result:", match_result, end="\n\n")
    print("-"*10)

# COMMENT
r"""
Regular Expression

# Identifiers
# -----------------
# \d -> represents any one digit between 0 to 9
# \D -> represents any one non-digit. any character except 0 to 9
# .  -> represents any one any character
# \. -> represents strictly DOT
# -----------------

# Quantifiers
# -----------------
# \d{3} -> it will produce 3 \d like \d\d\d
# \d{1,3} -> it will produce (\d|\d\d|\d\d\d)
# -----------------

# Modifiers
# -----------------
# * -> 0 or more times
# + -> 1 or more times
# ? -> 0 or 1 time
# -----------------

"""

print("#"*40, end="\n\n")
###################################

# Some More examples
# --------------
# Example-1
# ----
# from the beginning IP address
# match_result = re.match(br'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*', each_value)
#
# Anywhere in that data
# match_result = re.match(br'.*\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*', each_value)
#
# Example-2
# ----
#
# If we know exact course name like
# course_name = "Python Programming"
# match_result = re.match("Python Programming", course_name)
#
# If we don't know exact course name but we know the pattern
# like "Java Programming" or "Python Programming" etc
# match_result = re.match("[a-zA-Z]+ Programming", course_name)
#
# match_result = re.match("[a-zA-Z]+ Programming", course_name)
# "xyzyzsdbm Java Programming" # THIS WILL NOT MATCH
# "Python Programming"  # THIS WILL MATCH
#
# match_result = re.match(".*[a-zA-Z]+ Programming", course_name)
# "xyzyzsdbm jsdjsalkd asldk ;lsak;d Java Programming" # THIS WILL MATCH
# "Python Programming"  # THIS WILL MATCH
# "XYZ PERL sandnsan"  # THIS WILL NOT MATCH
#
#
# Exmaple-3
#
# match_result = re.match("r[ea]d", input_string)
# read # NOT MATCH
# red # MATCH FOUND
# rad  # MATCH FOUND
# rd # NOT MATCH
# reeeeeeaaaaaaaad  # NOT MATCH
# raaaaaaeeeeeed # NOT MATCH
#
# Exmaple-4
#
# match_result = re.match("r[ea]*d", input_string)
# read # MATCH FOUND
# red # MATCH FOUND
# rad  # MATCH FOUND
# rd # MATCH FOUND
# reeeeeeaaaaaaaad  # MATCH FOUND
# raaaaaaeeeeeed # MATCH FOUND
#
# Exmaple-5
#
# match_result = re.match("r[ea]+d", input_string)
# read # MATCH FOUND
# red # MATCH FOUND
# rad  # MATCH FOUND
# rd # MATCH NOTTTTTTT FOUND
# reeeeeeaaaaaaaad  # MATCH FOUND
# raaaaaaeeeeeed # MATCH FOUND
#
# Exmaple-6
#
# match_result = re.match("r[ea]{0,1}d", input_string)
# OR
# match_result = re.match("r[ea]?d", input_string)
# read # NO MATCH FOUND
# red # MATCH FOUND
# rad  # MATCH FOUND
# rd # MATCH FOUND
# reeeeeeaaaaaaaad  # NO MATCH FOUND
# raaaaaaeeeeeed # NO MATCH FOUND
#
###################################

print("Extract IP")
print("-"*20)
# --------------

import re

for each_value in log_file_content:
    match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*', each_value)
    if match_result is not None:
        ip = match_result.group(1)
        ip = ip.decode()
        print(ip)


# COMMENT
r"""
put () to IP address pattern
- this is called grouping
- each group has index starting from 1
"""

print("#"*40, end="\n\n")
###################################

print("Extract IP, PICS")
print("-"*20)
# --------------

import re

for each_value in log_file_content:

    # Very Less Information Provided Here
    # match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\w+\.[a-z]{3}).*', each_value)

    # More Information: BUT line which not having /pics/ is not matched
    # match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(GET|POST|PUT|PATCH|DELETE)\s/pics/(\w+\.(gif|jpg))\sHTTP.*', each_value)

    # Making image name optional so that lines which is not having image name also
    # considered
    match_result = re.match(br'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(GET|POST|PUT|PATCH|DELETE)\s+/(pics/(\w+\.(gif|jpg)))?.*\s+HTTP.*', each_value)
    if match_result is not None:
        ip = match_result.group(1)
        ip = ip.decode()
        img = match_result.group(4)
        if img is not None:
            img = img.decode()
        else:
            img = "No Image"
        print(ip, img)


# COMMENT
r"""
\w -> [a-zA-Z_0-9]
\W -> [^a-zA-Z_0-9] # ^ excluding

\s -> One Space
\S -> Any character except SPACE
"""

print("#"*40, end="\n\n")
###################################
