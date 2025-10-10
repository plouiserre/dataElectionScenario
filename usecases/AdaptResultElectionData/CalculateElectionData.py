class CalculateElectionData : 
    def __init__(self, dataServices):
        self.dataServices = dataServices

    def Calculate(self):
        results = self.dataServices.RetrieveDatas()
        is_ok = self.dataServices.SaveDatas(results)
        return is_ok