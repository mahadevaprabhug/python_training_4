"""
Write class with
1) get_ips method
2) get_all methods
3) write_to_txt methods

How we need?
class LogProcessClass:
    pass

l1 = LogProcessClass("log_file.txt")
l1.get_ips()
l1.get_all()
l1.write_to_text_file('my_report_1.txt')
"""

print("Log Process Class")
print("-"*20)
# --------------


class LogProcessClass:
    def __init__(self, log_file_path):
        my_log_file_handle = open(log_file_path, "rb")
        self.log_file_content = my_log_file_handle.readlines()
        my_log_file_handle.close()

    def get_ips(self):
        ips_list = []
        for each_line in self.log_file_content:
            if each_line.startswith(b"123"):
                # OPTION-1
                # each_line = each_line.decode() # Convert string
                # OR
                # OPTION-2
                sp = each_line.split()
                # print(sp)
                ip = sp[0]  # bytes
                ip = ip.decode()  # String
                ips_list.append(ip)
        return ips_list

    def get_all(self):
        my_output_dictionary = {}
        key = 0
        for each_line in self.log_file_content:
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
                key = key + 1
        return my_output_dictionary

    def write_to_text_file(self, out_file_path):
        my_out_file_handle = open(out_file_path, "w")
        my_out_data_dictionary = self.get_all()
        # Output =  {0:(ip, img), 1:(ip, img), 2:(ip, img)}
        # d.values = [(ip, img), (ip, img), (ip, img)]
        for i, j in my_out_data_dictionary.values():
            print(i, j, sep="\t", file=my_out_file_handle)
        my_out_file_handle.close()


print("#"*40, end="\n\n")
###################################

print("Processing log file")
print("-"*20)
# --------------

l1 = LogProcessClass(r"../log/web_server.log")

only_ips = l1.get_ips()
print("only_ips:", only_ips, end="\n\n")

all_records = l1.get_all()
print("all_records:", all_records, end="\n\n")

l1.write_to_text_file("my_class_report.txt")
print("Created 'my_class_report.txt' please check")

print("#"*40, end="\n\n")
###################################
