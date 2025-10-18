import unittest
from infrastructure.adapter.AdaptParty import AdaptParty
from tests.utils.build_party import build_parties, construct_party_json

class AdaptPartyTest(unittest.TestCase):

    def test_ug_party_to_json(self):
            adaptParty = AdaptParty()
            parties = build_parties()
            party = parties[2022][0]

            json = adaptParty.to_json(party)

            json_expected = construct_party_json(party)

            self.assertEqual(json, json_expected)