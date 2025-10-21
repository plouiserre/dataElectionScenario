import unittest
from tests.utils.build_department import build_departments, construct_departments_json
from tests.utils.build_district import  build_first_district, build_second_district, build_third_district, construct_districts_json
from tests.utils.build_election import construct_elections_json
from tests.utils.build_party import build_parties, construct_parties_json
from infrastructure.adapter.AdaptResultsElections import AdaptResultsElections
from domain.ResultDatas import ResultDatas
from domain.Election import Election

class AdaptResultsElectionsTest(unittest.TestCase):
    def test_districts_are_finded(self):
        adapt_results_elections = AdaptResultsElections()
        elections_results = self.__construct_elections_results()

        json_result = adapt_results_elections.to_json(elections_results)

        json_expected = self.__construct_json_result()
        self.assertEqual(json_expected, json_result)

    def __construct_json_result(self): 
        elections_results = self.__construct_elections_results()
        elections_results_json = self.__construct_json_elections_result(elections_results)
        return elections_results_json        

    def __construct_elections_results(self):
        result = ResultDatas()
        result.elections = []
        first_election = Election()
        first_election.districts.append(build_first_district())
        first_election.districts.append(build_third_district())
        first_election.year = 2022
        result.elections.append(first_election)
        second_election = Election()
        second_election.districts.append(build_second_district())
        second_election.year = 2024
        result.elections.append(second_election)
        result.departments = build_departments()
        result.parties = build_parties()
        return result

    def __construct_json_elections_result(self, elections_results):
        all_elections_json = construct_elections_json(elections_results.elections)
        all_departments_json = construct_departments_json(elections_results.departments)
        all_parties_json = construct_parties_json(elections_results.parties)
        result_data_json_inside = "{all_elections}, {all_departments}, {all_parties}".format(
            all_elections = all_elections_json, all_departments = all_departments_json, 
            all_parties = all_parties_json
        )
        elections_results_json = "{\"elections_results\" : {" + result_data_json_inside+ "}}"
        return elections_results_json    