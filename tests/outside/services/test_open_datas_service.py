import unittest
from ports.outside.services.OpenDatasService import OpenDataServices
from tests.utils.assertCustom import AssertDepartment, AssertParties, AssertDistrictResult


#TODO delete if become useless
class OpenDataServicesTest(unittest.TestCase):
    def test_if_datas_has_been_retrives(self):
        dataServices = OpenDataServices()

        result = dataServices.RetrieveDatas()

        AssertDepartment('1|Ain|13|Bouches-du-Rhône|31|Haute-Garonne|33|Gironde', result, self)
        AssertDistrictResult('33|Gironde|3310|10ème circonscription|83589|59039|70,63%|24550|29,37%|57167|68,39%|96,83%|1267|1.52|2.15|605|0.72|1.02|EXG|HALBIN|Hélène|FEMININ|1117|1.34|1.95|ENS|BOUDIÉ|Florent|MASCULIN|17128|20.49|29.96|UG|BOURGOIS|Pascal|MASCULIN|13885|16.61|24.29|RN|CHADOURNE|Sandrine|FEMININ|25037|29.95|43.8',result.Districts[0], self )
        AssertDistrictResult('13|Bouches-du-Rhône|1316|16ème circonscription|91684|61560|67,14%|30124|32,86%|59805|65,23%|97,15%|1088|1,19%|1,77%|667|0,73%|1,08%|REC|SEDDIK|Florent|MASCULIN|712|0.78|1.19|EXG|DUBOST|Guy|MASCULIN|505|0.55|0.84|UG|KOUKAS|Nicolas|MASCULIN|17896|19.52|29.92|ECO|BOUZIANI|Samir|MASCULIN|396|0.43|0.66',result.Districts[1], self )            
        AssertDistrictResult('71|Saône-et-Loire|7102|2ème circonscription|76621|53570|69,92%|23051|30,08%|52144|68,05%|97,34%|894|1,17|1.67|532|0.69|0.99|ENS|ZEKPA|Raymond|MASCULIN|5094|6.65|9.77|RN|DAMIEN|Olivier|MASCULIN|19738|25.76|37.85|UG|GAUTHERON|Sébastien|MASCULIN|9124|11.91|17.5|EXG|BERTHELOT|Patrick|MASCULIN|677|0.88|1.3',result.Districts[2], self )
        AssertParties('UG|Union de la gauche|ENS|ENS Ensemble ! (Majorité présidentielle)|LR|Les Républicains|DVD|Divers droite|RN|Rassemblement National', result.Parties, self)