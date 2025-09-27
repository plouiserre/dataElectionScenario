from ports.outside.files.ExcelElection import ExcelElection
from usecases.AdaptResultElectionData.CalculateElectionData import CalculateElectionData
from usecases.AdaptResultElectionData.RetrieveParty import RetrieveParty
from usecases.AdaptResultElectionData.RetrieveResultDepartment import RetrieveResultDepartment
from usecases.AdaptResultElectionData.RetrieveResultElectionDistrict import RetrieveResultElectionDistrict

print("lecture données")
excelManager = ExcelElection()
datas = excelManager.Load()
for line in datas :
    print(line)
retrieveParties = RetrieveParty()
retrieveDepartment = RetrieveResultDepartment()
retrieveElectionDistrict = RetrieveResultElectionDistrict()
calcul = CalculateElectionData(retrieveParties, retrieveDepartment, retrieveElectionDistrict)
calcul.Calculate()
print("fin lecture")


#packages à installer 
#wheel 
#pandas 
#openpyxl