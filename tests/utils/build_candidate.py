from domain.Candidate import Candidate

def build_first_candidate():
    first_candidate = __construct_candidate('LARSONNEUR', 'Jean-Charles', 'DVC', 'MASCULIN', '19239', '24.61%',	'35.68%')
    return first_candidate

def build_second_candidate():
    second_candidate = __construct_candidate('CADALEN', 'Pierre-Yves', 'UG', 'MASCULIN', '22110', '41.01%', '28.28%')
    return second_candidate

def build_third_candidate():
     third_candidate = __construct_candidate('KERVELLA', 'Denis', 'RN', 'MASCULIN', '12567', '23.31%', '16.07%')
     return third_candidate

def build_fourth_candidate():
     fourth_candidate = __construct_candidate('RAMOS', 'Richard', 'ENS', 'MASCULIN', '31737', '63.31%', '41.70%')
     return fourth_candidate

def build_fifth_candidate():
     fifth_candidate = __construct_candidate('ZELLER', 'Anthony', 'RN', 'MASCULIN', '18392', '36.69%', '24.17%')
     return fifth_candidate

def build_sixth_candidate():
    sixth_candidate = __construct_candidate('MOREL', 'Louise', 'ENS', 'FEMININ', '35890', '55.02%', '36.52%')
    return sixth_candidate

def build_seventh_candidate():
    seventh_candidate = __construct_candidate('COUSSEDIERE', 'Vincent', 'RN', 'MASCULIN','29338', '44.98%', '29.85%')
    return seventh_candidate

def build_eighth_candidate():
     eighth_candidate = __construct_candidate('BOUDIÉ', 'Florent', 'ENS', 'MASCULIN','28960', '34.63%', '52.17%')
     return eighth_candidate
    


def __construct_candidate(first_name, last_name, parti_code, sexe, vote, vote_by_expressed, vote_by_registered):
        candidate = Candidate()
        candidate.first_name = first_name
        candidate.last_name = last_name
        candidate.parti_code = parti_code 
        candidate.sexe = sexe
        candidate.vote = vote
        candidate.vote_expressed = vote_by_expressed
        candidate.vote_registered = vote_by_registered
        return candidate 

def construct_candidate_json(candidate):
    json_candidate = "\"lastName\":\"{lastname}\",\"firstName\":\"{firstName}\", \"sexe\":\"{sexe}\",\"partiCode\":\"{partiCode}\",\"vote\":{vote},\"voteByRegistered\":\"{voteByRegistered}\",\"voteByExpressed\":\"{voteByExpressed}\" ".format(
            lastname = candidate.last_name, firstName = candidate.first_name, sexe = candidate.sexe, partiCode = candidate.parti_code, 
            vote = candidate.vote, voteByRegistered = candidate.vote_registered, voteByExpressed = candidate.vote_expressed)
    json_final = "{"+json_candidate+"}"
    return json_final
     