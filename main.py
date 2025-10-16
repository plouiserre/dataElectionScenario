from infrastructure.files.ExcelElection import ExcelElection
from infrastructure.files.JsonFile import JsonFile
from infrastructure.services.OpenDatasService import OpenDataServices
from usecases.AdaptResultElectionData.CalculateElectionData import CalculateElectionData
from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from infrastructure.adapter.AdaptDepartment import AdaptDepartment
from infrastructure.adapter.AdaptDistrict import AdaptDistrict
from infrastructure.adapter.AdaptElection import AdaptElection
from infrastructure.adapter.AdaptResultsElections import AdaptResultsElections
from infrastructure.memory.party_memory import PartyMemory


print("lecture données")
# paths = ["C:/Users/ploui/Projects/dataElectionScenario/openDatas/2024-circonscriptions.xlsx", "C:/Users/ploui/Projects/dataElectionScenario/openDatas/2022-circonscriptions.xlsx"]
# keys = [2022, 2024]
paths = ["C:/Users/ploui/Projects/dataElectionScenario/openDatas/2024-circonscriptions.xlsx"]
keys = [2024]
# paths = ["C:/Users/ploui/Projects/dataElectionScenario/openDatas/2022-circonscriptions.xlsx"]
# keys = [2022]

excelManager = ExcelElection(keys, paths)
json_files = JsonFile()
adaptCandidate = AdaptCandidate()
adaptDistrict = AdaptDistrict(adaptCandidate)
adapt_election = AdaptElection(adaptDistrict)
adaptDepartment  = AdaptDepartment()
adapt_results_elections = AdaptResultsElections()
party_memory = PartyMemory()
datas = excelManager.Load()
for line in datas :
    print(line)
openDataServices = OpenDataServices(excelManager, json_files, adaptDepartment, adapt_results_elections, adapt_election, party_memory)
calcul = CalculateElectionData(openDataServices)
calcul.Calculate()
print("fin lecture")


#packages à installer 
#wheel 
#pandas 
#openpyxl