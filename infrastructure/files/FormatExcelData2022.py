from infrastructure.files.FormatExcelData import FormatExcelData

class FormatExcelData2022(FormatExcelData):
    def __init__(self):
        super().__init__()

    def format(self, text):
        data = text
        data = self._delete_square_bracket(data)
        data = self._replace_forbidden_words(data)
        datas = self._separate_str(data)
        datas = self.__delete_complet_word(datas)
        datas = self.__clean_percentage(datas)
        datas = self._reput_forbidden_words(datas)
        return datas
    
    def __delete_complet_word(self, datas):
        datas_accepted = []
        for data in datas :
            if data == "Complet":
                continue
            else : 
                datas_accepted.append(data)
        return datas_accepted
    
    def __clean_percentage(self, datas):
        datas_accepted = []
        for data in datas :
            if '.' in data:
                new_data = data+'%'
                datas_accepted.append(new_data)
            else : 
                datas_accepted.append(data)
        return datas_accepted