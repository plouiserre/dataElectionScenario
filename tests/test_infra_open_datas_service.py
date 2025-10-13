import unittest
from unittest.mock import Mock
from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from infrastructure.adapter.AdaptDepartment import AdaptDepartment
from infrastructure.adapter.AdaptDistrict import AdaptDistrict
from infrastructure.adapter.AdaptElectionsData import AdaptElectionsData
from infrastructure.adapter.AdaptElection import AdaptElection
from infrastructure.files.JsonFile import JsonFile
from infrastructure.memory.party_memory import PartyMemory
from infrastructure.services.OpenDatasService import OpenDataServices
from tests.utils.assertCustom import AssertDistrictWithTwoCandidates, AssertDepartment, AssertParty

class OpenDataServicesTest(unittest.TestCase):
    def __get_datas_from_excel(self)  : 
        firstLine = "['33' 'Gironde' 3310 '10ème circonscription' 83620 58727 '70,23%' 24893 '29,77%' 55515 '66,39%' '94,53%' 2365 '2,83%' '4,03%' 847 '1,01%' '1,44%' 2 'ENS' 'BOUDIÉ' 'Florent' 'MASCULIN' 28960 '34,63%' '52,17%' 'élu' '4.0' 'RN' 'CHADOURNE' 'Sandrine' 'FEMININ' '26555' '31,76%' '47,83%' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        secondLine = "['56' 'Morbihan' 5603 '3ème circonscription' 98156 69854 '71,17%' 28302 '28,83%' 65630 '66,86%' '93,95%' 2956 '3,01%' '4,23%' 1268 '1,29%' '1,82%' 5 'ENS' 'LE PEIH' 'Nicole' 'FEMININ' 37776 '38,49%' '57,56%' 'élu' '6.0' 'RN' 'OLIVIERO' 'Antoine' 'MASCULIN' '27854' '28,38%' '42,44%' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        thirdLine = "['73' 'Savoie' 7303 '3ème circonscription' 74595 53589 '71,84%' 21006 '28,16%' 51391 '68,89%' '95,90%' 1696 '2,27%' '3,16%' 502 '0,67%' '0,94%' 2 'RN' 'DAUCHY' 'Marie' 'FEMININ' 19961 '26,76%' '38,84%' 'nan' '3.0' 'LR' 'BONNIVARD' 'Emilie' 'FEMININ' '31430' '42,13%' '61,16%' 'élu' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        fourthLine = "['92' 'Hauts-de-Seine' 9205 '5ème circonscription' 77514 51903 '66,96%' 25611 '33,04%' 49318 '63,62%' '95,02%' 1850 '2,39%' '3,56%' 735 '0,95%' '1,42%' 1 'UG' 'PITTI' 'Raphaël' 'MASCULIN' 21676 '27,96%' '43,95%' 'nan' '4.0' 'ENS' 'CALVEZ' 'Céline' 'FEMININ' '27642' '35,66%' '56,05%' 'élu' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        first_lines = []
        second_lines = []
        first_lines.append(firstLine)
        first_lines.append(thirdLine)
        second_lines.append(secondLine)
        second_lines.append(fourthLine)
        all_datas = {}
        all_datas[2022] = first_lines
        all_datas[2024] = second_lines
        return all_datas
    
    def test_datas_are_retrieve(self): 
        lines = self.__get_datas_from_excel()
        excel_elections = Mock()
        excel_elections.Load.return_value = lines
        json_file = JsonFile()
        adapt_department = AdaptDepartment()
        adapt_candidate = AdaptCandidate()
        adapt_district = AdaptDistrict(adapt_candidate)        
        adapt_election = AdaptElection(adapt_district)
        adapt_elections_data = AdaptElectionsData()
        party_memory = PartyMemory()
        open_data_services = OpenDataServices(excel_elections, json_file, adapt_department, adapt_elections_data, adapt_election, 
                                              party_memory)

        results = open_data_services.RetrieveDatas()

        self.assertEqual(2, len(results.Elections[0].Districts))
        self.assertEqual(2022, results.Elections[0].year)
        self.assertEqual(2, len(results.Elections[1].Districts))
        self.assertEqual(2024, results.Elections[1].year)
        AssertDistrictWithTwoCandidates("33|Gironde|3310|10ème circonscription|83620|58727|70,23%|24893|29,77%|55515|66,39%|94,53%|2365|2.83|4.03|847|1.01|1.44|ENS|BOUDIÉ|Florent|MASCULIN|28960|34.63%|52.17%|RN|CHADOURNE|Sandrine|FEMININ|26555|31.76%|47.83%", results.Elections[0].Districts[0], self)
        AssertDistrictWithTwoCandidates("73|Savoie|7303|3ème circonscription|74595|53589|71,84%|21006|28,16%|51391|68,89%|95,90%|1696|2,27|3,16|502|0,67|0,94|RN|DAUCHY|Marie|FEMININ|19961|26.76%|38.84%|LR|BONNIVARD|Emilie|FEMININ|31430|42.13%|61.16%", results.Elections[0].Districts[1], self)
        AssertDistrictWithTwoCandidates("56|Morbihan|5603|3ème circonscription|98156|69854|71,17%|28302|28,83%|65630|66,86%|93,95%|2956|3,01|4,23|1268|1,29|1,82|ENS|LE PEIH|Nicole|FEMININ|37776|38.49%|57.56%|RN|OLIVIERO|Antoine|MASCULIN|27854|28.38%|42.44%", results.Elections[1].Districts[0], self)
        AssertDistrictWithTwoCandidates("92|Hauts-de-Seine|9205|5ème circonscription|77514|51903|66,96%|25611|33,04%|49318|63,62%|95,02%|1850|2,39|3,56|735|0,95|1,4|UG|PITTI|Raphaël|MASCULIN|21676|27.96%|43.95%|ENS|CALVEZ|Céline|FEMININ|27642|35.66%|56.05%", results.Elections[1].Districts[1], self)

        AssertDepartment("33|Gironde", results.Departments[0], self)
        AssertDepartment("73|Savoie", results.Departments[1], self)        

        AssertParty('EXG|Extrême gauche', results.Parties[0], self)
        AssertParty('COM|Parti communiste français', results.Parties[1], self)
        AssertParty('FI|La France insoumise', results.Parties[2], self)
        AssertParty('SOC|Parti socialiste', results.Parties[3], self)
        AssertParty('RDG|Parti radical de gauche', results.Parties[4], self)
        AssertParty('VEC|Les Ecologistes', results.Parties[5], self)
        AssertParty('DVG|Divers gauche', results.Parties[6], self)
        AssertParty('UG|Union de la gauche', results.Parties[7], self)
        AssertParty('ECO|Ecologistes', results.Parties[8], self)
        AssertParty('REG|Régionaliste', results.Parties[9], self)
        AssertParty('DIV|Divers', results.Parties[10], self)
        AssertParty('REN|Renaissance', results.Parties[11], self)
        AssertParty('MDM|Modem', results.Parties[12], self)
        AssertParty('HOR|Horizons', results.Parties[13], self)
        AssertParty('ENS|Ensemble ! (Majorité présidentielle)', results.Parties[14], self)
        AssertParty('DVC|Divers centre', results.Parties[15], self)
        AssertParty('UDI|Union des Démocrates et Indépendants', results.Parties[16], self)
        AssertParty('LR|Les Républicains', results.Parties[17], self)
        AssertParty('DVD|Divers droite', results.Parties[18], self)
        AssertParty('DSV|Droite souverainiste', results.Parties[19], self)
        AssertParty('RN|Rassemblement National', results.Parties[20], self)
        AssertParty('REC|Reconquête !', results.Parties[21], self)
        AssertParty('UXD|Union de l\'extrême droite', results.Parties[22], self)
        AssertParty('EXD|Extrême droite', results.Parties[23], self)