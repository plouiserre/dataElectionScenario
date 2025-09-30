from domain.District import District
from infrastructure.files.CleanStrExcel import CleanLineExcel

class AdaptDistrict():
    def __init__(self):
        self.datasStr = ''
        self.datas = []
        self.candidates_datas = []
        pass

    def Transform(self, datas):
        self.datas = CleanLineExcel(datas)
        district = self.__build_district()
        self.__extract_datas_candidates()
        return district

    def __build_district(self):
        district = District()
        district.number = self.datas[2]
        district.label = self.datas[3]
        district.registered = self.datas[4]
        district.voting = self.datas[5]
        return district
    
    def __extract_datas_candidates(self):
        for i, data in enumerate(self.datas):
            if(i > 17):
                self.candidates_datas.append(data)


# class District  : 
#     def __init__(self):
#         self.number = 0
#         self.label = ''
#         self.registered = 0
#         self.voting = 0
#         self.Candidates = []