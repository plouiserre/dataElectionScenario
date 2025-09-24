from usecases.Retrieve import Retrieve
from domain.ResultDistrictElection import ResultDistrictElection

class RetrieveResultElectionDistrict(Retrieve):
    def __init__(self):
        super().__init__()


    def Search(self):
        result = ResultDistrictElection()
        result.District.departmentNumber = 1
        result.District.label = '1ère circonscription'
        result.District.number = 101
        result.District.registered = 86843
        result.District.voting = 61830
        return result