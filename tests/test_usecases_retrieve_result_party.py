import unittest
from tests.utils.assertCustom import AssertParties
from usecases.AdaptResultElectionData.RetrieveParty import RetrieveParty

class UsecasesRetrieveResultDepartmentTest(unittest.TestCase):
    def test_parties_are_finded(self):
        retrieveParty = RetrieveParty()

        resultParties = retrieveParty.Search()

        AssertParties('UG|Union de la gauche|ENS|ENS Ensemble ! (Majorité présidentielle)|LR|Les Républicains|DVD|Divers droite|RN|Rassemblement National', resultParties, self)