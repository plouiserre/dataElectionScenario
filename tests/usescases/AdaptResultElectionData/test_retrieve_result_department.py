import unittest
from tests.utils.assertCustom import AssertDepartment
from usecases.AdaptResultElectionData.RetrieveResultDepartment import RetrieveResultDepartment

class RetrieveResultDepartmentTest(unittest.TestCase):
    def test_departments_are_finded(self):
        retrieveResultDepartment = RetrieveResultDepartment()

        resultDepartments = retrieveResultDepartment.Search()

        AssertDepartment('1|Ain|13|Bouches-du-Rhône|31|Haute-Garonne|33|Gironde', resultDepartments, self)