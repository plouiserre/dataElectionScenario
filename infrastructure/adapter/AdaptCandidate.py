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

    def to_json(self, candidate):
        json_candidate = "\"lastName\":\"{lastName}\",\"firstName\":\"{firstName}\", \"sexe\":\"{sexe}\",\"partiCode\":\"{partiCode}\"," \
        "\"vote\":{vote},\"voteByRegistered\":\"{voteByRegistered}\",\"voteByExpressed\":\"{voteByExpressed}\" ".format(
            lastName = candidate.lastName, firstName = candidate.firstName, sexe = candidate.sexe, partiCode = candidate.partiCode, 
            vote = candidate.vote, voteByRegistered = candidate.voteByRegistered, voteByExpressed = candidate.voteByExpressed
        )
        json_final = "{"+json_candidate+"}"
        return json_final