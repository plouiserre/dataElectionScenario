from domain.Candidate import Candidate

class AdaptCandidate():
    def __init__(self):
        pass

    def Transform(self, datas):
        candidate = Candidate()
        candidate.parti_code = datas[0]
        candidate.last_name = datas[1]
        candidate.first_name = datas[2]
        candidate.sexe = datas[3]
        candidate.vote = datas[4]
        candidate.vote_registered = datas[5]
        candidate.vote_expressed = datas[6]
        return candidate    

    def to_json(self, candidate):
        json_candidate = "\"lastName\":\"{lastName}\",\"firstName\":\"{firstName}\", \"sexe\":\"{sexe}\",\"partiCode\":\"{partiCode}\"," \
        "\"vote\":{vote},\"voteByRegistered\":\"{voteByRegistered}\",\"voteByExpressed\":\"{voteByExpressed}\" ".format(
            lastName = candidate.last_name, firstName = candidate.first_name, sexe = candidate.sexe, partiCode = candidate.parti_code, 
            vote = candidate.vote, voteByRegistered = candidate.vote_registered, voteByExpressed = candidate.vote_expressed
        )
        json_final = "{"+json_candidate+"}"
        return json_final