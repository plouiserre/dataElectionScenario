from infrastructure.files.ExcelElection import ExcelElection
from infrastructure.services.OpenDatasService import OpenDataServices
from usecases.AdaptResultElectionData.CalculateElectionData import CalculateElectionData
from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from infrastructure.adapter.AdaptDepartment import AdaptDepartment
from infrastructure.adapter.AdaptDistrict import AdaptDistrict
from infrastructure.memory.party_memory import PartyMemory
from infrastructure.files.JsonFile import JsonFile


print("lecture données")
excelManager = ExcelElection()
adaptCandidate = AdaptCandidate()
adaptDistrict = AdaptDistrict(adaptCandidate)
adaptDepartment  = AdaptDepartment()
party_memory = PartyMemory()
datas = excelManager.Load()
for line in datas :
    print(line)
openDataServices = OpenDataServices(excelManager, adaptDistrict, adaptDepartment, party_memory)
calcul = CalculateElectionData(openDataServices)
calcul.Calculate()

jsonFile = JsonFile()
jsonFile.write("apeoiizf")
print("fin lecture")


#packages à installer 
#wheel 
#pandas 
#openpyxl