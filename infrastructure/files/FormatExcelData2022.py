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
        datas = self.__ordered_datas(datas)
        datas = self.__rename_sexe_candidates(datas)
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
        limit_candidate = 18
        first_limit_ok = 6 + limit_candidate
        second_limit_ok = 7 + limit_candidate
        for idx, data in enumerate(datas):
            if idx < limit_candidate : 
                datas_accepted.append(data)
            else :
                is_first_limit = (idx - first_limit_ok) % 8 == 0 and idx > limit_candidate
                is_second_limit = (idx - second_limit_ok) % 8 == 0 and idx > limit_candidate
                if is_first_limit or is_second_limit:
                    new_data = data + '%'
                    datas_accepted.append(new_data)
                else :
                    datas_accepted.append(data)
        return datas_accepted    

    def __ordered_datas(self, datas):
        datas_ok = []
        limit_ok = 18
        datas_tmp = []
        for idx, data in enumerate(datas):
            if(idx < limit_ok) :
                datas_ok.append(data)
            else : 
                new_idx = idx - limit_ok
                if new_idx % 8 == 0 : 
                    if len(datas_tmp) > 0 :
                        candidates_datas_ok = self.__orderered_candidates_datas(datas_tmp)
                        for candidates_data in candidates_datas_ok :
                            datas_ok.append(candidates_data)
                    datas_tmp = []
                datas_tmp.append(data)
        if len(datas_tmp) > 0:
            candidates_datas_ok = self.__orderered_candidates_datas(datas_tmp)
            for candidates_data in candidates_datas_ok :
                datas_ok.append(candidates_data)
        return datas_ok
    
    def __orderered_candidates_datas(self, datas_tmp): 
        sex_data = datas_tmp[1]
        party_data = datas_tmp[4]
        datas_ok = datas_tmp
        datas_ok[1] = party_data
        datas_ok[4] = sex_data
        return datas_ok
    
    def __rename_sexe_candidates(self, datas):
        datas_ok = []
        for data in datas : 
            if data == 'M':
                data = "MASCULIN"
            elif data == 'F':
                data = "FEMININ"
            datas_ok.append(data)
        return datas_ok