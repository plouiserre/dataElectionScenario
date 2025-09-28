from ports.outside.services.DataServices import DataServices
from domain.Department import Department
from domain.Party import Party
from domain.Candidate import Candidate
from domain.District import District
from domain.ResultDatas import ResultDatas

class OpenDataServices(DataServices) : 
    def __init__(self):
        pass        

    def RetrieveDatas(self):
        departments = self.__constructDepartments()
        parties = self.__constructsParties()
        districts = self.__constructsDistricts()
        resultFinals = ResultDatas()
        resultFinals.Departments = departments
        resultFinals.Districts = districts
        resultFinals.Parties = parties
        return resultFinals



    def __constructDepartments(self): 
        firstDepartment = self.__construct_Department('Ain', 1)
        secondDepartment = self.__construct_Department('Bouches-du-Rhône', 13)
        thirdDepartment = self.__construct_Department('Haute-Garonne', 31)
        fourthDepartment = self.__construct_Department('Gironde', 33)
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
    
    
    def __constructsDistricts(self):
        firstDistrict = self.__constructFirstDistrict()
        secondDistrict = self.__constructSecondDistrict()
        thirdDistrict = self.__constructThirdDistrict()
        districts = []
        districts.append(firstDistrict)
        districts.append(secondDistrict)
        districts.append(thirdDistrict)
        return districts

    
    def __constructFirstDistrict(self): 
        district = District()
        district.label = '10ème circonscription'
        district.number = 3310
        district.registered = 83589
        district.voting = 59039
        firstCandidate = self.__generateCandidate('HALBIN', 'Hélène', 'EXG', 'FEMININ', 1117, 1.34, 1.95, False, 101)
        secondCandidate = self.__generateCandidate('BOUDIÉ', 'Florent', 'ENS', 'MASCULIN', 17128, 20.49, 29.96, False, 101)
        thirdCandidate = self.__generateCandidate('BOURGOIS', 'Pascal', 'UG', 'MASCULIN', 13885, 16.61, 24.29, False, 101)
        fourthCandidate = self.__generateCandidate('CHADOURNE', 'Sandrine', 'RN', 'FEMININ', 25037, 29.95, 43.8, False, 101)        
        district.Candidates.append(firstCandidate)
        district.Candidates.append(secondCandidate)
        district.Candidates.append(thirdCandidate)
        district.Candidates.append(fourthCandidate)
        return district

    def __constructSecondDistrict(self): 
        district = District()
        district.label = '16ème circonscription'
        district.number = 1316
        district.registered = 91684
        district.voting = 61560
        firstCandidate = self.__generateCandidate('SEDDIK', 'Florent', 'REC', 'MASCULIN', 712, 0.78, 1.19, False, 1316)
        secondCandidate = self.__generateCandidate('DUBOST', 'Guy', 'EXG', 'MASCULIN', 505, 0.55, 0.84, False, 1316)
        thirdCandidate = self.__generateCandidate('KOUKAS', 'Nicolas', 'UG', 'MASCULIN', 17896, 19.52, 29.92, False, 1316)
        fourthCandidate = self.__generateCandidate('BOUZIANI', 'Samir', 'ECO', 'MASCULIN', 396, 0.43, 0.66, False, 1316)
        district.Candidates.append(firstCandidate)
        district.Candidates.append(secondCandidate)
        district.Candidates.append(thirdCandidate)
        district.Candidates.append(fourthCandidate)
        return district

    def __constructThirdDistrict(self): 
        district = District()
        district.label = '2ème circonscription'
        district.number = 7102
        district.registered = 76621
        district.voting = 53570
        firstCandidate = self.__generateCandidate('ZEKPA', 'Raymond', 'ENS', 'MASCULIN', 5094, 6.65, 9.77, False, 7102)
        secondCandidate = self.__generateCandidate('DAMIEN', 'Olivier', 'RN', 'MASCULIN', 19738, 25.76, 37.85, False, 7102)
        thirdCandidate = self.__generateCandidate('GAUTHERON', 'Sébastien', 'UG', 'MASCULIN', 9124, 11.91, 17.50, False, 7102)
        fourthCandidate = self.__generateCandidate('BERTHELOT', 'Patrick', 'EXG', 'MASCULIN', 677, 0.88, 1.30, False, 7102)   
        fifthCandidate = self.__generateCandidate('CORNELOUP', 'Josiane', 'LR', 'FEMININ', 17511, 22.85, 33.58, False, 7102)     
        district.Candidates.append(firstCandidate)
        district.Candidates.append(secondCandidate)
        district.Candidates.append(thirdCandidate)
        district.Candidates.append(fourthCandidate)
        district.Candidates.append(fifthCandidate)
        return district

    def __generateCandidate(self, lastname, firstname, partiCode, sexe, vote, voteByRegistered, voteByExpressed, isElected, districtCode):
        candidate = Candidate()
        candidate.lastName = lastname
        candidate.firstName = firstname
        candidate.sexe = sexe
        candidate.partiCode = partiCode
        candidate.vote = vote
        candidate.voteByRegistered = voteByRegistered
        candidate.voteByExpressed = voteByExpressed
        candidate.isElected = isElected
        candidate.districtCode = districtCode
        return candidate

    
