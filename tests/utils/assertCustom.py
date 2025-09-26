#TODO 
# 1 - je fais marcher l'assert de ces parties pour un candidat 
# 2 - avec tous les candidats d'un district
# 3 - tous les résultats
#4	RN	CHADOURNE	Sandrine	FEMININ	25037	29,95%	43,80%
def AssertDistrictCandidatesResult(datas, resultDistrict, unitTest):
    data = datas.split('|')
    unitTest.assertEqual(data[2], str(resultDistrict.District.number))
    unitTest.assertEqual(data[3], resultDistrict.District.label)
    unitTest.assertEqual(data[4], str(resultDistrict.District.registered))
    unitTest.assertEqual(data[5], str(resultDistrict.District.voting))
    __assertFirstCandidate(data, resultDistrict.Candidates[0], unitTest)
    __assertSecondCandidate(data, resultDistrict.Candidates[1], unitTest)
    __assertThirdCandidate(data, resultDistrict.Candidates[2], unitTest)
    __assertFourthCandidate(data, resultDistrict.Candidates[3], unitTest)

def __assertFirstCandidate(data, candidate, unitTest):
    unitTest.assertEqual(data[18], candidate.partiCode)
    unitTest.assertEqual(data[19], candidate.lastName)
    unitTest.assertEqual(data[20], candidate.firstName)
    unitTest.assertEqual(data[21], candidate.sexe)
    unitTest.assertEqual(data[22], str(candidate.vote))
    unitTest.assertEqual(data[23], str(candidate.voteByRegistered))
    unitTest.assertEqual(data[24], str(candidate.voteByExpressed))

def __assertSecondCandidate(data, candidate, unitTest):
    unitTest.assertEqual(data[25], candidate.partiCode)
    unitTest.assertEqual(data[26], candidate.lastName)
    unitTest.assertEqual(data[27], candidate.firstName)
    unitTest.assertEqual(data[28], candidate.sexe)
    unitTest.assertEqual(data[29], str(candidate.vote))
    unitTest.assertEqual(data[30], str(candidate.voteByRegistered))
    unitTest.assertEqual(data[31], str(candidate.voteByExpressed))

def __assertThirdCandidate(data, candidate, unitTest):
    unitTest.assertEqual(data[32], candidate.partiCode)
    unitTest.assertEqual(data[33], candidate.lastName)
    unitTest.assertEqual(data[34], candidate.firstName)
    unitTest.assertEqual(data[35], candidate.sexe)
    unitTest.assertEqual(data[36], str(candidate.vote))
    unitTest.assertEqual(data[37], str(candidate.voteByRegistered))
    unitTest.assertEqual(data[38], str(candidate.voteByExpressed))

def __assertFourthCandidate(data, candidate, unitTest):
    unitTest.assertEqual(data[39], candidate.partiCode)
    unitTest.assertEqual(data[40], candidate.lastName)
    unitTest.assertEqual(data[41], candidate.firstName)
    unitTest.assertEqual(data[42], candidate.sexe)
    unitTest.assertEqual(data[43], str(candidate.vote))
    unitTest.assertEqual(data[44], str(candidate.voteByRegistered))
    unitTest.assertEqual(data[45], str(candidate.voteByExpressed))


def AssertDepartment(datas, resultDepartment, unitTest):
    data = datas.split('|')
    unitTest.assertEqual(data[0], str(resultDepartment.Departments[0].code))
    unitTest.assertEqual(data[1], resultDepartment.Departments[0].name)
    unitTest.assertEqual(data[2], str(resultDepartment.Departments[1].code))
    unitTest.assertEqual(data[3], resultDepartment.Departments[1].name)
    unitTest.assertEqual(data[4], str(resultDepartment.Departments[2].code))
    unitTest.assertEqual(data[5], resultDepartment.Departments[2].name)
    unitTest.assertEqual(data[6], str(resultDepartment.Departments[3].code))
    unitTest.assertEqual(data[7], resultDepartment.Departments[3].name)

def AssertParties(datas, resultParties, unitTest):
    data = datas.split('|')
    unitTest.assertEqual(data[0], resultParties[0].code)
    unitTest.assertEqual(data[1], resultParties[0].name)
    unitTest.assertEqual(data[2], resultParties[1].code)
    unitTest.assertEqual(data[3], resultParties[1].name)
    unitTest.assertEqual(data[4], resultParties[2].code)
    unitTest.assertEqual(data[5], resultParties[2].name)
    unitTest.assertEqual(data[6], resultParties[3].code)
    unitTest.assertEqual(data[7], resultParties[3].name)
    unitTest.assertEqual(data[8], resultParties[4].code)
    unitTest.assertEqual(data[9], resultParties[4].name)
