def AssertDistrictWithTwoCandidates(datas, district, unitTest):
    data = datas.split('|')
    __assertDistrictResult(data, district, unitTest)
    __assertFirstCandidate(data, district.Candidates[0], unitTest)
    __assertSecondCandidate(data, district.Candidates[1], unitTest)


def __assertDistrictResult(data, district, unitTest):
    unitTest.assertEqual(data[0], str(district.department_code))
    unitTest.assertEqual(data[2], str(district.number))
    unitTest.assertEqual(data[3], district.label)
    unitTest.assertEqual(data[4], str(district.registered))
    unitTest.assertEqual(data[5], str(district.voting))
    
def AssertCandidateResult(datas, candidate, unitTest):
    data = datas.split('|')
    __assertCandidate(data, 0, candidate, unitTest)

def __assertFirstCandidate(data, candidate, unitTest):
    __assertCandidate(data, 18, candidate, unitTest)

def __assertSecondCandidate(data, candidate, unitTest):
    __assertCandidate(data, 25, candidate, unitTest)

def __assertCandidate(data, index, candidate, unitTest):
    unitTest.assertEqual(data[index], candidate.parti_code)
    unitTest.assertEqual(data[index + 1], candidate.last_name)
    unitTest.assertEqual(data[index + 2], candidate.first_name)
    unitTest.assertEqual(data[index + 3], candidate.sexe)
    unitTest.assertEqual(data[index + 4], str(candidate.vote))
    unitTest.assertEqual(data[index + 5], str(candidate.vote_registered))
    unitTest.assertEqual(data[index + 6], str(candidate.vote_expressed))


def AssertDepartment(datas, department, unitTest):
    data = datas.split('|')
    unitTest.assertEqual(data[0], str(department.code))
    unitTest.assertEqual(data[1], department.name)

def AssertParties(datas, resultParties, unitTest):
    data = datas.split('|')
    __assertParty(data, 0, resultParties[0], unitTest)
    __assertParty(data, 2, resultParties[1], unitTest)
    __assertParty(data, 4, resultParties[2], unitTest)
    __assertParty(data, 6, resultParties[3], unitTest)
    __assertParty(data, 8, resultParties[4], unitTest)


def AssertParty(datas, resultParti, unitTest):
    data = datas.split('|')
    __assertParty(data, 0, resultParti, unitTest)


def __assertParty(data, index, resultParti, unitTest):
    unitTest.assertEqual(data[index], resultParti.code)
    unitTest.assertEqual(data[index+1], resultParti.name)
