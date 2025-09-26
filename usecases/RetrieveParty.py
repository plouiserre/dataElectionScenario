from usecases.Retrieve import Retrieve
from domain.Party import Party

# EXG Extrême gauche 
# COM Parti communiste français 
# FI La France insoumise 
# SOC Parti socialiste
# RDG Parti radical de gauche 
# VEC Les Ecologistes 
# DVG Divers gauche 
# UG Union de la gauche 
# ECO Ecologistes 
# REG Régionaliste 
# DIV Divers 
# REN Renaissance 
# MDM Modem 
# HOR Horizons 
# ENS Ensemble ! (Majorité présidentielle) 
# DVC Divers centre 
# UDI Union des Démocrates et Indépendants 
# LR Les Républicains 
# DVD Divers droite 
# DSV Droite souverainiste 
# RN Rassemblement National 
# REC Reconquête ! 
# UXD Union de l'extrême droite 
# EXD Extrême droite 

class RetrieveParty(Retrieve):
    def __init__(self):
        super().__init__()


    def Search(self):        
        firstParty = self.__setParties('UG', 'Union de la gauche')
        secondParty = self.__setParties('ENS', 'ENS Ensemble ! (Majorité présidentielle)')
        thirdParty = self.__setParties('LR', 'Les Républicains')
        fourthParty = self.__setParties('DVD', 'Divers droite')
        fifthParty = self.__setParties('RN', 'Rassemblement National')
        parties = []
        parties.append(firstParty)
        parties.append(secondParty)
        parties.append(thirdParty)
        parties.append(fourthParty)
        parties.append(fifthParty)
        return parties
    

    def __setParties(self, code, name): 
        party = Party()
        party.code = code
        party.name = name
        return party