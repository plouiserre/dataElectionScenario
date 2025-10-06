import unittest
from tests.utils.assertCustom import AssertDistrictWithTwoCandidates
from infrastructure.adapter.AdaptDistrict import AdaptDistrict
from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from domain.District import District
from domain.Candidate import Candidate

class AdaptDistrictTest(unittest.TestCase):
    def test_districts_are_finded(self):
        adaptCandidate = AdaptCandidate()
        adaptDistrict = AdaptDistrict(adaptCandidate)

        district = adaptDistrict.Transform("['33' 'Gironde' 3310 '10ème circonscription' 83620 58727 '70,23%' 24893 '29,77%' 55515 '66,39%' '94,53%' 2365 '2,83%' '4,03%' 847 '1,01%' '1,44%' 2 'ENS' 'BOUDIÉ' 'Florent' 'MASCULIN' 28960 '34,63%' '52,17%' 'élu' '4.0' 'RN' 'CHADOURNE' 'Sandrine' 'FEMININ' '26555' '31,76%' '47,83%' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")

        AssertDistrictWithTwoCandidates("33|Gironde|3310|10ème circonscription|83620|58727|70,23%|24893|29,77%|55515|66,39%|94,53%|2365|2.83|4.03|847|1.01|1.44|ENS|BOUDIÉ|Florent|MASCULIN|28960|34.63%|52.17%|RN|CHADOURNE|Sandrine|FEMININ|26555|31.76%|47.83%", district, self)


    def test_district_to_json(self):
        adaptCandidate = AdaptCandidate()
        adaptDistrict = AdaptDistrict(adaptCandidate)
        district = self.__district_build()

        json = adaptDistrict.to_json(district)

        json_expected = self.__construct_json_inside_district(district)

        self.assertEqual(json, json_expected)

    def __district_build(self):
        first_candidate_first_district = self.__construct_candidate('LARSONNEUR', 'Jean-Charles', 'DVC', 'MASCULIN', '19239', '24.61%',	'35.68%')
        second_candidate_first_district = self.__construct_candidate('CADALEN', 'Pierre-Yves', 'UG', 'MASCULIN', '22110', '41.01%', '28.28%')
        third_candidate_first_district = self.__construct_candidate('KERVELLA', 'Denis', 'RN', 'MASCULIN', '12567', '23.31%', '16.07%')
        district = District()
        district.label = '2ème circonscription'
        district.number ='2902'
        district.registered = '78185'
        district.voting = '55066'
        district.Candidates = []
        district.Candidates.append(first_candidate_first_district)
        district.Candidates.append(second_candidate_first_district)
        district.Candidates.append(third_candidate_first_district)
        return district
    
    def __construct_candidate(self, first_name, last_name, parti_code, sexe, voting, voting_registered, voting_expressed): 
        candidate = Candidate()
        candidate.firstName = first_name
        candidate.lastName = last_name
        candidate.partiCode = parti_code
        candidate.sexe = sexe
        candidate.vote = voting
        candidate.voteByRegistered = voting_registered
        candidate.voteByExpressed = voting_expressed
        return candidate    

    def __construct_json_inside_district(self, district):
        candidates = ''
        district_json = self.__construct_district_without_candidates(district)
        first_candidate_json = self.__construct_json_candidate(district.Candidates[0])
        second_candidate_json = self.__construct_json_candidate(district.Candidates[1])
        three_candidate_json = self.__construct_json_candidate(district.Candidates[2])
        candidates = "\"candidates\":[{first_candidate_json},{second_candidate_json},{three_candidate_json}]".format(
                first_candidate_json = first_candidate_json, second_candidate_json = second_candidate_json,
                three_candidate_json = three_candidate_json
            )
        district_concat = "{district}, {candidates}".format(district = district_json, candidates = candidates )
        final_district = district_concat+"}"
        return final_district
    
    def __construct_district_without_candidates(self, district):
        json_district = "\"label\":\"{label}\",\"number\":{number}, \"registered\":{registered},\"voting\":{voting} ".format(
            label = district.label, number = district.number, registered = district.registered, voting = district.voting)
        json_final = "{"+json_district
        return json_final

    def __construct_json_candidate(self, candidate):
         json_candidate = "\"lastName\":\"{lastName}\",\"firstName\":\"{firstName}\", \"sexe\":\"{sexe}\",\"partiCode\":\"{partiCode}\",\"vote\":{vote},\"voteByRegistered\":\"{voteByRegistered}\",\"voteByExpressed\":\"{voteByExpressed}\" ".format(
            lastName = candidate.lastName, firstName = candidate.firstName, sexe = candidate.sexe, partiCode = candidate.partiCode, 
            vote = candidate.vote, voteByRegistered = candidate.voteByRegistered, voteByExpressed = candidate.voteByExpressed
        )    
         json_final_candidate = "{"+json_candidate+"}"
         return json_final_candidate

