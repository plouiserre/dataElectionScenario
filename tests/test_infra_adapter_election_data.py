import unittest
from tests.utils.build_district import build_first_district, build_second_district, build_third_district, construct_district_json
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
        result.Districts =  self.__construct_districts()
        result.Departments = self.__construct_departments()
        result.Parties = self.__construct_parties()
        return result
        
    def __construct_districts(self):
        first_district = build_first_district()
        
        second_district = build_second_district()

        third_district = build_third_district()

        districts = []
        districts.append(first_district)
        districts.append(second_district)
        districts.append(third_district)
        return districts

    def __construct_departments(self): 
        first_department = self.__construct_department('33', 'Gironde')
        second_department = self.__construct_department('92', 'Hauts de Seine')
        departments = []
        departments.append(first_department)
        departments.append(second_department)
        return departments

    def __construct_department(self, code, name):
        department = Department()
        department.code = code
        department.name = name
        return department    

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
        all_districts_json = self.__construct_json_result_data_districts(result_data.Districts)
        all_departments_json = self.__construct_departments_json(result_data.Departments)
        all_parties_json = self.__construct_parties_json(result_data.Parties)
        result_data_json_inside = "{all_districts}, {all_departments}, {all_parties}".format(
            all_districts = all_districts_json, all_departments = all_departments_json, 
            all_parties = all_parties_json
        )
        result_data_json = "{\"result_data\" : {" + result_data_json_inside+ "}}"
        return result_data_json    

    def __construct_json_result_data_districts(self, districts):
        first_district_json = construct_district_json(districts[0])
        second_district_json = construct_district_json(districts[1])
        three_district_json = construct_district_json(districts[2])
        districts_json_concat = "\"districts\":[{first_district_json} ,{second_district_json},{three_district_json}]".format(
                first_district_json = first_district_json, second_district_json = second_district_json,
                three_district_json = three_district_json
            )
        return districts_json_concat
    
    def __construct_departments_json(self, departments):
        first_department_json = self.__construct_department_json(departments[0])
        second_department_json = self.__construct_department_json(departments[1])
        departments_json_concat = "\"departments\":[{first_department}, {second_department}]".format(
            first_department = first_department_json, second_department = second_department_json
        )
        return departments_json_concat
    
    def __construct_department_json(self, department):
        json_department = "\"name\":\"{name}\",\"code\":{code}".format(
            name = department.name, code = department.code
        )
        json_final = "{"+json_department+"}"      
        return json_final    

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