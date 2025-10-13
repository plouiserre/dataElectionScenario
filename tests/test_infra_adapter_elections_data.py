import unittest
from tests.utils.build_department import build_departments, construct_departments_json
from tests.utils.build_district import  builds_three_districts, construct_districts_json
from tests.utils.build_party import build_parties, construct_parties_json
from infrastructure.adapter.AdaptElectionsData import AdaptElectionsData
from domain.ResultDatas import ResultDatas

class AdaptElectionDataTest(unittest.TestCase):
    def test_districts_are_finded(self):
        adaptElectionData = AdaptElectionsData()
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
        result.Parties = build_parties()
        return result

    def __construct_json_result_data(self, result_data):
        all_districts_json = construct_districts_json(result_data.Districts)
        all_departments_json = construct_departments_json(result_data.Departments)
        all_parties_json = construct_parties_json(result_data.Parties)
        result_data_json_inside = "{all_districts}, {all_departments}, {all_parties}".format(
            all_districts = all_districts_json, all_departments = all_departments_json, 
            all_parties = all_parties_json
        )
        result_data_json = "{\"result_data\" : {" + result_data_json_inside+ "}}"
        return result_data_json    