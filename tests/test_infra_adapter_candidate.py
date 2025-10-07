import unittest
from utils.build_candidate import build_eighth_candidate, construct_candidate_json
from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from tests.utils.assertCustom import AssertCandidateResult

class AdaptCandidateTest(unittest.TestCase):
    def test_candidate_is_build(self):
        adaptCandidate = AdaptCandidate()

        candidate = adaptCandidate.Transform(['ENS','BOUDIÉ','Florent','MASCULIN',28960,'34.63','52.17','élu'])

        AssertCandidateResult("ENS|BOUDIÉ|Florent|MASCULIN|28960|34.63|52.17", candidate, self)


    def test_candidate_to_json(self):
        adaptCandidate = AdaptCandidate()
        candidate = build_eighth_candidate()

        json = adaptCandidate.to_json(candidate)

        json_expected = construct_candidate_json(candidate)

        self.assertEqual(json, json_expected)
        
        