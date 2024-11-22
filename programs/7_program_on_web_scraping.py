"""
Program on web scraping using beautifulsoup library

In this case, get log data
"""

print("Get data from website and print")
print("-"*20)
# --------------

import urllib.request as u

my_web_file_handle = u.urlopen("https://www.jafsoft.com/searchengines/log_sample.html")
web_content = my_web_file_handle.read()
my_web_file_handle.close()

print(web_content)

print("#"*40, end="\n\n")
###################################

print("Created object of Beautifulsoup class object and store website data")
print("-"*20)
# --------------

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')
print(soup)

print("#"*40, end="\n\n")
###################################

print("Title Tag")
print("-"*20)
# --------------

print(soup.head.title) # <TITLE>A Web server log file explained</TITLE>

print("#"*40, end="\n\n")
###################################

print("Title Tag Text")
print("-"*20)
# --------------

print(soup.head.title.text) # A Web server log file explained

print("#"*40, end="\n\n")
###################################

print("Get log data:")
print("-"*20)
# --------------

log_data = soup.body.pre.text
print(log_data)

print("#"*40, end="\n\n")
###################################

print("type of log data:")
print("-"*20)
# --------------

log_data = soup.body.pre.text
print(type(log_data))

print("#"*40, end="\n\n")
###################################

print("log data in raw format")
print("-"*20)
# --------------

log_data = soup.body.pre.text
print(repr(log_data))

print("#"*40, end="\n\n")
###################################
