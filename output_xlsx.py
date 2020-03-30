import xlrd as xlrd
import xlsxwriter as xlsxwriter

# create and write sheets
# Method 1:
xl = xlrd.open_workbook('xx.xlsx')
table = xl.sheets()[0]
row = table.row_values(0)
col = table.colvalues(0)
print(table.nrows, table.ncols, table.cell(0, 0).value)

# Method 2:
xl = xlsxwriter.Workbook('xx.xlsx')
table = xl.add_worksheet('sheet1')
table.write_string(0, 0, 'xx')
table.set_column('C:E', 15)
xl.close()
