from tests.utils.build_candidate import build_first_candidate, build_second_candidate, build_third_candidate, build_fourth_candidate, build_fifth_candidate, build_sixth_candidate, build_seventh_candidate, construct_candidate_json
from domain.District import District

def builds_three_districts():
    first_district = build_first_district()
    
    second_district = build_second_district()

    third_district = build_third_district()

    districts = []
    districts.append(first_district)
    districts.append(second_district)
    districts.append(third_district)
    return districts

def build_first_district():
    first_candidate_first_district = build_first_candidate()
    second_candidate_first_district = build_second_candidate()
    third_candidate_first_district = build_third_candidate()
    first_district = __construct_district('2ème circonscription', '2902', '29', '78185', '55066', first_candidate_first_district, 
                                                   second_candidate_first_district, third_candidate_first_district)
    return first_district

def build_second_district():
    first_candidate_second_district = build_fourth_candidate()
    second_candidate_second_district = build_fifth_candidate()
    second_district = __construct_district('6ème circonscription', '4506',  '45', '76104', '52335', first_candidate_second_district, 
                                                    second_candidate_second_district, None)
    return second_district


def build_third_district():
    first_candidate_third_district = build_sixth_candidate()
    second_candidate_third_district = build_seventh_candidate()
    third_district = __construct_district('6ème circonscription', '6706', '67', '98281', '67852', first_candidate_third_district,
                                                second_candidate_third_district, None)
    return third_district

def __construct_district(label, number, department_code, registered, voting, first_candidate, second_candidate, third_candidate): 
        district = District()
        district.label = label
        district.number = number
        district.department_code = department_code
        district.registered = registered
        district.voting = voting
        district.candidates.append(first_candidate)
        district.candidates.append(second_candidate)
        if third_candidate != None : 
            district.candidates.append(third_candidate)
        return district

def construct_districts_json(districts):
        first_district_json = construct_district_json(districts[0])
        if len(districts) > 1 :
            second_district_json = construct_district_json(districts[1])
            if len(districts) == 3:
                three_district_json = construct_district_json(districts[2])
                districts_json_concat = "\"districts\":[{first_district_json},{second_district_json},{three_district_json}]".format(
                        first_district_json = first_district_json, second_district_json = second_district_json,
                        three_district_json = three_district_json
                    )
                return districts_json_concat
            else :
                districts_json_concat = "\"districts\":[{first_district_json},{second_district_json}]".format(
                        first_district_json = first_district_json, second_district_json = second_district_json
                    )
                return districts_json_concat
        else :
            districts_json_concat = "\"districts\":[{first_district_json}]".format(
                    first_district_json = first_district_json
                )
            return districts_json_concat

def construct_district_json(district):
        candidates = ''
        district_json = __construct_district_without_candidates(district)
        first_candidate_json = construct_candidate_json(district.candidates[0])
        second_candidate_json = construct_candidate_json(district.candidates[1])
        if len(district.candidates) == 3 :
            three_candidate_json = construct_candidate_json(district.candidates[2])
            candidates = "\"candidates\":[{first_candidate_json},{second_candidate_json},{three_candidate_json}]".format(
                    first_candidate_json = first_candidate_json, second_candidate_json = second_candidate_json,
                    three_candidate_json = three_candidate_json
                )
        else :
            candidates = "\"candidates\":[{first_candidate_json},{second_candidate_json}]".format(
                    first_candidate_json = first_candidate_json, second_candidate_json = second_candidate_json
                )
        district_concat = "{district}, {candidates}".format(district = district_json, candidates = candidates )
        final_district = district_concat+"}"
        return final_district
    
def __construct_district_without_candidates(district):
        json_district = "\"label\":\"{label}\",\"number\":\"{number}\", \"department code\":\"{departmentCode}\", " \
        "\"registered\":{registered},\"voting\":{voting} ".format(
            label = district.label, number = district.number, departmentCode = district.department_code,
            registered = district.registered, voting = district.voting)
        json_final = "{"+json_district
        return json_final