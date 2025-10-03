from usecases.ports.outside.DataServices import DataServices
from domain.Department import Department
from domain.Party import Party
from domain.ResultDatas import ResultDatas

class OpenDataServices(DataServices) : 
    def __init__(self, excelElection, adaptDistrict, adaptDepartment):
        self.ExcelElection = excelElection
        self.AdaptDistrict = adaptDistrict
        self.AdaptDepartment = adaptDepartment
        self.districts = []
        self.departments = []

    def RetrieveDatas(self):
        datas = self.ExcelElection.Load()
        self.__retrieveDistricts(datas)
        self.__retrieveDepartments(datas)
        parties = self.__constructsParties()
        resultFinals = ResultDatas()
        resultFinals.Departments = self.departments
        resultFinals.Districts = self.districts
        resultFinals.Parties = parties
        return resultFinals
    
    def __retrieveDistricts(self, datas):
        for data in datas : 
            district = self.AdaptDistrict.Transform(data)
            self.districts.append(district)        

    def __retrieveDepartments(self, datas): 
         for data in datas : 
            department = self.AdaptDepartment.Transform(data)
            self.departments.append(department)     
    
    def __constructsParties(self):        
        firstParty = self.__setParties('UG', 'Union de la gauche')
        secondParty = self.__setParties('ENS', 'ENS Ensemble ! (Majorité présidentielle)')
        thirdParty = self.__setParties('LR', 'Les Républicains')
        fourthParty = self.__setParties('DVD', 'Divers droite')
        fifthParty = self.__setParties('RN', 'Rassemblement National')
        parties = []
        parties.append(firstParty)
        parties.append(secondParty)
        parties.append(thirdParty)
        parties.append(fourthParty)
        parties.append(fifthParty)
        return parties
    

    def __setParties(self, code, name): 
        party = Party()
        party.code = code
        party.name = name
        return party
    
    