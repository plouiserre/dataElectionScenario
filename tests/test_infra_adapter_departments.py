import unittest
from infrastructure.adapter.AdaptDepartments import AdaptDepartments
from tests.utils.assertCustom import AssertDepartment
from tests.utils.build_department import build_first_department, build_second_department, construct_departments_json

class AdaptDepartmentTest(unittest.TestCase):
    def test_departments_to_json(self):
        adaptDepartments = AdaptDepartments()
        departments = self.__build_departments()

        json = adaptDepartments.to_json(departments)

        departments_expected = self.__build_expected_department()
        json_expected = construct_departments_json(departments_expected)

        self.assertEqual(json, json_expected)


    def __build_departments(self):
        first_department = build_first_department()
        second_department = build_second_department()
        departments = [first_department, second_department, second_department, first_department]
        return departments
    
    def __build_expected_department(self):
        first_department = build_first_department()
        second_department = build_second_department()
        departments = [first_department, second_department]
        return departments
