import unittest
from tests.utils.assertCustom import assertDistrictWithTwoCandidates
from tests.utils.build_district import build_first_district, construct_district_json
from infrastructure.adapter.AdaptDistrict import AdaptDistrict
from infrastructure.adapter.AdaptCandidate import AdaptCandidate

class AdaptDistrictTest(unittest.TestCase):
    def test_districts_are_finded(self):
        adaptCandidate = AdaptCandidate()
        adaptDistrict = AdaptDistrict(adaptCandidate)

        district = adaptDistrict.transform("['33' 'Gironde' 3310 '10ème circonscription' 83620 58727 '70,23%' 24893 '29,77%' 55515 '66,39%' '94,53%' 2365 '2,83%' '4,03%' 847 '1,01%' '1,44%' 2 'ENS' 'BOUDIÉ' 'Florent' 'MASCULIN' 28960 '34,63%' '52,17%' 'élu' '4.0' 'RN' 'CHADOURNE' 'Sandrine' 'FEMININ' '26555' '31,76%' '47,83%' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']", 2024)

        assertDistrictWithTwoCandidates("33|Gironde|3310|10ème circonscription|83620|58727|70,23%|24893|29,77%|55515|66,39%|94,53%|2365|2.83|4.03|847|1.01|1.44|ENS|BOUDIÉ|Florent|MASCULIN|28960|34.63%|52.17%|RN|CHADOURNE|Sandrine|FEMININ|26555|31.76%|47.83%", district, self)


    def test_district_to_json(self):
        adaptCandidate = AdaptCandidate()
        adaptDistrict = AdaptDistrict(adaptCandidate)
        district = build_first_district()

        json = adaptDistrict.to_json(district)

        json_expected = construct_district_json(district)

        self.assertEqual(json, json_expected)

