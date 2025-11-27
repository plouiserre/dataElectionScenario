from domain.Party import Party

def build_parties():
    first_party = __construct_party('UG', 'Union de la gauche', 2)
    second_party = __construct_party('ENS', 'Ensemble ! (Majorité présidentielle)', 3)
    third_party = __construct_party('LR', 'Les Republicains', 4)
    fourth_party = __construct_party('RN', 'Rassemblement National', 5)
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
    parties.append(__construct_party('EXG', 'Extrême gauche', 1))
    parties.append(__construct_party('COM', 'Parti communiste français', 2))
    parties.append(__construct_party('FI', 'La France insoumise', 2))
    parties.append(__construct_party('SOC', 'Parti socialiste', 2))
    parties.append(__construct_party('RDG', 'Parti radical de gauche', 2))
    parties.append(__construct_party('VEC', 'Les Ecologistes', 2))
    parties.append(__construct_party('DVG', 'Divers gauche', 2))
    parties.append(__construct_party('UG', 'Union de la gauche', 2))
    parties.append(__construct_party('ECO', 'Ecologistes', 2))
    parties.append(__construct_party('REG', 'Régionaliste', 2))
    parties.append(__construct_party('DIV', 'Divers', 2))
    parties.append(__construct_party('REN', 'Renaissance', 3))
    parties.append(__construct_party('MDM', 'Modem', 3))
    parties.append(__construct_party('HOR', 'Horizons', 3))
    parties.append(__construct_party('ENS', 'Ensemble ! (Majorité présidentielle)', 3))
    parties.append(__construct_party('DVC', 'Divers centre', 3))
    parties.append(__construct_party('UDI', 'Union des Démocrates et Indépendants', 4))
    parties.append(__construct_party('LR', 'Les Républicains', 4))
    parties.append(__construct_party('DVD', 'Divers droite', 4))
    parties.append(__construct_party('DSV', 'Droite souverainiste', 4))
    parties.append(__construct_party('RN', 'Rassemblement National', 5))
    parties.append(__construct_party('REC', 'Reconquête !', 5))
    parties.append(__construct_party('UXD', "Union de Extrême droite", 5))
    parties.append(__construct_party('EXD', 'Extrême droite', 5))
    return parties
    
def __get_all_parties_2022():
    parties = []
    parties.append(__construct_party('DXG', 'Divers extrême gauche', 1))
    parties.append(__construct_party('RDG', 'Parti radical de gauche', 2))
    parties.append(__construct_party('NUP', 'Nouvelle union populaire écologique et sociale', 2))
    parties.append(__construct_party('DVG', 'Divers gauche', 2))
    parties.append(__construct_party('ECO', 'Ecologistes', 10))
    parties.append(__construct_party('DIV', 'Divers', 10))
    parties.append(__construct_party('REG', 'Régionaliste', 10))
    parties.append(__construct_party('ENS', 'Ensemble ! (Majorité présidentielle)', 3))
    parties.append(__construct_party('DVC', 'Divers centre', 3))
    parties.append(__construct_party('UDI', 'Union des Démocrates et des Indépendants', 3))
    parties.append(__construct_party('LR', 'Les Républicains', 4))
    parties.append(__construct_party('DVD', 'Divers droite', 4))
    parties.append(__construct_party('DSV', 'Droite souverainiste', 4))
    parties.append(__construct_party('REC', 'Reconquête !', 5))
    parties.append(__construct_party('RN', 'Rassemblement National', 5))
    parties.append(__construct_party('DXD', 'Divers extrême droite', 5))
    return parties          

def __construct_party(code, name, family): 
    party = Party()
    party.code = code
    party.name = name
    party.family = family
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
        json_party = "\"name\":\"{name}\",\"code\":\"{code}\",\"family\":\"{family}\"".format(
            name = party.name, code = party.code, family = party.family
        )
        json_final = "{"+json_party+"}"
        return json_final
