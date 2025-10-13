from domain.Election import Election
from tests.utils.build_district import build_first_district, build_second_district, build_third_district, construct_districts_json

def build_one_election():
    election = Election()
    election.year = 2022
    election.Districts.append(build_first_district())
    election.Districts.append(build_third_district())
    election.Districts.append(build_second_district())
    return election

def construct_election_json(election):
    districts_json = construct_districts_json(election.Districts)
    json = "\"year\":{year}, {districts}".format(year = election.year, districts = districts_json)
    json_final  = "{"+json+"}"
    return json_final