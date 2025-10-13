import unittest
from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from infrastructure.adapter.AdaptDistrict import AdaptDistrict
from infrastructure.adapter.AdaptElection import AdaptElection
from tests.utils.assertCustom import AssertDistrictWithTwoCandidates
from tests.utils.build_election import build_one_election, construct_election_json


class AdapterElectionTest(unittest.TestCase):
    def __get_election_datas(self)  : 
        firstLine = "['33' 'Gironde' 3310 '10ème circonscription' 83620 58727 '70,23%' 24893 '29,77%' 55515 '66,39%' '94,53%' 2365 '2,83%' '4,03%' 847 '1,01%' '1,44%' 2 'ENS' 'BOUDIÉ' 'Florent' 'MASCULIN' 28960 '34,63%' '52,17%' 'élu' '4.0' 'RN' 'CHADOURNE' 'Sandrine' 'FEMININ' '26555' '31,76%' '47,83%' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        secondLine = "['56' 'Morbihan' 5603 '3ème circonscription' 98156 69854 '71,17%' 28302 '28,83%' 65630 '66,86%' '93,95%' 2956 '3,01%' '4,23%' 1268 '1,29%' '1,82%' 5 'ENS' 'LE PEIH' 'Nicole' 'FEMININ' 37776 '38,49%' '57,56%' 'élu' '6.0' 'RN' 'OLIVIERO' 'Antoine' 'MASCULIN' '27854' '28,38%' '42,44%' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        lines = []
        lines.append(firstLine)
        lines.append(secondLine)
        return lines
    
    def test_adapt_election(self):
        datas = self.__get_election_datas()
        adapt_candidate = AdaptCandidate()
        adapt_district = AdaptDistrict(adapt_candidate)
        adapt_election = AdaptElection(adapt_district)

        election_data =adapt_election.Transform(datas, 2022)

        self.assertEqual(2022, election_data.year)
        AssertDistrictWithTwoCandidates("33|Gironde|3310|10ème circonscription|83620|58727|70,23%|24893|29,77%|55515|66,39%|94,53%|2365|2.83|4.03|847|1.01|1.44|ENS|BOUDIÉ|Florent|MASCULIN|28960|34.63%|52.17%|RN|CHADOURNE|Sandrine|FEMININ|26555|31.76%|47.83%", election_data.Districts[0], self)
        AssertDistrictWithTwoCandidates("56|Morbihan|5603|3ème circonscription|98156|69854|71,17%|28302|28,83%|65630|66,86%|93,95%|2956|3,01|4,23|1268|1,29|1,82|ENS|LE PEIH|Nicole|FEMININ|37776|38.49%|57.56%|RN|OLIVIERO|Antoine|MASCULIN|27854|28.38%|42.44%", election_data.Districts[1], self)


    def test_adapt_election_to_json(self):
        election = build_one_election()
        adapt_candidate = AdaptCandidate()
        adapt_district = AdaptDistrict(adapt_candidate)
        adapt_election = AdaptElection(adapt_district)

        json =adapt_election.to_json(election)

        json_expected = construct_election_json(election)

        self.assertEqual(json, json_expected)