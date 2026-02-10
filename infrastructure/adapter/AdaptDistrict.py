from domain.District import District
from infrastructure.factory.FormatExcelDataFactory import FormatExcelDataFactory


class AdaptDistrict():
    def __init__(self, adapt_candidate):
        self.datasStr = ''
        self.datas = []
        self.candidates_datas = []
        self.candidates = []
        self.adapt_candidate = adapt_candidate
        #TODO centralize somewhere
        #TODO supprimer 'DXG' 'NUP' et repenser les parties plus proprement!!!!!!!!
        #TODO retravailler avec https://www.archives-resultats-elections.interieur.gouv.fr/resultats/legislatives-2022/nuances.php
        self.parties_codes = ['EXG', 'DXG', 'COM', 'FI', 'SOC', 'RDG', 'VEC', 'DVG', 'NUP', 'UG', 'ECO', 'REG', 'DIV', 'REN', 'MDM', 'HOR', 'ENS', 
                              'DVC', 'UDI', 'LR', 'DVD', 'DSV', 'RN', 'REC', 'UXD', 'EXD']         
        self.format_excel_factory = FormatExcelDataFactory()
        pass

    def transform(self, datas, key):
        excel_format = self.format_excel_factory.get_format_excel_data(key)
        self.datas = excel_format.format(datas)
        self.__extract_datas_candidates()
        self.__get_candidates()
        district = self.__build_district()
        return district

    def __build_district(self):
        district = District()
        district.department_code = self.datas[0]
        district.number = self.datas[2]
        district.label = self.datas[3]
        district.registered = self.datas[4]
        district.voting = self.datas[5]
        district.candidates = self.candidates
        return district
    
    def __extract_datas_candidates(self):
        self.candidates_datas = []
        for i, data in enumerate(self.datas):
            if(i > 17):
                self.candidates_datas.append(data)


    def __get_candidates(self) : 
        isFirstCandidate = True
        candidate_data_to_adapt = []
        self.candidates = []
        for candidate_data in self.candidates_datas:
            if candidate_data in self.parties_codes and isFirstCandidate == True:
                isFirstCandidate = False
                candidate_data_to_adapt.append(candidate_data)
            elif candidate_data in self.parties_codes and isFirstCandidate == False:
                candidate = self.adapt_candidate.transform(candidate_data_to_adapt)
                self.candidates.append(candidate)
                candidate_data_to_adapt = []      
                candidate_data_to_adapt.append(candidate_data)
            elif isFirstCandidate == False : 
                candidate_data_to_adapt.append(candidate_data)
        candidate = self.adapt_candidate.transform(candidate_data_to_adapt)
        self.candidates.append(candidate)

    def to_json(self, district):
        json_candidates = "\"candidates\":["
        for i, candidate in enumerate(district.candidates):             
            json_candidate = self.adapt_candidate.to_json(candidate)
            if(i == len(district.candidates) - 1):
                json_candidates += json_candidate
            else :
                json_candidates += json_candidate +","
        json_candidates += "]"
        json_district_without_candidates = "\"label\":\"{label}\",\"number\":\"{number}\", \"department code\":\"{department_code}\", \"registered\":{registered}," \
                "\"voting\":{voting} ".format( label = district.label, number = district.number, department_code = self.__manage_department_code_complexe_2022_years(district.department_code),
                registered = district.registered, voting = district.voting)
        json_district_final = "{district}, {candidates}".format(district = json_district_without_candidates, candidates = json_candidates )
        json_district_final = "{"+json_district_final+"}"
        return json_district_final
    

    #TODO move all below in a new class
    def __manage_department_code_complexe_2022_years(self, department_code):
        if department_code == "ZA": 
            return "971"
        elif department_code == "ZB":
            return "972"
        elif department_code == "ZC":
            return "973"
        elif department_code == "ZD": 
            return "974"
        elif department_code == "ZM":
            return "976"
        elif department_code == "ZN":
            return "988"
        elif department_code == "ZP":
            return "987"
        elif department_code == "ZS":
            return "975"
        elif department_code == "ZW":
            return "986"
        else : 
            return self.__change_dpt_code_for_less_than_ten(department_code)
    
    def __change_dpt_code_for_less_than_ten(self, department_code): 
        if department_code.isdigit():
            if int(department_code) > 9 : 
                return department_code
            else : 
                return department_code.replace('0', '')
        else : 
            return department_code
