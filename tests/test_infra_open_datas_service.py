import unittest
from unittest.mock import Mock
from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from infrastructure.adapter.AdaptDepartment import AdaptDepartment
from infrastructure.adapter.AdaptDistrict import AdaptDistrict
from infrastructure.adapter.AdaptResultsElections import AdaptResultsElections
from infrastructure.adapter.AdaptElection import AdaptElection
from infrastructure.files.JsonFile import JsonFile
from infrastructure.memory.party_memory import PartyMemory
from infrastructure.services.OpenDatasService import OpenDataServices
from tests.utils.assertCustom import assertDistrictWithTwoCandidates, assertDepartment, assertParty

class OpenDataServicesTest(unittest.TestCase):
    def __get_datas_from_excel(self)  : 
        firstLine = "['33' 'Gironde' 10 '10ème circonscription' 'Complet' 83277 40667 '48.83' 42610 '51.17' 781 '0.94' '1.83' 347 '0.42' '0.81' 41482 '49.81' '97.35' 9 'F' 'HALBIN' 'Hélène' 'DXG' 507 '0.61' '1.22' 'nan' 5 'F' 'PLANTON' 'Veronique, Raymonde' 'RDG' 2034 '2.44' '4.9' 'nan' 3 'M' 'BOURGOIS' 'Pascal' 'NUP' 9705 '11.65' '23.4' 'nan' 6 'F' 'BERNARD' 'Muriel' 'DVG' 0 '0.0' '0.0' 'nan' '8.0' 'F' 'GUILBERT' 'Amélie' 'ECO' '606.0' '0.73' '1.46' 'nan' '10.0' 'F' 'DEJONG-PAUSS' 'Angélique' 'DIV' '262.0' '0.31' '0.63' 'nan' '2.0' 'M' 'BOUDIÉ' 'Florent' 'ENS' '13565.0' '16.29' '32.7' 'nan' '4.0' 'F' 'FLEURY' 'Catherine' 'DSV' '593.0' '0.71' '1.43' 'nan' '7.0' 'M' 'MALHERBE' 'Gonzague' 'REC' '2582.0' '3.1' '6.22' 'nan' '1.0' 'F' 'CHADOURNE' 'Sandrine' 'RN' '11628.0' '13.96' '28.03' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        secondLine = "['56' 'Morbihan' 5603 '3ème circonscription' 98156 69854 '71,17%' 28302 '28,83%' 65630 '66,86%' '93,95%' 2956 '3,01%' '4,23%' 1268 '1,29%' '1,82%' 5 'ENS' 'LE PEIH' 'Nicole' 'FEMININ' 37776 '38,49%' '57,56%' 'élu' '6.0' 'RN' 'OLIVIERO' 'Antoine' 'MASCULIN' '27854' '28,38%' '42,44%' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        thirdLine = "['73' 'Savoie' 3 '3ème circonscription' 'Complet' 74446 35242 '47.34' 39204 '52.66' 405 '0.54' '1.03' 168 '0.23' '0.43' 38631 '51.89' '98.54' 8 'F' 'TROUVÉ' 'Pascale' 'DXG' 347 '0.47' '0.9' 'nan' 7 'F' 'KRAWEZYNSKI' 'Nathalie' 'NUP' 8793 '11.81' '22.76' 'nan' 5 'F' 'NOWAK' 'Patricia' 'ECO' 1029 '1.38' '2.66' 'nan' 6 'F' 'SOCQUET-JUGLARD' 'Ghislaine' 'ECO' 572 '0.77' '1.48' 'nan' '3.0' 'M' 'TROSSET' 'Xavier' 'ENS' '6095.0' '8.19' '15.78' 'nan' '2.0' 'F' 'BONNIVARD' 'Emilie' 'LR' '12788.0' '17.18' '33.1' 'nan' '4.0' 'M' 'THOMAZO' 'Vincent' 'DSV' '623.0' '0.84' '1.61' 'nan' '1.0' 'M' 'FLORIO' 'Mikaël' 'REC' '823.0' '1.11' '2.13' 'nan' '9.0' 'F' 'DAUCHY' 'Marie' 'RN' '7561.0' '10.16' '19.57' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        fourthLine = "['92' 'Hauts-de-Seine' 9205 '5ème circonscription' 77514 51903 '66,96%' 25611 '33,04%' 49318 '63,62%' '95,02%' 1850 '2,39%' '3,56%' 735 '0,95%' '1,42%' 1 'UG' 'PITTI' 'Raphaël' 'MASCULIN' 21676 '27,96%' '43,95%' 'nan' '4.0' 'ENS' 'CALVEZ' 'Céline' 'FEMININ' '27642' '35,66%' '56,05%' 'élu' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"
        first_election = []
        second_election = []
        first_election.append(firstLine)
        first_election.append(thirdLine)
        second_election.append(secondLine)
        second_election.append(fourthLine)
        all_datas = {}
        all_datas[2022] = first_election
        all_datas[2024] = second_election
        return all_datas
    
    def test_datas_are_retrieve(self): 
        lines = self.__get_datas_from_excel()
        excel_elections = Mock()
        excel_elections.load.return_value = lines
        json_file = JsonFile()
        adapt_department = AdaptDepartment()
        adapt_candidate = AdaptCandidate()
        adapt_district = AdaptDistrict(adapt_candidate)        
        adapt_election = AdaptElection(adapt_district)
        adapt_results_elections = AdaptResultsElections()
        party_memory = PartyMemory()
        open_data_services = OpenDataServices(excel_elections, json_file, adapt_department, adapt_results_elections, adapt_election, 
                                              party_memory)

        results = open_data_services.retrieveDatas()

        self.assertEqual(2, len(results.elections[0].districts))
        self.assertEqual(2022, results.elections[0].year)
        self.assertEqual(2, len(results.elections[1].districts))
        self.assertEqual(2024, results.elections[1].year)
        assertDistrictWithTwoCandidates("33|Gironde|10|10ème circonscription|83277|40667|48,83%|42610|51,17%|781|0.94%|1,83%|347|0.42|0.81|347|0.42|0.81|DXG|HALBIN|Hélène|FEMININ|507|0.61%|1.22%|RDG|PLANTON|Veronique, Raymonde|FEMININ|2034|2.44%|4.9%|NUP|BOURGOIS|Pascal|MASCULIN|9705|11.65%|23.4%|DVG|BERNARD|Muriel|FEMININ|0|0.0%|0.0%|ECO|GUILBERT|Amélie|FEMININ|606|0.73%|1.46%|DIV|DEJONG-PAUSS|Angélique|FEMININ|262|0.31%|0.63%|ENS|BOUDIÉ|Florent|MASCULIN|13565|16.29%|32.7%|DSV|FLEURY|Catherine|FEMININ|593|0.71%|1.43%|REC|MALHERBE|Gonzague|MASCULIN|2582|3.1%|6.22%|RN|CHADOURNE|Sandrine|FEMININ|11628|13.96%|28.03%", results.elections[0].districts[0], self)                                                                                                                                                                                                                                                                                                                             
        assertDistrictWithTwoCandidates("73|Savoie|3|3ème circonscription|74446|35242|47,34%|39204|52,66%|405|0,54%|1,03%|168|0,23|0,43|405|0,54|1,03|DXG|TROUVÉ|Pascale|FEMININ|347|0.47%|0.9%|NUP|KRAWEZYNSKI|Nathalie|FEMININ|8793|11.81%|22.76%|ECO|NOWAK|Patricia|FEMININ|1029|1.38%|2.66%|ECO|SOCQUET-JUGLARD|Ghislaine|FEMININ|572|0.77%|1.48%|ENS|TROSSET|Xavier|MASCULIN|6095|8.19%|15.78%|LR|BONNIVARD|Emilie|FEMININ|12788|17.18%|33.1%|DSV|THOMAZO|Vincent|MASCULIN|623|0.84%|1.61%|REC|FLORIO|Mikaël|MASCULIN|823|1.11%|2.13%|RN|FEMININ|Marie|MASCULIN|7561|10.16%|19.57%", results.elections[0].districts[1], self)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        assertDistrictWithTwoCandidates("56|Morbihan|5603|3ème circonscription|98156|69854|71,17%|28302|28,83%|65630|66,86%|93,95%|2956|3,01|4,23|1268|1,29|1,82|ENS|LE PEIH|Nicole|FEMININ|37776|38.49%|57.56%|RN|OLIVIERO|Antoine|MASCULIN|27854|28.38%|42.44%", results.elections[1].districts[0], self)
        assertDistrictWithTwoCandidates("92|Hauts-de-Seine|9205|5ème circonscription|77514|51903|66,96%|25611|33,04%|49318|63,62%|95,02%|1850|2,39|3,56|735|0,95|1,4|UG|PITTI|Raphaël|MASCULIN|21676|27.96%|43.95%|ENS|CALVEZ|Céline|FEMININ|27642|35.66%|56.05%", results.elections[1].districts[1], self)

        assertDepartment("33|Gironde", results.departments[0], self)
        assertDepartment("73|Savoie", results.departments[1], self)        

        self.__assertParty2024(results.parties[2024])

        self.__assertParty2022(results.parties[2022])


    def __assertParty2024(self, parties):
        assertParty('EXG|Extrême gauche', parties[0], self)
        assertParty('COM|Parti communiste français', parties[1], self)
        assertParty('FI|La France insoumise', parties[2], self)
        assertParty('SOC|Parti socialiste', parties[3], self)
        assertParty('RDG|Parti radical de gauche', parties[4], self)
        assertParty('VEC|Les Ecologistes', parties[5], self)
        assertParty('DVG|Divers gauche', parties[6], self)
        assertParty('UG|Union de la gauche', parties[7], self)
        assertParty('ECO|Ecologistes', parties[8], self)
        assertParty('REG|Régionaliste', parties[9], self)
        assertParty('DIV|Divers', parties[10], self)
        assertParty('REN|Renaissance', parties[11], self)
        assertParty('MDM|Modem', parties[12], self)
        assertParty('HOR|Horizons', parties[13], self)
        assertParty('ENS|Ensemble ! (Majorité présidentielle)', parties[14], self)
        assertParty('DVC|Divers centre', parties[15], self)
        assertParty('UDI|Union des Démocrates et Indépendants', parties[16], self)
        assertParty('LR|Les Républicains', parties[17], self)
        assertParty('DVD|Divers droite', parties[18], self)
        assertParty('DSV|Droite souverainiste', parties[19], self)
        assertParty('RN|Rassemblement National', parties[20], self)
        assertParty('REC|Reconquête !', parties[21], self)
        assertParty('UXD|Union de l\'extrême droite', parties[22], self)
        assertParty('EXD|Extrême droite', parties[23], self)

    def __assertParty2022(self, parties):
        assertParty('DXG|Divers extrême gauche', parties[0], self)
        assertParty('RDG|Parti radical de gauche', parties[1], self)
        assertParty('NUP|Nouvelle union populaire écologique et sociale', parties[2], self)
        assertParty('DVG|Divers gauche', parties[3], self)
        assertParty('ECO|Ecologistes', parties[4], self)
        assertParty('DIV|Divers', parties[5], self)
        assertParty('REG|Régionaliste', parties[6], self)
        assertParty('ENS|Ensemble ! (Majorité présidentielle)', parties[7], self)
        assertParty('DVC|Divers centre', parties[8], self)
        assertParty('UDI|Union des Démocrates et des Indépendants', parties[9], self)
        assertParty('LR|Les Républicains', parties[10], self)
        assertParty('DVD|Divers droite', parties[11], self)
        assertParty('DSV|Droite souverainiste', parties[12], self)
        assertParty('REC|Reconquête !', parties[13], self)
        assertParty('RN|Rassemblement National', parties[14], self)
        assertParty('DXD|Divers extrême droite', parties[15], self)