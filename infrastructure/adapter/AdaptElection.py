from domain.Election import Election

class AdaptElection : 
    def __init__(self, adaptDistrict):
        self.AdaptDistrict = adaptDistrict        

    def Transform(self, datas, year):
        self.districts = []
        for data in datas : 
            district = self.AdaptDistrict.Transform(data)
            self.districts.append(district)  
        election = Election()
        election.year = year
        election.Districts = self.districts
        return election
        