import unittest
from tests.utils.assertCustom import AssertDistrictResult
from infrastructure.adapter.AdaptDistrict import AdaptDistrict

class AdaptDistrictTest(unittest.TestCase):
    def test_departments_are_finded(self):
        adaptDistrict = AdaptDistrict()

        district = adaptDistrict.Transform("['33' 'Gironde' 3310 '10ème circonscription' 83620 58727 '70,23%' 24893 '29,77%' 55515 '66,39%' '94,53%' 2365 '2,83%' '4,03%' 847 '1,01%' '1,44%' 2 'ENS' 'BOUDIÉ' 'Florent' 'MASCULIN' 28960 '34,63%' '52,17%' 'élu' '4.0' 'RN' 'CHADOURNE' 'Sandrine' 'FEMININ' '26555.0' '31,76%' '47,83%' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']")

        AssertDistrictResult("33|Gironde|3310|10ème circonscription|83620|58727|70,23%|24893|29,77%|55515|66,39%|94,53%|2365|2.83|4.03|847|1.01|1.44|ENS|BOUDIÉ|Florent|MASCULIN|28960|34.63|52.17|RN|CHADOURNE|Sandrine|FEMININ|26555|31.76|47.83", district, self)
