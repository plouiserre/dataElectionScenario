from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from infrastructure.adapter.AdaptDepartments import AdaptDepartments
from infrastructure.adapter.AdaptDistrict import AdaptDistrict
from infrastructure.adapter.AdaptElection import AdaptElection
from infrastructure.adapter.AdaptParty import AdaptParty

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
        self.elections = result_datas.Elections
        self.departments = result_datas.Departments
        self.parties = result_datas.Parties
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
        self.parties_json += "\"parties\":["
        for i, party in enumerate(self.parties):
            adapt_party = AdaptParty()
            json_party = adapt_party.to_json(party)
            if(i == len(self.parties) - 1):
                self.parties_json += json_party
            else :                 
                self.parties_json += json_party + ','
        self.parties_json += "]}"


    def __results_data_json(self):
        result_data_json_inside = "{all_elections}, {all_departments}, {all_parties}".format(
            all_elections = self.elections_json, all_departments = self.departments_json, 
            all_parties = self.parties_json
        )
        result_data_json = "{\"elections_results\" : " + result_data_json_inside+ "}"
        return result_data_json


    

