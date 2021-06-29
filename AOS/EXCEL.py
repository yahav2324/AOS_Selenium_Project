from openpyxl import load_workbook
workbook = load_workbook(filename=r"C:\Users\yahav\Desktop\AOS test.xlsx")
sheet = workbook.active
category = []
# category = sheet["C2:k2"].value

for row in sheet.iter_rows(min_row=2, max_row=2, min_col=3, max_col=11, values_only=True):
    category += (row)
print(category)
