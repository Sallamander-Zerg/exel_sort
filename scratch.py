import openpyxl
import pandas as pd
from collections import defaultdict
d = defaultdict(list)


table = openpyxl.load_workbook(filename="FEREKS.xlsx")
sheet = table.active
table_row = sheet.max_row

obj_table1 = pd.read_excel('FEREKS.xlsx', header=None, usecols='A,B')
dfs = []


for i in range(0,table_row):
    sample = obj_table1[27 * i + 1: 27 * (i + 1)]
    dfs.append(sample)
print(dfs)
ret = pd.concat(dfs)
ret_list = ret.values.tolist()
for h, n in ret_list:
    d[h].append(n)
df = pd.DataFrame([d])
df.to_excel("1.xlsx")
print(d)

