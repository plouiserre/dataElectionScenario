from domain.Department import Department
from infrastructure.files.CleanStrExcel import CleanLineExcel

class AdaptDepartment():
    def __init__(self):
        pass

    def Transform(self, datas):
        self.datas = CleanLineExcel(datas)
        department  = Department()
        department.code = self.datas[0]
        department.name = self.datas[1]
        return department
    
    def to_json(self, department):
        json_department = "\"name\":\"{name}\",\"code\":{code}".format(
            name = department.name, code = department.code
        )
        json_final = "{"+json_department+"}"      
        return json_final    