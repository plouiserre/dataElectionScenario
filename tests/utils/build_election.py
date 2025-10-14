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

def construct_elections_json(elections):
    first_election_json = construct_election_json(elections[0])
    second_election_json = construct_election_json(elections[1])
    elections_json_concat = "\"elections\":[{first_election_json},{second_election_json}]".format(
        first_election_json = first_election_json, second_election_json = second_election_json
    )
    return elections_json_concat