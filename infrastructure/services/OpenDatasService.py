from usecases.ports.outside.DataServices import DataServices
from domain.ResultDatas import ResultDatas

class OpenDataServices(DataServices) : 
    def __init__(self, excelElection, jsonFile, adaptDistrict, adaptDepartment, adaptElectionData, party_memory):
        self.ExcelElection = excelElection
        self.JsonFile = jsonFile
        self.AdaptDistrict = adaptDistrict
        self.AdaptDepartment = adaptDepartment
        self.AdaptElectionData = adaptElectionData
        self.party_memory = party_memory
        self.districts = []
        self.departments = []
        self.parties = []

    def RetrieveDatas(self):
        all_datas = self.ExcelElection.Load()
        datas = all_datas[2022]
        self.__retrieveDistricts(datas)
        self.__retrieveDepartments(datas)
        self.__retrieve_parties()
        resultFinals = ResultDatas()
        resultFinals.Departments = self.departments
        resultFinals.Districts = self.districts
        resultFinals.Parties = self.parties
        return resultFinals
    
    def __retrieveDistricts(self, datas):
        for data in datas : 
            district = self.AdaptDistrict.Transform(data)
            self.districts.append(district)        

    def __retrieveDepartments(self, datas): 
         for data in datas : 
            department = self.AdaptDepartment.Transform(data)
            self.departments.append(department)     
    
    def __retrieve_parties(self):        
        self.parties = self.party_memory.get_all_parties()

    def SaveDatas(self, result_datas):
        json = self.AdaptElectionData.to_json(result_datas)
        self.JsonFile.write(json)
        return True
    