import pymysql
import xlrd
from tqdm import tqdm


def get_merged_cells_value(sheet, merged, row_index, col_index):
    """
    先判断给定的单元格，是否属于合并单元格；
    如果是合并单元格，就返回合并单元格的内容
    :return:
    """
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
                return cell_value
    return None


db = pymysql.connect('localhost', 'root', '19990620zyh@', 'huasi')
cursor = db.cursor()
fr = xlrd.open_workbook(r'D:/Documents/files/huasi/form.xlsx')
sheet = fr.sheet_by_index(0)
merged = sheet.merged_cells
max_row = sheet.nrows
i = 5
for r in tqdm(range(3, max_row)):
    c = 6
    cell_value = sheet.row_values(r)[c]
    if cell_value is None or cell_value == '':
        cell_value = get_merged_cells_value(sheet, merged, r, c)
    if cell_value.find('专科') >= 0:
        sql = "INSERT INTO evaluation_recommend_education_level(id, recommend_id, educationlevel_id) VALUES ('%d', '%d', '%d')" % (i, r, 1)
        try:
            cursor.execute(sql)
            i += 1
            db.commit()
        except:
            db.rollback()
    if cell_value.find('本科') >= 0:
        sql = "INSERT INTO evaluation_recommend_education_level(id, recommend_id, educationlevel_id) VALUES ('%d', '%d', '%d')" % (i, r, 2)
        try:
            cursor.execute(sql)
            i += 1
            db.commit()
        except:
            db.rollback()
    if cell_value.find('研究生') >= 0:
        sql = "INSERT INTO evaluation_recommend_education_level(id, recommend_id, educationlevel_id) VALUES ('%d', '%d', '%d')" % (i, r, 3)
        try:
            cursor.execute(sql)
            i += 1
            db.commit()
        except:
            db.rollback()
    # print(s)
cursor.close()
db.close()
