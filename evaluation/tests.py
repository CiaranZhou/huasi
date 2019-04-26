from django.test import TestCase

# Create your tests here.
import xlrd

fr = xlrd.open_workbook(r'D:/Documents/files/huasi/form.xlsx')
sheet = fr.sheet_by_index(0)
merged = sheet.merged_cells
max_col = sheet.ncols - 9
max_row = sheet.nrows
b = sheet.col_values(5)[1:]
d = []
for i in b:
    for j in i.split('/'):
        if j not in d:
            d.append(j)
# for r in range(3, max_row):
#     s = []
#     for c in range(max_col):
#         cell_value = sheet.row_values(r)[c]
#         if cell_value is None or cell_value == '':
#             cell_value = get_merged_cells_value(sheet, merged, r, c)
#         if type(cell_value) == float:
#             cell_value = str(int(cell_value))
#         s.append(str(cell_value))
print(d)
print(len(d))
