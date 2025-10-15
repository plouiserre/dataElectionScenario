import unittest
from infrastructure.factory.FormatExcelDataFactory import FormatExcelDataFactory
from infrastructure.files.FormatExcelData2022 import FormatExcelData2022
from infrastructure.files.FormatExcelData2024 import FormatExcelData2024

class FormatExcelDataFactoryTest(unittest.TestCase):
    def test_2024_format_excel_data_factory_choose(self):
        factory = FormatExcelDataFactory()

        format_excel = factory.get_format_excel_data(2024)

        self.assertTrue(isinstance(format_excel, FormatExcelData2024))


    def test_2022_format_excel_data_factory_choose(self):
        factory = FormatExcelDataFactory()

        format_excel = factory.get_format_excel_data(2022)

        self.assertTrue(isinstance(format_excel, FormatExcelData2022))