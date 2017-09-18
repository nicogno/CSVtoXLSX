import pandas as pd

table=pd.DataFrame.from_csv('Data.csv', sep=';', index_col=None)


print(table.columns.values.tolist())
print(table)
