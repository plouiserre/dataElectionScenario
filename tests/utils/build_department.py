from domain.Department import Department

def build_departments():
    first_department =  build_first_department()
    second_department = build_second_department()
    departments = []
    departments.append(first_department)
    departments.append(second_department)
    return departments     

def build_first_department():
    first_department = __construct_department('33', 'Gironde')
    return first_department


def build_second_department():
    second_department = __construct_department('75', 'Paris')
    return second_department


def __construct_department(code, name):
        department = Department()
        department.code = code
        department.name = name
        return department 

def construct_departments_json(departments):
    first_department_json = construct_department_json(departments[0])
    second_department_json = construct_department_json(departments[1])
    departments_json_concat = "\"departments\":[{first_department},{second_department}]".format(
        first_department = first_department_json, second_department = second_department_json
    )
    return departments_json_concat

def construct_department_json(department):
    json_department = "\"name\":\"{name}\",\"code\":\"{code}\"".format(
        name = department.name, code = department.code
    )
    json_final = "{"+json_department+"}"      
    return json_final
