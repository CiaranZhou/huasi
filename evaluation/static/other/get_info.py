import pymysql
import xlrd


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
max_col = sheet.ncols - 9
max_row = sheet.nrows
b = sheet.col_values(1)[1:]
d = []
for i in b:
    if i not in d:
        d.append(i)
for r in range(3, max_row):
    s = []
    for c in range(max_col):
        cell_value = sheet.row_values(r)[c]
        if cell_value is None or cell_value == '':
            cell_value = get_merged_cells_value(sheet, merged, r, c)
        if type(cell_value) == float:
            cell_value = str(int(cell_value))
        s.append(str(cell_value))
    sql = "INSERT INTO evaluation_recommend(id, name, profession_code, core_course, high_school_curriculum, career_direction, sub_category_id) VALUES ('%d', '%s', '%s', '%s', '%s','%s', '%d')" % (r, s[4], s[3], s[7], s[8], s[9], d.index(s[1])+1)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    # print(s)
cursor.close()
db.close()
