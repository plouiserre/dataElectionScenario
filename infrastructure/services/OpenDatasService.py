from usecases.ports.outside.DataServices import DataServices
from domain.ResultDatas import ResultDatas

class OpenDataServices(DataServices) : 
    def __init__(self, excelElection, jsonFile, adaptDepartment, adaptElectionData, adapt_election, party_memory):
        self.ExcelElection = excelElection
        self.JsonFile = jsonFile
        self.AdaptDepartment = adaptDepartment
        self.AdaptElectionsData = adaptElectionData
        self.AdaptElection = adapt_election
        self.party_memory = party_memory
        self.elections = []
        self.departments = []
        self.parties = []

    def RetrieveDatas(self):
        all_datas = self.ExcelElection.Load()
        self.__retrieveElections(all_datas)
        self.__retrieveDepartments(all_datas)
        self.__retrieve_parties() 
        resultFinals = ResultDatas()
        resultFinals.departments = self.departments
        resultFinals.elections = self.elections
        resultFinals.parties = self.parties
        return resultFinals
    
    def __retrieveElections(self, datas):
        for key, data in datas.items() : 
            election = self.AdaptElection.Transform(data, key)
            self.elections.append(election)

    def __retrieveDepartments(self, datas): 
         first_year = list(datas.keys())[0]
         for data in datas[first_year] : 
            department = self.AdaptDepartment.Transform(data, first_year)
            self.departments.append(department)     
    
    def __retrieve_parties(self):        
        self.parties = self.party_memory.get_all_parties()

    def SaveDatas(self, result_datas):
        json = self.AdaptElectionsData.to_json(result_datas)
        self.JsonFile.write(json)
        return True    