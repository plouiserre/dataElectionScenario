from domain.Party import Party

def build_parties():
    first_party = __construct_party('UG', 'Union de la gauche')
    second_party = __construct_party('ENS', 'Ensemble ! (Majorité présidentielle)')
    third_party = __construct_party('LR', 'Les Republicains')
    fourth_party = __construct_party('RN', 'Rassemblement National')
    parties = []
    parties.append(first_party)
    parties.append(second_party)
    parties.append(third_party)
    parties.append(fourth_party)
    return parties    

def __construct_party(code, name): 
    party = Party()
    party.code = code
    party.name = name
    return party  

def construct_parties_json(parties):
        first_party_json = construct_party_json(parties[0])
        second_party_json = construct_party_json(parties[1])
        third_party_json = construct_party_json(parties[2])
        fourth_party_json = construct_party_json(parties[3])
        parties_json_concat = "\"parties\":[{first_party}, {second_party}, {third_party}, {fourth_party}]".format(
            first_party = first_party_json, second_party = second_party_json, third_party = third_party_json,
            fourth_party = fourth_party_json
        )
        return parties_json_concat        

def construct_party_json(party):
        json_party = "\"name\":\"{name}\",\"code\":\"{code}\"".format(
            name = party.name, code = party.code
        )
        json_final = "{"+json_party+"}"
        return json_final
