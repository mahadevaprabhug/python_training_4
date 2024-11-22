"""
Write a function which takes log_file_path as an argument
then
it should read log file
then
it should extract info
then
it should return extracted info in dictionary
{0:(ip, img), 1:(ip, img), 2:(ip, img)}
"""

print("Function to process log file")
print("-"*20)
# --------------


def log_file_process_function(log_file_path):
    """
    get data from log file and return extracted info
    :param log_file_path:
    :return dictionary:
    """
    my_log_file_handle = open(log_file_path, "rb")
    log_file_content = my_log_file_handle.readlines()
    my_log_file_handle.close()

    # Output =  {0:(ip, img), 1:(ip, img), 2:(ip, img)}
    #
    my_output_dictionary = {}
    key = 0
    for each_line in log_file_content:
        if each_line.startswith(b"123"):
            # OPTION-1
            # each_line = each_line.decode() # Convert string
            # OR
            # OPTION-2
            sp = each_line.split()
            # print(sp)
            ip = sp[0]  # bytes
            ip = ip.decode()  # String

            raw_img = sp[6]  # Ex: b'/pics/wpaper.gif'

            if raw_img.endswith(b".jpg") or raw_img.endswith(b".gif"):
                img = raw_img.removeprefix(b"/pics/")
                img = img.decode()
            else:
                img = "No Image"

            each_line_tuple = (ip, img)
            my_output_dictionary[key] = each_line_tuple
            key = key+1
    return my_output_dictionary

print("#"*40, end="\n\n")
###################################

print("Calling log process function")
print("-"*20)
# --------------

log_process_function_output = log_file_process_function(r"../log/web_server.log")
print(log_process_function_output)

print("#"*40, end="\n\n")
###################################

