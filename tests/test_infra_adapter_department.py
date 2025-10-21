import unittest
from infrastructure.adapter.AdaptDepartment import AdaptDepartment
from tests.utils.assertCustom import assertDepartment
from tests.utils.build_department import build_first_department, construct_department_json

class AdaptDepartmentTest(unittest.TestCase):
    def test_department_is_build(self):
        adaptDepartment = AdaptDepartment()

        department = adaptDepartment.transform("['33' 'Gironde' 3310 '10ème circonscription' 83620 58727 '70,23%' 24893 '29,77%' 55515 '66,39%' '94,53%' 2365 '2,83%' '4,03%' 847 '1,01%' '1,44%' 2 'ENS' 'BOUDIÉ' 'Florent' 'MASCULIN' 28960 '34,63%' '52,17%' 'élu' '4.0' 'RN' 'CHADOURNE' 'Sandrine' 'FEMININ' '26555' '31,76%' '47,83%' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan' 'nan']", 2024)        

        assertDepartment('33|Gironde', department, self)
        

    def test_department_to_json(self):
        adaptDepartment = AdaptDepartment()
        department = build_first_department()

        json = adaptDepartment.to_json(department)

        json_expected = construct_department_json(department)

        self.assertEqual(json, json_expected)