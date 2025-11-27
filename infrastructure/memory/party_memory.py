from domain.Party import Party
class PartyMemory():
    def __init__(self):
        self.parties = []
        self.all_parties = {}

    def get_all_parties(self):
        all_parties_2022 = self.__get_all_parties_2022()
        all_parties_2024 = self.__get_all_parties_2024()
        self.all_parties[2022] = all_parties_2022
        self.all_parties[2024] = all_parties_2024
        return self.all_parties
    
    def __get_all_parties_2024(self):
        self.parties = []
        self.__construct_parties('EXG', 'Extrême gauche', 1)
        self.__construct_parties('COM', 'Parti communiste français', 2)
        self.__construct_parties('FI', 'La France insoumise', 2)
        self.__construct_parties('SOC', 'Parti socialiste', 2)
        self.__construct_parties('RDG', 'Parti radical de gauche', 2)
        self.__construct_parties('VEC', 'Les Ecologistes', 2)
        self.__construct_parties('DVG', 'Divers gauche', 2)
        self.__construct_parties('UG', 'Union de la gauche', 2)
        self.__construct_parties('ECO', 'Ecologistes', 10)
        self.__construct_parties('REG', 'Régionaliste', 10)
        self.__construct_parties('DIV', 'Divers', 10)
        self.__construct_parties('REN', 'Renaissance', 3)
        self.__construct_parties('MDM', 'Modem', 3)
        self.__construct_parties('HOR', 'Horizons', 3)
        self.__construct_parties('ENS', 'Ensemble ! (Majorité présidentielle)', 3)
        self.__construct_parties('DVC', 'Divers centre', 3)
        self.__construct_parties('UDI', 'Union des Démocrates et Indépendants', 4)
        self.__construct_parties('LR', 'Les Républicains', 4)
        self.__construct_parties('DVD', 'Divers droite', 4)
        self.__construct_parties('DSV', 'Droite souverainiste', 4)
        self.__construct_parties('RN', 'Rassemblement National', 5)
        self.__construct_parties('REC', 'Reconquête !', 5)
        self.__construct_parties('UXD', 'Union de l\'extrême droite', 5)
        self.__construct_parties('EXD', 'Extrême droite', 5)
        return self.parties
    
    def __get_all_parties_2022(self):
        self.parties = []
        self.__construct_parties('DXG', 'Divers extrême gauche', 1)
        self.__construct_parties('RDG', 'Parti radical de gauche', 2)
        self.__construct_parties('NUP', 'Nouvelle union populaire écologique et sociale', 2)
        self.__construct_parties('DVG', 'Divers gauche', 2)
        self.__construct_parties('ECO', 'Ecologistes', 10)
        self.__construct_parties('DIV', 'Divers', 10)
        self.__construct_parties('REG', 'Régionaliste', 10)
        self.__construct_parties('ENS', 'Ensemble ! (Majorité présidentielle)', 3)
        self.__construct_parties('DVC', 'Divers centre', 3)
        self.__construct_parties('UDI', 'Union des Démocrates et des Indépendants', 4)
        self.__construct_parties('LR', 'Les Républicains', 4)
        self.__construct_parties('DVD', 'Divers droite', 4)
        self.__construct_parties('DSV', 'Droite souverainiste', 4)
        self.__construct_parties('REC', 'Reconquête !', 5)
        self.__construct_parties('RN', 'Rassemblement National', 5)
        self.__construct_parties('DXD', 'Divers extrême droite', 5)
        return self.parties    

    def __construct_parties(self, code, name, family):
        party = Party()
        party.code = code
        party.name = name
        party.family = family
        self.parties.append(party)