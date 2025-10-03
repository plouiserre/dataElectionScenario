from domain.Party import Party
class PartyMemory():
    def __init__(self):
        self.parties = []

    #this code is tested in OpenDataServicesTest
    def get_all_parties(self):
        self.__construct_parties('EXG', 'Extrême gauche')
        self.__construct_parties('COM', 'Parti communiste français')
        self.__construct_parties('FI', 'La France insoumise')
        self.__construct_parties('SOC', 'Parti socialiste')
        self.__construct_parties('RDG', 'Parti radical de gauche')
        self.__construct_parties('VEC', 'Les Ecologistes')
        self.__construct_parties('DVG', 'Divers gauche')
        self.__construct_parties('UG', 'Union de la gauche')
        self.__construct_parties('ECO', 'Ecologistes')
        self.__construct_parties('REG', 'Régionaliste')
        self.__construct_parties('DIV', 'Divers')
        self.__construct_parties('REN', 'Renaissance')
        self.__construct_parties('MDM', 'Modem')
        self.__construct_parties('HOR', 'Horizons')
        self.__construct_parties('ENS', 'Ensemble ! (Majorité présidentielle)')
        self.__construct_parties('DVC', 'Divers centre')
        self.__construct_parties('UDI', 'Union des Démocrates et Indépendants')
        self.__construct_parties('LR', 'Les Républicains')
        self.__construct_parties('DVD', 'Divers droite')
        self.__construct_parties('DSV', 'Droite souverainiste')
        self.__construct_parties('RN', 'Rassemblement National')
        self.__construct_parties('REC', 'Reconquête !')
        self.__construct_parties('UXD', 'Union de l\'extrême droite')
        self.__construct_parties('EXD', 'Extrême droite')

        return self.parties
    

    def __construct_parties(self, code, name):
        party = Party()
        party.code = code
        party.name = name
        self.parties.append(party)