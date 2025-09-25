from domain.Department import Department
from domain.ResultDepartment import ResultDepartment
from usecases.Retrieve import Retrieve
class RetrieveResultDepartment(Retrieve):
    def __init__(self):
        super().__init__()

    def Search(self):
        firstDepartment = self.__construct_Department('Ain', 1)
        secondDepartment = self.__construct_Department('Bouches-du-Rhône', 13)
        thirdDepartment = self.__construct_Department('Haute-Garonne', 31)
        fourthDepartment = self.__construct_Department('Gironde', 33)
        departments = []
        departments.append(firstDepartment)
        departments.append(secondDepartment)
        departments.append(thirdDepartment)
        departments.append(fourthDepartment)
        result = ResultDepartment()
        result.Departments = departments
        return result


    def __construct_Department(self, name, number): 
        department = Department()
        department.code = number
        department.name = name
        return department