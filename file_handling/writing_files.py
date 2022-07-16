f_path = r"C:\Users\Vidya\PycharmProjects\Alpha_3\files_directory\txt_log_files\file1.txt"
# with open(path + "my_file1.txt.txt", "a") as file:
#     file.writelines(["hai\n", "hello\n", "python"])


""" copy content of sample.txt into different file """
path = r"C:\Users\Vidya\PycharmProjects\Alpha_3\files_directory\txt_log_files\sample.txt"

with open(path, "r") as file_read, open(f_path, "w") as file_write:
        for line in file_read:
            file_write.write(line)
















