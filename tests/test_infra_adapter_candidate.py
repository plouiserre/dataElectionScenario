import unittest
from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from tests.utils.assertCustom import AssertCandidateResult

class AdaptCandidateTest(unittest.TestCase):
    def test_candidate_is_build(self):
        adaptCandidate = AdaptCandidate()

        candidate = adaptCandidate.Transform(['ENS','BOUDIÉ','Florent','MASCULIN',28960,'34.63','52.17','élu'])

        AssertCandidateResult("ENS|BOUDIÉ|Florent|MASCULIN|28960|34.63|52.17", candidate, self)