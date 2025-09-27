from usecases.AdaptResultElectionData.Retrieve import Retrieve
from domain.Candidate import Candidate
from domain.ResultDistrictElection import ResultDistrictElection

class RetrieveResultElectionDistrict(Retrieve):
    def __init__(self):
        super().__init__()


    def Search(self):
        result = ResultDistrictElection()
        result.District.label = '10ème circonscription'
        result.District.number = 3310
        result.District.registered = 83589
        result.District.voting = 59039
        firstCandidate = self.__generateCandidate('HALBIN', 'Hélène', 'EXG', 'FEMININ', 1117, 1.34, 1.95, False, 101)
        secondCandidate = self.__generateCandidate('BOUDIÉ', 'Florent', 'ENS', 'MASCULIN', 17128, 20.49, 29.96, False, 101)
        thirdCandidate = self.__generateCandidate('BOURGOIS', 'Pascal', 'UG', 'MASCULIN', 13885, 16.61, 24.29, False, 101)
        fourthCandidate = self.__generateCandidate('CHADOURNE', 'Sandrine', 'RN', 'FEMININ', 25037, 29.95, 43.8, False, 101)        
        result.Candidates.append(firstCandidate)
        result.Candidates.append(secondCandidate)
        result.Candidates.append(thirdCandidate)
        result.Candidates.append(fourthCandidate)
        return result

    
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