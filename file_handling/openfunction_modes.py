import os

f_path = r"C:\Users\Vidya\PycharmProjects\Alpha_3\files_directory\txt_log_files"

# print(os.getcwd())
os.chdir(f_path)
# print(os.getcwd())

# without context manager
f = open("sample.txt", "r")
print(f)
print(f.closed)     # False
f.close()
print(f.closed)     # True

# using context manager
with open("sample.txt") as f:
    print(f)
    print(f.closed)     # False

print(f.closed)     # True


# f = open("sample.txt", "w")
# print(f)

# f = open("sample.txt", "a")
# print(f)

# creating a file
# f = open("my_file1.txt.txt", "w")
# print(f)

# f = open("file2.txt", "a")
# print(f)

# f = open("sample1.txt", "x")
# print(f)
