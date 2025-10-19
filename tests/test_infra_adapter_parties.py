import unittest
from infrastructure.adapter.AdaptParties import AdaptParties
from tests.utils.build_party import build_all_parties, construct_all_parties_json

class AdaptPartiesTest(unittest.TestCase):

    def test_all_parties_all_years_to_json(self):
        adaptParties = AdaptParties()
        parties = build_all_parties()
        
        json = adaptParties.to_json(parties)

        json_expected = construct_all_parties_json(parties)

        self.assertEqual(json, json_expected)