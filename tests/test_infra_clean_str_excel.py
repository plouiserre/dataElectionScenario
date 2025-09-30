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

