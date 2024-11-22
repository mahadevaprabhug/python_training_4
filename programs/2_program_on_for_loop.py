"""
From the given string below,

Extract
IP
DATE
PICS
URL

Expected Output:
-----------------
123.123.123.123     26/Apr/2000     wpaper.gif       http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     No Image         http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF
123.123.123.123     26/Apr/2000     5star2000.gif    http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     5star.gif        http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     a2hlogo.gif      http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     No Image         http://www.jafsoft.com/asctortf/
-----------------

"""

print("How input data looks like?")
print("-"*20)
# --------------

input_data = """
First lets look at a fragment of log file....

fcrawler.looksmart.com - - [26/Apr/2000:00:00:12 -0400] "GET /contacts.html HTTP/1.0" 200 4595 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"
fcrawler.looksmart.com - - [26/Apr/2000:00:17:19 -0400] "GET /news/news.html HTTP/1.0" 200 16716 "-" "FAST-WebCrawler/2.1-pre2 (ashen@looksmart.net)"

ppp931.on.bellglobal.com - - [26/Apr/2000:00:16:12 -0400] "GET /download/windows/asctab31.zip HTTP/1.0" 200 1540096 "http://www.htmlgoodies.com/downloads/freeware/webdevelopment/15.html" "Mozilla/4.7 [en]C-SYMPA  (Win95; U)"

123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:47 -0400] "GET /asctortf/ HTTP/1.0" 200 8130 "http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/5star2000.gif HTTP/1.0" 200 4005 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:50 -0400] "GET /pics/5star.gif HTTP/1.0" 200 1031 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /pics/a2hlogo.jpg HTTP/1.0" 200 4282 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"
123.123.123.123 - - [26/Apr/2000:00:23:51 -0400] "GET /cgi-bin/newcount?jafsof3&width=4&font=digital&noshow HTTP/1.0" 200 36 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"

(Note, I've added some space for clarity, and changed the IP number to 123.123.123.123 to protect the privacy of the actual visitor)

The fragment shown represents three visitors to my web site
"""

print(input_data)

print("#"*40, end="\n\n")
###################################

print("type of input_data")
print("-"*20)
# --------------

print(type(input_data))

print("#"*40, end="\n\n")
###################################

print("input_data in raw format")
print("-"*20)
# --------------

print(repr(input_data))

print("#"*40, end="\n\n")
###################################

print("List of lines")
print("-"*20)
# --------------

# list_of_lines = input_data.split("\n")
list_of_lines = input_data.splitlines() # split by newline character \n
print(list_of_lines)

print("#"*40, end="\n\n")
###################################

print("Access each line")
print("-"*20)
# --------------

for each_line in list_of_lines:
    print("Each Line:", each_line)

print("#"*40, end="\n\n")
###################################


print("print only IP address line")
print("-"*20)
# --------------

for each_line in list_of_lines:
    if each_line.startswith('123'):
        print("Each Line:", each_line)

print("#"*40, end="\n\n")
###################################

print("Extract Info")
print("-"*20)
# --------------

for each_line in list_of_lines:
    if each_line.startswith('123'):
        sp = each_line.split()
        # print("Splitted Values In List:", sp)

        ip = sp[0]

        raw_img = sp[6] # '/pics/wpaper.gif'

        # 1-way to Remove '/pics/' from '/pics/wpaper.gif'
        raw_img_sp = raw_img.split("/") # ['', 'pics', 'wpaper.gif']
        # print(raw_img_sp) # ['', 'pics', 'wpaper.gif']
        img_1 = raw_img_sp[-1]

        # 2-way to Remove '/pics/' from '/pics/wpaper.gif'
        img_2 = raw_img[6:]

        # 3-way to Remove '/pics/' from '/pics/wpaper.gif'
        img_3 = raw_img.removeprefix("/pics/")

        # raw_img = sp[6] # '/pics/wpaper.gif'
        # if raw_img.startswith("/pics/"):
        if raw_img.endswith(".jpg") or raw_img.endswith(".gif"):
            img = raw_img.removeprefix("/pics/")
        else:
            img = "No Image"

        print(ip, img, sep="\t\t")

print("#"*40, end="\n\n")
###################################
