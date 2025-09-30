def AssertDistrictResult(datas, district, unitTest):
    data = datas.split('|')
    unitTest.assertEqual(data[2], str(district.number))
    unitTest.assertEqual(data[3], district.label)
    unitTest.assertEqual(data[4], str(district.registered))
    unitTest.assertEqual(data[5], str(district.voting))
    __assertFirstCandidate(data, district.Candidates[0], unitTest)
    __assertSecondCandidate(data, district.Candidates[1], unitTest)

def AssertCandidateResult(datas, candidate, unitTest):
    data = datas.split('|')
    unitTest.assertEqual(data[0], candidate.partiCode)
    unitTest.assertEqual(data[1], candidate.lastName)
    unitTest.assertEqual(data[2], candidate.firstName)
    unitTest.assertEqual(data[3], candidate.sexe)
    unitTest.assertEqual(data[4], str(candidate.vote))
    unitTest.assertEqual(data[5], candidate.voteByRegistered)
    unitTest.assertEqual(data[6], candidate.voteByExpressed)

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
