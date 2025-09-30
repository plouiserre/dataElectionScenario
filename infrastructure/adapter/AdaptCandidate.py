from domain.Candidate import Candidate

class AdaptCandidate():
    def __init__(self):
        pass

    def Transform(self, datas):
        candidate = Candidate()
        candidate.partiCode = datas[0]
        candidate.lastName = datas[1]
        candidate.firstName = datas[2]
        candidate.sexe = datas[3]
        candidate.vote = datas[4]
        candidate.voteByRegistered = datas[5]
        candidate.voteByExpressed = datas[6]
        return candidate