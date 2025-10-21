import unittest
from unittest.mock import Mock
from infrastructure.adapter.AdaptResultsElections import AdaptResultsElections
from infrastructure.adapter.AdaptElection import AdaptElection
from infrastructure.adapter.AdaptDistrict import AdaptDistrict
from infrastructure.adapter.AdaptDepartment import AdaptDepartment
from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from infrastructure.memory.party_memory import PartyMemory
from infrastructure.services.OpenDatasService import OpenDataServices
from usecases.AdaptResultElectionData.CalculateElectionData import CalculateElectionData

class UsecasesCalculateElectionDataTest(unittest.TestCase):
    def get_datas_from_excel(self)  : 
        firstLine = "['33' 'Gironde' 3310 '10ème circonscription' 83620 58727 '70,23%' 24893 '29,77%' 55515 '66,39%' '94,53%' 2365 '2,83%' '4,03%' 847 '1,01%' '1,44%' 2 'ENS' 'BOUDIÉ' 'Florent' 'MASCULIN' 28960 '34,63%' '52,17%' 'élu' '4.0' 'RN' 'CHADOURNE' 'Sandrine' 'FEMININ' '26555.0' '31,76%' '47,83%' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        seconeLine = "['56' 'Morbihan' 5603 '3ème circonscription' 98156 69854 '71,17%' 28302 '28,83%' 65630 '66,86%' '93,95%' 2956 '3,01%' '4,23%' 1268 '1,29%' '1,82%' 5 'ENS' 'LE PEIH' 'Nicole' 'FEMININ' 37776 '38,49%' '57,56%' 'élu' '6.0' 'RN' 'OLIVIERO' 'Antoine' 'MASCULIN' '27854.0' '28,38%' '42,44%' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        thirdLine = "['73' 'Savoie' 7303 '3ème circonscription' 74595 53589 '71,84%' 21006 '28,16%' 51391 '68,89%' '95,90%' 1696 '2,27%' '3,16%' 502 '0,67%' '0,94%' 2 'RN' 'DAUCHY' 'Marie' 'FEMININ' 19961 '26,76%' '38,84%' 'nan' '3.0' 'LR' 'BONNIVARD' 'Emilie' 'FEMININ' '31430.0' '42,13%' '61,16%' 'élu' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        fourthLine = "['92' 'Hauts-de-Seine' 9205 '5ème circonscription' 77514 51903 '66,96%' 25611 '33,04%' 49318 '63,62%' '95,02%' 1850 '2,39%' '3,56%' 735 '0,95%' '1,42%' 1 'UG' 'PITTI' 'Raphaël' 'MASCULIN' 21676 '27,96%' '43,95%' 'nan' '4.0' 'ENS' 'CALVEZ' 'Céline' 'FEMININ' '27642.0' '35,66%' '56,05%' 'élu' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        lines = []
        lines.append(firstLine)
        lines.append(seconeLine)
        lines.append(thirdLine)
        lines.append(fourthLine)
        all_datas = {}
        all_datas[2024] = lines
        return all_datas
    
    def test_elections_datas_are_calculated(self):
        lines = self.get_datas_from_excel()
        excelElection = Mock()
        excelElection.load.return_value = lines
        json_file = Mock()
        json_file.Save.return_value = True
        adaptDepartment = AdaptDepartment()
        adaptCandidate = AdaptCandidate()
        adaptDistrict = AdaptDistrict(adaptCandidate)   
        adaptElection = AdaptElection(adaptDistrict)
        adapt_results_elections = AdaptResultsElections()     
        party_memory = PartyMemory()
        openDatasService = OpenDataServices(excelElection, json_file, adaptDepartment, adapt_results_elections, adaptElection, party_memory)
        calculateElectionData = CalculateElectionData(openDatasService)
        isWellExecuted = calculateElectionData.calculate()
        self.assertTrue(isWellExecuted)                                                                                                                                                 
