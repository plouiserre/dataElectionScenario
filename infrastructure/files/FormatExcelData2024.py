from infrastructure.files.FormatExcelData import FormatExcelData

class FormatExcelData2024(FormatExcelData):
    def __init__(self):
        super().__init__()

    def format(self, text):
        data = text
        data = self._delete_square_bracket(data)
        data = self._replace_complexe_words(data)
        datas = self._separate_str(data)
        datas = self.__clean_percentage(datas)
        datas = self._reput_forbidden_words(datas)
        return datas
    
    def __clean_percentage(self, datas):
        datas_cleaned = []
        for data in datas : 
            data = self.__update_percentage(data)
            datas_cleaned.append(data)
        return datas_cleaned

    def __update_percentage(self, data) : 
        data_cleaned = data
        if '%' in data : 
            data_cleaned = data.replace(',','.')
        return data_cleaned