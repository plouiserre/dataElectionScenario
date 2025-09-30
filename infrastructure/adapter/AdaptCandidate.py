from domain.Candidate import Candidate

class AdaptCandidate():
    def __init__(self):
        pass

    def Transform(self, datas):
        candidate = Candidate()
        candidate.partiCode = datas[1]
        candidate.lastName = datas[2]
        candidate.firstName = datas[3]
        candidate.sexe = datas[4]
        candidate.vote = datas[5]
        candidate.voteByRegistered = datas[6]
        candidate.voteByExpressed = datas[7]
        return candidate