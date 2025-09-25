import unittest
from tests.utils.assertCustom import AssertDistrictCandidatesResult
from usecases.RetrieveResultElectionDistrict import RetrieveResultElectionDistrict

class RetrieveResultElectionDistrictTest(unittest.TestCase):
    def test_candidates_are_finded(self):
        retrieveResultElectionDistrict = RetrieveResultElectionDistrict()
                
        resultDistrict = retrieveResultElectionDistrict.Search()

        AssertDistrictCandidatesResult('33|Gironde|3310|10ème circonscription|83589|59039|70,63%|24550|29,37%|57167|68,39%|96,83%|1267|1.52|2.15|605|0.72|1.02|EXG|HALBIN|Hélène|FEMININ|1117|1.34|1.95|ENS|BOUDIÉ|Florent|MASCULIN|17128|20.49|29.96|UG|BOURGOIS|Pascal|MASCULIN|13885|16.61|24.29|RN|CHADOURNE|Sandrine|FEMININ|25037|29.95|43.8',resultDistrict, self )
        