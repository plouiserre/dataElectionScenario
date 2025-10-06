import unittest
from tests.utils.assertCustom import AssertDistrictWithTwoCandidates
from infrastructure.adapter.AdaptElectionData import AdaptElectionData
from domain.ResultDatas import ResultDatas
from domain.Candidate import Candidate
from domain.Department import Department
from domain.District import District
from domain.Party import Party

class AdaptElectionDataTest(unittest.TestCase):
    def test_districts_are_finded(self):
        adaptElectionData = AdaptElectionData()

        # result_datas = self.__construct_result_data()
        
        # data = adaptElectionData.to_json(result_datas)

        result_data_expected = self.__construct_json_result()
        mpl= "af"


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
        first_candidate_first_district = self.__construct_candidate('LARSONNEUR', 'Jean-Charles', 'DVC', 'MASCULIN', '19239', '24.61%',	'35.68%')
        second_candidate_first_district = self.__construct_candidate('CADALEN', 'Pierre-Yves', 'UG', 'MASCULIN', '22110', '41.01%', '28.28%')
        third_candidate_first_district = self.__construct_candidate('KERVELLA', 'Denis', 'RN', 'MASCULIN', '12567', '23.31%', '16.07%')
        first_district = self.__construct_district('2ème circonscription', '2902', '78185', '55066', first_candidate_first_district, 
                                                   second_candidate_first_district, third_candidate_first_district)
        first_candidate_second_district = self.__construct_candidate('RAMOS', 'Richard', 'ENS', 'MASCULIN', '31737', '63.31%', '41.70%')
        second_candidate_second_district = self.__construct_candidate('ZELLER', 'Anthony', 'RN', 'MASCULIN', '18392', '36.69%', '24.17%')
        second_district = self.__construct_district('6ème circonscription', '4506', '76104', '52335', first_candidate_second_district, 
                                                    second_candidate_second_district, None)
        first_candidate_third_district = self.__construct_candidate('MOREL', 'Louise', 'ENS', 'FEMININ', '35890', '55.02%', '36.52%')
        second_candidate_third_district = self.__construct_candidate('COUSSEDIERE', 'Vincent', 'RN', 'MASCULIN','29338', '44.98%', '29.85%')
        third_district = self.__construct_district('6ème circonscription', '6706', '98281', '67852', first_candidate_third_district,
                                                   second_candidate_third_district, None)
        districts = []
        districts.append(first_district)
        districts.append(second_district)
        districts.append(third_district)
        return districts

    def __construct_candidate(self, first_name, last_name, parti_code, sexe, vote, vote_by_expressed, vote_by_registered):
        candidate = Candidate()
        candidate.firstName = first_name
        candidate.lastName = last_name
        candidate.partiCode = parti_code 
        candidate.sexe = sexe
        candidate.vote = vote
        candidate.voteByExpressed = vote_by_expressed
        candidate.voteByRegistered = vote_by_registered
        return candidate

    def __construct_district(self, label, number, registered, voting, first_candidate, second_candidate, third_candidate): 
        district = District()
        district.label = label
        district.number = number
        district.registered = registered
        district.voting = voting
        district.Candidates.append(first_candidate)
        district.Candidates.append(second_candidate)
        if third_candidate != None : 
            district.Candidates.append(third_candidate)
        return district

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
        first_district_json = self.__construct_district_json(districts[0])
        second_district_json = self.__construct_district_json(districts[1])
        three_district_json = self.__construct_district_json(districts[2])
        districts_json_concat = "\"districts\":[{first_district_json} ,{second_district_json},{three_district_json}]".format(
                first_district_json = first_district_json, second_district_json = second_district_json,
                three_district_json = three_district_json
            )
        return districts_json_concat
        
    def __construct_district_json(self, district):
        candidates = ''
        district_json = self.__construct_district_without_candidates(district)
        first_candidate_json = self.__construct_candidate_json(district.Candidates[0])
        second_candidate_json = self.__construct_candidate_json(district.Candidates[1])
        if len(district.Candidates) == 3 :
            three_candidate_json = self.__construct_candidate_json(district.Candidates[2])
            candidates = "\"candidates\":[{first_candidate_json} ,{second_candidate_json},{three_candidate_json}]".format(
                first_candidate_json = first_candidate_json, second_candidate_json = second_candidate_json,
                three_candidate_json = three_candidate_json
            )
        else :
            candidates = "\"candidates\":[{first_candidate_json} ,{second_candidate_json}]".format(
                first_candidate_json = first_candidate_json, second_candidate_json = second_candidate_json)
        district_concat = "{district}, {candidates}".format(district = district_json, candidates = candidates )
        final_district = district_concat+"}"
        return final_district
    
    def __construct_district_without_candidates(self, district):
        json_district = "\"label\":\"{label}\",\"number\":{number}, \"registered\":{registered},\"voting\":{voting} ".format(
            label = district.label, number = district.number, registered = district.registered, voting = district.voting)
        json_final = "{"+json_district
        return json_final
        
    def __construct_candidate_json(self, candidate ):
        json_candidate = "\"lastName\":\"{lastname}\",\"firstName\":\"{firstName}\", \"sexe\":\"{sexe}\",\"partiCode\":\"{partiCode}\",\"vote\":{vote},\"voteByRegistered\":\"{voteByRegistered}\",\"voteByExpressed\":\"{voteByExpressed}\" ".format(
            lastname = candidate.lastName, firstName = candidate.firstName, sexe = candidate.sexe, partiCode = candidate.partiCode, 
            vote = candidate.vote, voteByRegistered = candidate.voteByRegistered, voteByExpressed = candidate.voteByExpressed)
        json_final = "{"+json_candidate+"}"
        return json_final
    
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