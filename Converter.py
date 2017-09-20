from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd
from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation

df=pd.DataFrame.from_csv('Data.csv', sep=';', index_col=None)

wb = Workbook()
ws = wb.active

for r in dataframe_to_rows(df, index=False, header=True):
    ws.append(r)

wb.save("pandas_openpyxl.xlsx")
