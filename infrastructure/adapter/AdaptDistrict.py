from domain.District import District
from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from infrastructure.files.CleanStrExcel import CleanLineExcel

class AdaptDistrict():
    def __init__(self, adapt_candidate):
        self.datasStr = ''
        self.datas = []
        self.candidates_datas = []
        self.candidates = []
        self.adapt_candidate = adapt_candidate
        #TODO centralize somewhere
        self.parties_codes = ['EXG', 'COM', 'FI', 'SOC', 'RDG', 'VEC', 'DVG', 'UG', 'ECO', 'REG', 'DIV', 'REN', 'MDM', 'HOR', 'ENS', 
                              'DVC', 'UDI', 'LR', 'DVD', 'DSV', 'RN', 'REC', 'UXD', 'EXD']         
        pass

    def Transform(self, datas):
        self.datas = CleanLineExcel(datas)
        self.__extract_datas_candidates()
        self.__get_candidates()
        district = self.__build_district()
        return district

    def __build_district(self):
        district = District()
        district.number = self.datas[2]
        district.label = self.datas[3]
        district.registered = self.datas[4]
        district.voting = self.datas[5]
        district.Candidates = self.candidates
        return district
    
    def __extract_datas_candidates(self):
        for i, data in enumerate(self.datas):
            if(i > 17):
                self.candidates_datas.append(data)


    def __get_candidates(self) : 
        isFirstCandidate = True
        candidate_data_to_adapt = []
        for candidate_data in self.candidates_datas:
            if candidate_data in self.parties_codes and isFirstCandidate == True:
                isFirstCandidate = False
                candidate_data_to_adapt.append(candidate_data)
            elif candidate_data in self.parties_codes and isFirstCandidate == False:
                candidate = self.adapt_candidate.Transform(candidate_data_to_adapt)
                self.candidates.append(candidate)
                candidate_data_to_adapt = []      
                candidate_data_to_adapt.append(candidate_data)
            elif isFirstCandidate == False : 
                candidate_data_to_adapt.append(candidate_data)
        candidate = self.adapt_candidate.Transform(candidate_data_to_adapt)
        self.candidates.append(candidate)