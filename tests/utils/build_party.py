from domain.Party import Party

def build_parties():
    first_party = __construct_party('UG', 'Union de la gauche')
    second_party = __construct_party('ENS', 'Ensemble ! (Majorité présidentielle)')
    third_party = __construct_party('LR', 'Les Republicains')
    fourth_party = __construct_party('RN', 'Rassemblement National')
    parties = {}
    first_year_parties = []
    second_year_parties = []
    first_year_parties.append(first_party)
    second_year_parties.append(second_party)
    first_year_parties.append(third_party)
    second_year_parties.append(fourth_party)
    parties[2022] = first_year_parties
    parties[2024] = second_year_parties
    return parties    

def __construct_party(code, name): 
    party = Party()
    party.code = code
    party.name = name
    return party  

def construct_parties_json(parties_by_year):
        first_party_json = construct_party_json(parties_by_year[2022][0])
        second_party_json = construct_party_json(parties_by_year[2022][1])
        third_party_json = construct_party_json(parties_by_year[2024][0])
        fourth_party_json = construct_party_json(parties_by_year[2024][1])
        first_year = "\"2022\":[{first_party},{second_party}]".format(first_party = first_party_json, 
            second_party = second_party_json)
        second_year = "\"2024\":[{third_party},{fourth_party}]".format(third_party = third_party_json, 
            fourth_party = fourth_party_json)
        parties_data = "{first_year},{second_year}".format(first_year = first_year, second_year = second_year)
        parties_json_concat = "\"parties\":{"+parties_data+"}"
        return parties_json_concat        

def construct_party_json(party):
        json_party = "\"name\":\"{name}\",\"code\":\"{code}\"".format(
            name = party.name, code = party.code
        )
        json_final = "{"+json_party+"}"
        return json_final
