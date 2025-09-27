class CalculateElectionData : 
    def __init__(self, retrieveParty, retrieveDepartment, retrieveElectionDistrict):
        self.retrieveParty = retrieveParty
        self.retrieveDepartment = retrieveDepartment
        self.retrieveElectionDistrict = retrieveElectionDistrict        

    def Calculate(self):
        parties = self.retrieveParty.Search()
        departments = self.retrieveDepartment.Search()
        districts = self.retrieveElectionDistrict.Search()
        return True