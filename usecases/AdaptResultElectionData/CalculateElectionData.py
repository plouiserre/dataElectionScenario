class CalculateElectionData : 
    def __init__(self, dataServices):
        self.dataServices = dataServices

    def Calculate(self):
        results = self.dataServices.RetrieveDatas()
        return True