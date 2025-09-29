from infrastructure.files.ExcelElection import ExcelElection
from infrastructure.services.OpenDatasService import OpenDataServices
from usecases.AdaptResultElectionData.CalculateElectionData import CalculateElectionData
from usecases.AdaptResultElectionData.RetrieveParty import RetrieveParty
from usecases.AdaptResultElectionData.RetrieveResultDepartment import RetrieveResultDepartment
from usecases.AdaptResultElectionData.RetrieveResultElectionDistrict import RetrieveResultElectionDistrict

print("lecture données")
excelManager = ExcelElection()
datas = excelManager.Load()
for line in datas :
    print(line)
openDataServices = OpenDataServices(excelManager)
calcul = CalculateElectionData(openDataServices)
calcul.Calculate()
print("fin lecture")


#packages à installer 
#wheel 
#pandas 
#openpyxl