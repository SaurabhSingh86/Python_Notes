import os
path = r"C:\Users\Vidya\PycharmProjects\Alpha_3\files_directory\txt_log_files"
os.chdir(path)

# with open("sample.txt", "r") as file:
#     print(file.closed)      # False
#     print(file.mode)        # r
#     print(file.name)        # sample.txt
#     print(file.readable())  # True
#     print(file.writable())  # False


# opening a file in both read and write mode
with open("sample.txt", "r+") as file:
    print(file.readable())
    print(file.writable())
