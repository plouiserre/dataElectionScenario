import unittest
from infrastructure.files.CleanStrExcel import CleanLineExcel

class CleanStrExcelTest(unittest.TestCase):
    def test_clean_str_simple_line_excel(self):
        str_excel = "['33' 'Gironde' 3310 '10ème circonscription' 83620 58727 '70,23%' 24893 '29,77%' 55515 '66,39%' '94,53%' 2365 '2,83%' '4,03%' 847 '1,01%' '1,44%']"

        str_cleaned = CleanLineExcel(str_excel)

        self.assertEqual(18, len(str_cleaned))
        self.assertEqual('33', str_cleaned[0])
        self.assertEqual('Gironde', str_cleaned[1])
        self.assertEqual('3310', str_cleaned[2])
        self.assertEqual('10ème circonscription', str_cleaned[3])
        self.assertEqual('83620', str_cleaned[4])
        self.assertEqual('58727', str_cleaned[5])
        self.assertEqual('70.23%', str_cleaned[6])
        self.assertEqual('24893', str_cleaned[7])
        self.assertEqual('29.77%', str_cleaned[8])
        self.assertEqual('55515', str_cleaned[9])
        self.assertEqual('66.39%', str_cleaned[10])
        self.assertEqual('94.53%', str_cleaned[11])
        self.assertEqual('2365', str_cleaned[12])
        self.assertEqual('2.83%', str_cleaned[13])
        self.assertEqual('4.03%', str_cleaned[14])
        self.assertEqual('847', str_cleaned[15])
        self.assertEqual('1.01%', str_cleaned[16])
        self.assertEqual('1.44%', str_cleaned[17])


    def test_clean_str_simple_line_excel_with_nan(self):
        str_excel = "['33' 'Gironde' 3310 '10ème circonscription' 83620 58727 '70,23%' 24893 '29,77%' 55515 '66,39%' '94,53%' 2365 '2,83%' '4,03%' 847 '1,01%' '1,44%' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"

        str_cleaned = CleanLineExcel(str_excel)

        self.assertEqual(18, len(str_cleaned))
        self.assertEqual('33', str_cleaned[0])
        self.assertEqual('Gironde', str_cleaned[1])
        self.assertEqual('3310', str_cleaned[2])
        self.assertEqual('10ème circonscription', str_cleaned[3])
        self.assertEqual('83620', str_cleaned[4])
        self.assertEqual('58727', str_cleaned[5])
        self.assertEqual('70.23%', str_cleaned[6])
        self.assertEqual('24893', str_cleaned[7])
        self.assertEqual('29.77%', str_cleaned[8])
        self.assertEqual('55515', str_cleaned[9])
        self.assertEqual('66.39%', str_cleaned[10])
        self.assertEqual('94.53%', str_cleaned[11])
        self.assertEqual('2365', str_cleaned[12])
        self.assertEqual('2.83%', str_cleaned[13])
        self.assertEqual('4.03%', str_cleaned[14])
        self.assertEqual('847', str_cleaned[15])
        self.assertEqual('1.01%', str_cleaned[16])
        self.assertEqual('1.44%', str_cleaned[17])



    def test_clean_str_complexe_line_cote_d_or_department(self):
        str_excel = "['21' 'Côte-d'Or' 2101 '1ère circonscription' 70511 51765 '73,41%' 18746 '26,59%' 50386 '71,46%' '97,34%' 1081 '1,53%' '2,09%' 298 '0,42%' '0,58%' 1 'UG' 'GODARD' 'Océane' 'FEMININ' 18716 '26,54%' '37,15%' 'élu' '4.0' 'ENS' 'MARTIN' 'Didier' 'MASCULIN' '17314.0' '24,56%' '34,36%' 'nan' '5.0' 'RN' 'HUMBLOT-CORNILLE' 'Cyline' 'FEMININ' '14356.0' '20,36%' '28,49%' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']"

        str_cleaned = CleanLineExcel(str_excel)

        self.assertEqual(43, len(str_cleaned))
        self.assertEqual('21', str_cleaned[0])
        self.assertEqual('Côte-d\'Or', str_cleaned[1])
        self.assertEqual('2101', str_cleaned[2])
        self.assertEqual('1ère circonscription', str_cleaned[3])
        self.assertEqual('70511', str_cleaned[4])
        self.assertEqual('51765', str_cleaned[5])
        self.assertEqual('73.41%', str_cleaned[6])
        self.assertEqual('18746', str_cleaned[7])
        self.assertEqual('26.59%', str_cleaned[8])
        self.assertEqual('50386', str_cleaned[9])
        self.assertEqual('71.46%', str_cleaned[10])
        self.assertEqual('97.34%', str_cleaned[11])
        self.assertEqual('1081', str_cleaned[12])
        self.assertEqual('1.53%', str_cleaned[13])
        self.assertEqual('2.09%', str_cleaned[14])
        self.assertEqual('298', str_cleaned[15])
        self.assertEqual('0.42%', str_cleaned[16])
        self.assertEqual('0.58%', str_cleaned[17])        
        self.assertEqual('1', str_cleaned[18])
        self.assertEqual('UG', str_cleaned[19])
        self.assertEqual('GODARD', str_cleaned[20])
        self.assertEqual('Océane', str_cleaned[21])
        self.assertEqual('FEMININ', str_cleaned[22])
        self.assertEqual('18716', str_cleaned[23])
        self.assertEqual('26.54%', str_cleaned[24])
        self.assertEqual('37.15%', str_cleaned[25])
        self.assertEqual('élu', str_cleaned[26])
        self.assertEqual('4.0', str_cleaned[27])
        self.assertEqual('ENS', str_cleaned[28])
        self.assertEqual('MARTIN', str_cleaned[29])
        self.assertEqual('Didier', str_cleaned[30])
        self.assertEqual('MASCULIN', str_cleaned[31])
        self.assertEqual('17314.0', str_cleaned[32])
        self.assertEqual('24.56%', str_cleaned[33])
        self.assertEqual('34.36%', str_cleaned[34])
        self.assertEqual('5.0', str_cleaned[35])
        self.assertEqual('RN', str_cleaned[36])        
        self.assertEqual('HUMBLOT-CORNILLE', str_cleaned[37])
        self.assertEqual('Cyline', str_cleaned[38])
        self.assertEqual('FEMININ', str_cleaned[39])
        self.assertEqual('14356.0', str_cleaned[40])
        self.assertEqual('20.36%', str_cleaned[41])
        self.assertEqual('28.49%', str_cleaned[42])