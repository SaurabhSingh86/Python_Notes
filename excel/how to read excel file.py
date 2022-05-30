# Step 1: First we have to import xlrd
import xlrd

excel_file_path = r"C:\Users\Saurabh\Desktop\Mark_sheet.xlsx"

# Step 2: opening the excel file / workbook
book = xlrd.open_workbook(excel_file_path)

# Step 3: Opening the spreadsheet & getting its handle
sheet = book.sheet_by_name("Marks_Sheet1")

# Step 4: get the data in entire sheet
data = sheet.get_rows()

# skip the headers
header = next(data)

# get each row
mark_sheets = {}
for row in data:
    mark_sheets[row[0].value] = (row[1].value, row[2].value)

print(mark_sheets)
