import openpyxl

wb = openpyxl.reader.excel.load_workbook(filename="W_Agri_data.xlsx")

print(wb.sheetnames)
wb.active = 0 # устанавливаем активный лист (сейчас лист 1)

sheet = wb.active
#print(sheet['A6'].value)

for i in range(5,59):
    print(sheet['A'+str(i)].value, sheet['B'+str(i)].value, sheet['C'+str(i)].value)
