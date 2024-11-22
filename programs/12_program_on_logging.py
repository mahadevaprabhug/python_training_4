"""
logging: Capture logs in file
"""

print("Configuring Logging and Testing Logging ")
print("-"*20)
# --------------

import logging

# Configure logging
logging.basicConfig(filename="my_log.log", filemode="w", level=logging.DEBUG, format="%(levelname)s : %(filename)s : %(message)s")
my_logger = logging.getLogger(__name__)

my_logger.info("This is info")
my_logger.debug("This is debug")
my_logger.warning("This is warning")
my_logger.error("This is error")
my_logger.critical("This is critical")

print("""
Log captured in my_log.log, Please check
""")

print("#"*40, end="\n\n")
###################################

print("Write some data to file and capture the log in 'my_log.log'")
print("-"*20)
# --------------

try:
    my_logger.info("Opening file..")
    my_file_handle = open("testfile.txt", "w")
    my_logger.info("Opening file Success")
except:
    my_logger.error("Opening file failed")
    my_logger.info("Exiting")
    exit()
else:
    my_logger.info("Writing to file")
    my_file_handle.write("Hello")
    my_logger.info("Writing to file success")
finally:
    my_logger.info("Closing file handle")
    my_file_handle.close()
    my_logger.info("Closing file handle Done")

print("""
Log captured in my_log.log, Please check
""")

print("#"*40, end="\n\n")
###################################
