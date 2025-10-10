from infrastructure.files.ExcelElection import ExcelElection
from infrastructure.files.JsonFile import JsonFile
from infrastructure.services.OpenDatasService import OpenDataServices
from usecases.AdaptResultElectionData.CalculateElectionData import CalculateElectionData
from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from infrastructure.adapter.AdaptDepartment import AdaptDepartment
from infrastructure.adapter.AdaptDistrict import AdaptDistrict
from infrastructure.adapter.AdaptElectionData import AdaptElectionData
from infrastructure.memory.party_memory import PartyMemory


print("lecture données")
excelManager = ExcelElection()
json_files = JsonFile()
adaptCandidate = AdaptCandidate()
adaptDistrict = AdaptDistrict(adaptCandidate)
adaptDepartment  = AdaptDepartment()
adapt_election_data = AdaptElectionData()
party_memory = PartyMemory()
datas = excelManager.Load()
for line in datas :
    print(line)
openDataServices = OpenDataServices(excelManager, json_files, adaptDistrict, adaptDepartment, adapt_election_data, party_memory)
calcul = CalculateElectionData(openDataServices)
calcul.Calculate()
print("fin lecture")


#packages à installer 
#wheel 
#pandas 
#openpyxl