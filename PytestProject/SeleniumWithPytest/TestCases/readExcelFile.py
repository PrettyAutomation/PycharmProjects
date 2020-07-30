import xlrd

file_Location = "/Users/pretty.sanwale/PycharmProjects/PytestProject/resource/ExcelData.xlsx";
workbook = xlrd.open_workbook(file_Location);
sheet = workbook.sheet_by_index(0)
row = sheet.nrows
col = sheet.ncols

data = [[sheet.cell_value(r, c) for c in range(col)] for r in range(row)]
print(data)
data1 = []

for i in range(row):
    for j in range(col):
        data1.append(sheet.cell_value(i, j))
print(data1)

