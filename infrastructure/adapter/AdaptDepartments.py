from infrastructure.adapter.AdaptDepartment import AdaptDepartment

class AdaptDepartments(): 
    def __init__(self):
        self.departments_json = '' 
        self.departments = []       

    def to_json(self, departments):
        self.departments = departments
        self.departments = self.__delete_duplicate()
        self.departments_json += "\"departments\":["
        for i, department in enumerate(self.departments):
            adapt_department = AdaptDepartment()
            json_department = adapt_department.to_json(department)
            if(i == len(self.departments) - 1):
                self.departments_json += json_department
            else :                 
                self.departments_json += json_department + ','
        self.departments_json += "]"
        return self.departments_json

    def __delete_duplicate(self):
        departments_no_duplicates = []
        for department in self.departments:            
            is_duplicate = False
            if len(departments_no_duplicates) == 0:
                departments_no_duplicates.append(department)
                continue 
            for save in departments_no_duplicates: 
                if department.code == save.code : 
                    is_duplicate = True
                    break
            if is_duplicate == False :
                departments_no_duplicates.append(department)
        return departments_no_duplicates