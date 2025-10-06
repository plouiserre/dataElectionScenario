import unittest
from domain.Candidate import Candidate
from infrastructure.adapter.AdaptCandidate import AdaptCandidate
from tests.utils.assertCustom import AssertCandidateResult

class AdaptCandidateTest(unittest.TestCase):
    def test_candidate_is_build(self):
        adaptCandidate = AdaptCandidate()

        candidate = adaptCandidate.Transform(['ENS','BOUDIÉ','Florent','MASCULIN',28960,'34.63','52.17','élu'])

        AssertCandidateResult("ENS|BOUDIÉ|Florent|MASCULIN|28960|34.63|52.17", candidate, self)


    def test_candidate_to_json(self):
        adaptCandidate = AdaptCandidate()
        candidate = self.__candidate_build()

        json = adaptCandidate.to_json(candidate)

        json_candidate = "\"lastName\":\"{lastName}\",\"firstName\":\"{firstName}\", \"sexe\":\"{sexe}\",\"partiCode\":\"{partiCode}\",\"vote\":{vote},\"voteByRegistered\":\"{voteByRegistered}\",\"voteByExpressed\":\"{voteByExpressed}\" ".format(
            lastName = candidate.lastName, firstName = candidate.firstName, sexe = candidate.sexe, partiCode = candidate.partiCode, 
            vote = candidate.vote, voteByRegistered = candidate.voteByRegistered, voteByExpressed = candidate.voteByExpressed
        )

        json_expected = "{"+json_candidate+"}"

        self.assertEqual(json, json_expected)



    def __candidate_build(self): 
        candidate = Candidate()
        candidate.partiCode = 'ENS'
        candidate.lastName = 'BOUDIÉ'
        candidate.firstName = 'Florent'
        candidate.sexe = 'MASCULIN'
        candidate.vote = '28960'
        candidate.voteByRegistered = '34.63%'
        candidate.voteByExpressed = '52.17%'
        return candidate
        
        