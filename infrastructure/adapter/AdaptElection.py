from domain.Election import Election

class AdaptElection : 
    def __init__(self, adaptDistrict):
        self.AdaptDistrict = adaptDistrict        

    def Transform(self, datas, year):
        self.districts = []
        for data in datas : 
            district = self.AdaptDistrict.Transform(data, year)
            self.districts.append(district)  
        election = Election()
        election.year = year
        election.Districts = self.districts
        return election
    
    def to_json(self, election):
        json_districts = "\"districts\":["
        for i, district in enumerate(election.Districts):
            json_district = self.AdaptDistrict.to_json(district)
            if(i == len(election.Districts) - 1):
                json_districts += json_district
            else : 
                json_districts += json_district +"," 
        json_districts += "]"
        json = "\"year\":{year}, {districts}".format(year = election.year, districts = json_districts)
        json_final  = "{"+json+"}"
        return json_final
        