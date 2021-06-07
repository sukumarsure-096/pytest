import xlrd

def readdata():
    l =[]
    wb = xlrd.open_workbook(r'C:\Users\suren\Desktop\Book1.xls')
    sn = wb.sheet_by_name('Sheet1')
    rows = sn.get_rows()
    head = next(rows)
    for row in rows:
        if row[3].value == 'no':
            l.append((row[0].value, row[1].value,row[2].value, row[3].value))
    return l
for j in readdata():
    print(j)