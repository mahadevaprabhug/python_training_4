"""
Get data from web_server.log

then

Extract
IP
DATE
PICS
URL

then

write extracted data to log_report.txt

Expected output in log_report.txt
-----------------
    IP                  DATE            PICS                URL
123.123.123.123     26/Apr/2000     wpaper.gif       http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     No Image         http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF
123.123.123.123     26/Apr/2000     5star2000.gif    http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     5star.gif        http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     a2hlogo.gif      http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     No Image         http://www.jafsoft.com/asctortf/
-----------------
"""

print("Get data from web_server.log")
print("-"*20)
# --------------

# 1. Connect to file
# --------------
# Absolute path
# my_log_file_handle = open(r"C:\python_training\log\web_server.log", "r")
# OR
# Relative path
my_log_file_handle = open(r"../log/web_server.log", "rb")

# 2. Read
# --------------
log_file_content = my_log_file_handle.readlines()

# 3. Disconnect
# --------------
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
###################################


print("type of log_file_content")
print("-"*20)
# --------------

print(type(log_file_content))

print("#"*40, end="\n\n")
###################################

print("type of values present in log_file_content list")
print("-"*20)
# --------------

print(type(log_file_content[0]))
# Check 1st value to understand what type of data we have
# inside list log_file_content

print("#"*40, end="\n\n")
###################################


print("Extract Info")
print("-"*20)
# --------------

for each_line in log_file_content:
    if each_line.startswith(b"123"):
        # OPTION-1
        # each_line = each_line.decode() # Convert string
        # OR
        # OPTION-2
        sp = each_line.split()
        # print(sp)
        ip = sp[0] # bytes
        ip = ip.decode() # String

        raw_img = sp[6]  # Ex: b'/pics/wpaper.gif'

        if raw_img.endswith(b".jpg") or raw_img.endswith(b".gif"):
            img = raw_img.removeprefix(b"/pics/")
            img = img.decode()
        else:
            img = "No Image"

        print(ip, img, sep="\t\t")

print("#"*40, end="\n\n")
###################################

# find simleys in each line
#---------------
# list_of_smileys = [b'', b'', b'']
#
# for each_line in log_file_content:
#     for i in list_of_smileys:
#         if each_line.startswith(i) or (i in each_line) or each_line.endswith(i):
###################################


print("Extract Info and write to file")
print("-"*20)
# --------------

my_out_file_handle = open("log_report.txt", "w")

# Write heading
# my_out_file_handle.write("IP\tPICS\n")
# OR
# my_out_file_handle.writelines(["IP\t", "PICS\n"])
# OR
print("IP", "PICS", sep="\t", file=my_out_file_handle)

for each_line in log_file_content:
    if each_line.startswith(b"123"):
        # OPTION-1
        # each_line = each_line.decode() # Convert string
        # OR
        # OPTION-2
        sp = each_line.split()
        # print(sp)
        ip = sp[0] # bytes
        ip = ip.decode() # String

        raw_img = sp[6]  # Ex: b'/pics/wpaper.gif'

        if raw_img.endswith(b".jpg") or raw_img.endswith(b".gif"):
            img = raw_img.removeprefix(b"/pics/")
            img = img.decode()
        else:
            img = "No Image"

        print(ip, img, sep="\t", file=my_out_file_handle)

my_out_file_handle.close()

print("""
Created log_report.txt,
Please check
""")

print("#"*40, end="\n\n")
###################################
