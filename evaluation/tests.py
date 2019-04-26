from django.test import TestCase

# Create your tests here.
import xlrd

fr = xlrd.open_workbook(r'D:/Documents/files/huasi/form.xlsx')
sheet = fr.sheet_by_index(0)
# fl = open(r'perfession.txt', 'w')
# for i in sheet.col_values(4)[1:]:
#     i += '\n'
#     fl.write(i)
# fl.close()
s = sheet.col_values(9)[1:]
# for i in s:
#     print(i)
print(max(map(len, s)))
