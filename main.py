from ports.outside.files.ExcelElection import ExcelElection

print("lecture données")
excelManager = ExcelElection()
datas = excelManager.Load()
for line in datas :
    print(line)
print("fin lecture")


#packages à installer 
#wheel 
#pandas 
#openpyxl