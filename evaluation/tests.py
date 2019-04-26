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
a = sheet.col_values(0)[1:]
b = sheet.col_values(1)[1:]
c = sheet.col_values(2)[1:]
d = set()
for i in range(len(b)):
    if not b[i] in d:
        d.add(b[i])
        print(a[i], b[i], int(c[i]))
