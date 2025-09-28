import unittest
from infrastructure.services.OpenDatasService import OpenDataServices
from usecases.AdaptResultElectionData.CalculateElectionData import CalculateElectionData
from usecases.AdaptResultElectionData.RetrieveParty import RetrieveParty
from usecases.AdaptResultElectionData.RetrieveResultDepartment import RetrieveResultDepartment
from usecases.AdaptResultElectionData.RetrieveResultElectionDistrict import RetrieveResultElectionDistrict

class CalculateElectionDataTest(unittest.TestCase):
    def test_elections_datas_are_calculated(self):
        openDatasService = OpenDataServices()
        calculateElectionData = CalculateElectionData(openDatasService)
        isWellExecuted = calculateElectionData.Calculate()
        self.assertTrue(isWellExecuted)
