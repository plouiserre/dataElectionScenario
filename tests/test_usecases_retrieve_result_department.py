import unittest
from tests.utils.assertCustom import AssertDepartment
from usecases.AdaptResultElectionData.RetrieveResultDepartment import RetrieveResultDepartment

class UsecasesRetrieveResultDepartmentTest(unittest.TestCase):
    def test_departments_are_finded(self):
        retrieveResultDepartment = RetrieveResultDepartment()

        resultDepartments = retrieveResultDepartment.Search()

        AssertDepartment('1|Ain', resultDepartments.Departments[0], self)
        AssertDepartment('13|Bouches-du-Rhône', resultDepartments.Departments[1], self)
        AssertDepartment('31|Haute-Garonne', resultDepartments.Departments[2], self)
        AssertDepartment('33|Gironde', resultDepartments.Departments[3], self)