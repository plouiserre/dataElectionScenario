from usecases.ports.outside.DataServices import DataServices
from domain.Department import Department
from domain.Party import Party
from domain.Candidate import Candidate
from domain.District import District
from domain.ResultDatas import ResultDatas

class OpenDataServices(DataServices) : 
    def __init__(self, excelElection, adaptDistrict):
        self.ExcelElection = excelElection
        self.AdaptDistrict = adaptDistrict
        self.districts = []

    def RetrieveDatas(self):
        datas = self.ExcelElection.Load()
        self.__retrieveDistricts(datas)
        departments = self.__constructDepartments()
        parties = self.__constructsParties()
        resultFinals = ResultDatas()
        resultFinals.Departments = departments
        resultFinals.Districts = self.districts
        resultFinals.Parties = parties
        return resultFinals
    
    def __retrieveDistricts(self, datas):
        for data in datas : 
            district = self.AdaptDistrict.Transform(data)
            self.districts.append(district)        


    def __constructDepartments(self): 
        firstDepartment = self.__construct_Department('Gironde', 33)
        secondDepartment = self.__construct_Department('Morbihan', 56)
        thirdDepartment = self.__construct_Department('Savoie', 73)
        fourthDepartment = self.__construct_Department('Hauts-de-Seine', 92)
        departments = []
        departments.append(firstDepartment)
        departments.append(secondDepartment)
        departments.append(thirdDepartment)
        departments.append(fourthDepartment)        
        return departments


    def __construct_Department(self, name, number): 
        department = Department()
        department.code = number
        department.name = name
        return department
    
    
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
    
    