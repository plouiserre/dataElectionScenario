import unittest
from unittest.mock import patch
from infrastructure.files.ExcelElection import ExcelElection
from infrastructure.services.OpenDatasService import OpenDataServices
from usecases.AdaptResultElectionData.CalculateElectionData import CalculateElectionData

class UsecasesCalculateElectionDataTest(unittest.TestCase):
    def get_datas_from_excel(self, *args)  : 
        return ''
    
    @patch.object(ExcelElection,'Load', side_effect=get_datas_from_excel)
    def test_elections_datas_are_calculated(self, mock_excel_election):
        openDatasService = OpenDataServices(mock_excel_election)
        calculateElectionData = CalculateElectionData(openDatasService)
        isWellExecuted = calculateElectionData.Calculate()
        self.assertTrue(isWellExecuted)
