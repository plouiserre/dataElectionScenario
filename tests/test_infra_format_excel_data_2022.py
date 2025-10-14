import unittest
from infrastructure.files.FormatExcelData2022 import FormatExcelData2022

class FromExcelData2022Test(unittest.TestCase):
    def test_separate_gironde_districts_2022_elections(self):
        excel_line = "['33' 'Gironde' 10 '10ème circonscription' 'Complet' 83277 40667 '48.83' 42610 '51.17' 781 '0.94' '1.83' 347 '0.42' '0.81' 41482 '49.81' '97.35' 9 'F' 'HALBIN' 'Hélène' 'DXG' 507 '0.61' '1.22' 'nan' 5 'F' 'PLANTON' 'Veronique, Raymonde' 'RDG' 2034 '2.44' '4.9' 'nan' 3 'M' 'BOURGOIS' 'Pascal' 'NUP' 9705 '11.65' '23.4' 'nan' 6 'F' 'BERNARD' 'Muriel' 'DVG' 0 '0.0' '0.0' 'nan' '8.0' 'F' 'GUILBERT' 'Amélie' 'ECO' '606.0' '0.73' '1.46' 'nan' '10.0' 'F' 'DEJONG-PAUSS' 'Angélique' 'DIV' '262.0' '0.31' '0.63' 'nan' '2.0' 'M' 'BOUDIÉ' 'Florent' 'ENS' '13565.0' '16.29' '32.7' 'nan' '4.0' 'F' 'FLEURY' 'Catherine' 'DSV' '593.0' '0.71' '1.43' 'nan' '7.0' 'M' 'MALHERBE' 'Gonzague' 'REC' '2582.0' '3.1' '6.22' 'nan' '1.0' 'F' 'CHADOURNE' 'Sandrine' 'RN' '11628.0' '13.96' '28.03' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' ]"
        
        excel_format = FormatExcelData2022()

        datas = excel_format.format(excel_line)

        self.assertEqual('33', datas[0])
        self.assertEqual('Gironde', datas[1])
        self.assertEqual('10', datas[2])
        self.assertEqual('10ème circonscription', datas[3])
        self.assertEqual('83277', datas[4])
        self.assertEqual('40667', datas[5])
        self.assertEqual('48.83%', datas[6])
        self.assertEqual('42610', datas[7])
        self.assertEqual('51.17%', datas[8])
        self.assertEqual('781', datas[9])
        self.assertEqual('0.94%', datas[10])
        self.assertEqual('1.83%', datas[11])
        self.assertEqual('347', datas[12])
        self.assertEqual('0.42%', datas[13])
        self.assertEqual('0.81%', datas[14])
        self.assertEqual('41482', datas[15])
        self.assertEqual('49.81%', datas[16])
        self.assertEqual('97.35%', datas[17])
