from domain.Department import Department
from infrastructure.factory.FormatExcelDataFactory import FormatExcelDataFactory

class AdaptDepartment():
    def __init__(self):
        self.format_excel_factory = FormatExcelDataFactory()
        pass

    def Transform(self, datas, key):
        excel_format = self.format_excel_factory.get_format_excel_data(key)
        self.datas = excel_format.format(datas)
        department  = Department()
        department.code = self.datas[0]
        department.name = self.datas[1]
        return department
    
    def to_json(self, department):
        json_department = "\"name\":\"{name}\",\"code\":\"{code}\"".format(
            name = department.name, code = department.code
        )
        json_final = "{"+json_department+"}"      
        return json_final    