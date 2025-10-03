from infrastructure.files.ExcelElection import ExcelElection
from infrastructure.services.OpenDatasService import OpenDataServices
from usecases.AdaptResultElectionData.CalculateElectionData import CalculateElectionData
from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from infrastructure.adapter.AdaptDepartment import AdaptDepartment
from infrastructure.adapter.AdaptDistrict import AdaptDistrict


print("lecture données")
excelManager = ExcelElection()
adaptCandidate = AdaptCandidate()
adaptDistrict = AdaptDistrict(adaptCandidate)
adaptDepartment  = AdaptDepartment()
datas = excelManager.Load()
for line in datas :
    print(line)
openDataServices = OpenDataServices(excelManager, adaptDistrict, adaptDepartment )
calcul = CalculateElectionData(openDataServices)
calcul.Calculate()
print("fin lecture")


#packages à installer 
#wheel 
#pandas 
#openpyxl