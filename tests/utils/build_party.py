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

def build_all_parties():
    parties = {}
    parties[2022] = __get_all_parties_2022()
    parties[2024] = __get_all_parties_2024()
    return parties

def __get_all_parties_2024():
    parties = []
    parties.append(__construct_party('EXG', 'Extrême gauche'))
    parties.append(__construct_party('COM', 'Parti communiste français'))
    parties.append(__construct_party('FI', 'La France insoumise'))
    parties.append(__construct_party('SOC', 'Parti socialiste'))
    parties.append(__construct_party('RDG', 'Parti radical de gauche'))
    parties.append(__construct_party('VEC', 'Les Ecologistes'))
    parties.append(__construct_party('DVG', 'Divers gauche'))
    parties.append(__construct_party('UG', 'Union de la gauche'))
    parties.append(__construct_party('ECO', 'Ecologistes'))
    parties.append(__construct_party('REG', 'Régionaliste'))
    parties.append(__construct_party('DIV', 'Divers'))
    parties.append(__construct_party('REN', 'Renaissance'))
    parties.append(__construct_party('MDM', 'Modem'))
    parties.append(__construct_party('HOR', 'Horizons'))
    parties.append(__construct_party('ENS', 'Ensemble ! (Majorité présidentielle)'))
    parties.append(__construct_party('DVC', 'Divers centre'))
    parties.append(__construct_party('UDI', 'Union des Démocrates et Indépendants'))
    parties.append(__construct_party('LR', 'Les Républicains'))
    parties.append(__construct_party('DVD', 'Divers droite'))
    parties.append(__construct_party('DSV', 'Droite souverainiste'))
    parties.append(__construct_party('RN', 'Rassemblement National'))
    parties.append(__construct_party('REC', 'Reconquête !'))
    parties.append(__construct_party('UXD', "Union de Extrême droite"))
    parties.append(__construct_party('EXD', 'Extrême droite'))
    return parties
    
def __get_all_parties_2022():
    parties = []
    parties.append(__construct_party('DXG', 'Divers extrême gauche'))
    parties.append(__construct_party('RDG', 'Parti radical de gauche'))
    parties.append(__construct_party('NUP', 'Nouvelle union populaire écologique et sociale'))
    parties.append(__construct_party('DVG', 'Divers gauche'))
    parties.append(__construct_party('ECO', 'Ecologistes'))
    parties.append(__construct_party('DIV', 'Divers'))
    parties.append(__construct_party('REG', 'Régionaliste'))
    parties.append(__construct_party('ENS', 'Ensemble ! (Majorité présidentielle)'))
    parties.append(__construct_party('DVC', 'Divers centre'))
    parties.append(__construct_party('UDI', 'Union des Démocrates et des Indépendants'))
    parties.append(__construct_party('LR', 'Les Républicains'))
    parties.append(__construct_party('DVD', 'Divers droite'))
    parties.append(__construct_party('DSV', 'Droite souverainiste'))
    parties.append(__construct_party('REC', 'Reconquête !'))
    parties.append(__construct_party('RN', 'Rassemblement National'))
    parties.append(__construct_party('DXD', 'Divers extrême droite'))
    return parties          

def __construct_party(code, name): 
    party = Party()
    party.code = code
    party.name = name
    return party  

def construct_all_parties_json(parties):        
    first_year_parties = __construct_parties_json_by_year(parties[2022])
    second_year_parties = __construct_parties_json_by_year(parties[2024])
    json_final = "\"parties\":{\"2022\":"+first_year_parties+",\"2024\":"+second_year_parties+"}"
    return json_final

def __construct_parties_json_by_year(parties):
    parties_json = '['
    for idx, party in enumerate(parties):
        if idx < len(parties) - 1:
            parties_json += construct_party_json(party)+','
        else :
            parties_json += construct_party_json(party)
    parties_json += ']'
    return parties_json

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
