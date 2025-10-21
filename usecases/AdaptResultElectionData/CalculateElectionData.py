class CalculateElectionData : 
    def __init__(self, dataServices):
        self.dataServices = dataServices

    def Calculate(self):
        results = self.dataServices.retrieveDatas()
        is_ok = self.dataServices.saveDatas(results)
        return is_ok