import csv
path = r"C:\Users\Vidya\PycharmProjects\Alpha_3_batch\files_directory\csv_files\sample.csv"
with open(path) as csv_file:
    read_obj = csv.reader(csv_file)
    print(read_obj)
    for row in read_obj:
        print(row)

# with open(path) as csv_file:
#     read_obj = csv.DictReader(csv_file)
#     print(read_obj)
#     for row in read_obj:
#         print(row)