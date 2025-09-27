import unittest
from usecases.AdaptResultElectionData.CalculateElectionData import CalculateElectionData
from usecases.AdaptResultElectionData.RetrieveParty import RetrieveParty
from usecases.AdaptResultElectionData.RetrieveResultDepartment import RetrieveResultDepartment
from usecases.AdaptResultElectionData.RetrieveResultElectionDistrict import RetrieveResultElectionDistrict

class CalculateElectionDataTest(unittest.TestCase):
    def test_elections_datas_are_calculated(self):
        retrieveParties = RetrieveParty()
        retrieveDepartment = RetrieveResultDepartment()
        retrieveElectionDistrict = RetrieveResultElectionDistrict()
        calculateElectionData = CalculateElectionData(retrieveParties, retrieveDepartment, retrieveElectionDistrict)
        isWellExecuted = calculateElectionData.Calculate()
        self.assertTrue(isWellExecuted)
