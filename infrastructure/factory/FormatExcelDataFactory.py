from infrastructure.files.FormatExcelData2022 import FormatExcelData2022
from infrastructure.files.FormatExcelData2024 import FormatExcelData2024

class FormatExcelDataFactory: 
    def __init__(self):
        pass

    def get_format_excel_data(self, key):
        if(key == 2024) :
            return FormatExcelData2024()
        else :
            return FormatExcelData2022()