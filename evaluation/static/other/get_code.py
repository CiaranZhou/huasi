import xlrd
import pymysql
from tqdm import tqdm

db = pymysql.connect('localhost', 'root', '19990620zyh@', 'huasi')
cursor = db.cursor()
fr = xlrd.open_workbook(r'D:/Documents/files/huasi/form.xlsx')
sheet = fr.sheet_by_index(0)
merged = sheet.merged_cells
max_row = sheet.nrows
b = sheet.col_values(5)[1:]
d = []
for i in b:
    for j in i.split('/'):
        if j not in d:
            d.append(j)
i = 3
for r in tqdm(range(3, max_row)):
    c = 5
    cell_value = sheet.row_values(r)[c]
    if cell_value is None or cell_value == '':
        cell_value = get_merged_cells_value(sheet, merged, r, c)
    for m in cell_value.split('/'):
        sql = "INSERT INTO evaluation_recommend_psy_code(id, recommend_id, psycode_id) VALUES ('%d', '%d', '%d')" % (i, r, d.index(m)+1)
        try:
            cursor.execute(sql)
            i += 1
            db.commit()
        except:
            db.rollback()
    # print(s)
cursor.close()
db.close()
