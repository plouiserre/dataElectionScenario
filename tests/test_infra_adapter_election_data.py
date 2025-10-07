import unittest
from tests.utils.build_department import build_departments, construct_departments_json
from tests.utils.build_district import  builds_three_districts, construct_districts_json
from infrastructure.adapter.AdaptElectionData import AdaptElectionData
from domain.ResultDatas import ResultDatas
from domain.Department import Department
from domain.Party import Party

class AdaptElectionDataTest(unittest.TestCase):
    def test_districts_are_finded(self):
        adaptElectionData = AdaptElectionData()
        result_data = self.__construct_result_data()

        json_result = adaptElectionData.to_json(result_data)

        json_expected = self.__construct_json_result()
        self.assertEqual(json_expected, json_result)

    def __construct_json_result(self): 
        result_data = self.__construct_result_data()
        result_data_json = self.__construct_json_result_data(result_data)
        return result_data_json        

    def __construct_result_data(self):
        result = ResultDatas()
        result.Districts =  builds_three_districts()
        result.Departments = build_departments()
        result.Parties = self.__construct_parties()
        return result

    def __construct_parties(self):
        first_party = self.__construct_party('UG', 'Union de la gauche')
        second_party = self.__construct_party('ENS', 'Ensemble ! (Majorité présidentielle)')
        third_party = self.__construct_party('LR', 'Les Republicains')
        fourth_party = self.__construct_party('RN', 'Rassemblement National')
        parties = []
        parties.append(first_party)
        parties.append(second_party)
        parties.append(third_party)
        parties.append(fourth_party)
        return parties    

    def __construct_party(self, code, name): 
        party = Party()
        party.code = code
        party.name = name
        return party    

    def __construct_json_result_data(self, result_data):
        all_districts_json = construct_districts_json(result_data.Districts)
        all_departments_json = construct_departments_json(result_data.Departments)
        all_parties_json = self.__construct_parties_json(result_data.Parties)
        result_data_json_inside = "{all_districts}, {all_departments}, {all_parties}".format(
            all_districts = all_districts_json, all_departments = all_departments_json, 
            all_parties = all_parties_json
        )
        result_data_json = "{\"result_data\" : {" + result_data_json_inside+ "}}"
        return result_data_json    

    def __construct_parties_json(self, parties):
        first_party_json = self.__construct_party_json(parties[0])
        second_party_json = self.__construct_party_json(parties[1])
        third_party_json = self.__construct_party_json(parties[2])
        fourth_party_json = self.__construct_party_json(parties[3])
        parties_json_concat = "\"parties\":[{first_party}, {second_party}, {third_party}, {fourth_party}]".format(
            first_party = first_party_json, second_party = second_party_json, third_party = third_party_json,
            fourth_party = fourth_party_json
        )
        return parties_json_concat        

    def __construct_party_json(self, party):
        json_party = "\"name\":\"{name}\",\"code\":\"{code}\"".format(
            name = party.name, code = party.code
        )
        json_final = "{"+json_party+"}"
        return json_final