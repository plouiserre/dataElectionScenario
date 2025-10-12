from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from infrastructure.adapter.AdaptDepartments import AdaptDepartments
from infrastructure.adapter.AdaptDistrict import AdaptDistrict
from infrastructure.adapter.AdaptParty import AdaptParty

class AdaptElectionData : 
    def __init__(self):
        self.districts_json = ''
        self.departments_json = ''
        self.parties_json = ''
        self.districts = []
        self.departments = []
        pass

    def to_json(self, result_datas): 
        self.districts = result_datas.Districts
        self.departments = result_datas.Departments
        self.parties = result_datas.Parties
        self.__districts_json()
        self.__departments_json()
        self.__parties_json()
        result_datas_json = self.__results_data_json()      
        return result_datas_json

    def __districts_json(self):
        self.districts_json += "{\"districts\":["
        for i, district in enumerate(self.districts):
            adapt_candidate = AdaptCandidate()
            adapt_district = AdaptDistrict(adapt_candidate)
            json_district = adapt_district.to_json(district)
            if(i == len(self.districts) - 1):
                self.districts_json += json_district            
            else :
                self.districts_json += json_district +","
        self.districts_json += "]"

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
        result_data_json_inside = "{all_districts}, {all_departments}, {all_parties}".format(
            all_districts = self.districts_json, all_departments = self.departments_json, 
            all_parties = self.parties_json
        )
        result_data_json = "{\"result_data\" : " + result_data_json_inside+ "}"
        return result_data_json


    

