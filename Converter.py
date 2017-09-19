import pandas as pd
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation


table=pd.DataFrame.from_csv('Data.csv', sep=';', index_col=None)

i=0

for column in range(table.columns.size):
    for row in range(table[table.columns.values[column]].size):
        print(column)
        print(row)


wb = Workbook()
ws = wb.active

#col_d = ws1.columns[3] # 0-indexing
#for idx, cell in enumerate(col_d, 1):
#    ws.cell(row=idx, col=4).value = cell.value #1-indexing


wb.save('Data.xlsx')
