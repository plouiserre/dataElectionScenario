from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from infrastructure.adapter.AdaptDepartments import AdaptDepartments
from infrastructure.adapter.AdaptDistrict import AdaptDistrict
from infrastructure.adapter.AdaptElection import AdaptElection
from infrastructure.adapter.AdaptParties import AdaptParties

class AdaptResultsElections : 
    def __init__(self):
        self.elections_json = ''
        self.departments_json = ''
        self.parties_json = ''
        self.elections = []
        self.departments = []
        pass

    def to_json(self, result_datas): 
        #tmp code
        self.elections = result_datas.elections
        self.departments = result_datas.departments
        self.parties = result_datas.parties
        # self.__districts_json()
        self.__elections_json()
        self.__departments_json()
        self.__parties_json()
        result_datas_json = self.__results_data_json()      
        return result_datas_json

    def __elections_json(self):
        self.elections_json += "{\"elections\":["
        for i, election in enumerate(self.elections):
            adapt_candidate = AdaptCandidate()
            adapt_district = AdaptDistrict(adapt_candidate)
            adapt_election = AdaptElection(adapt_district)
            json_election = adapt_election.to_json(election)
            if(i == len(self.elections) - 1):
                self.elections_json += json_election            
            else :
                self.elections_json += json_election +","
        self.elections_json += "]"

    def __departments_json(self):
        adapt_departments = AdaptDepartments()
        self.departments_json = adapt_departments.to_json(self.departments)

    def __parties_json(self):
        adapt_parties = AdaptParties()
        self.parties_json = adapt_parties.to_json(self.parties)
        self.parties_json += "}"

    def __results_data_json(self):
        result_data_json_inside = "{all_elections}, {all_departments}, {all_parties}".format(
            all_elections = self.elections_json, all_departments = self.departments_json, 
            all_parties = self.parties_json
        )
        result_data_json = "{\"elections_results\" : " + result_data_json_inside+ "}"
        return result_data_json