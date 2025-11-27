from domain.Party import Party

class AdaptParty():
    def __init__(self):
        pass

    def to_json(self, party):
        json_party = "\"name\":\"{name}\",\"code\":\"{code}\",\"family\":\"{family}\"".format(
            name = party.name, code = party.code, family = party.family
        )
        json_final = "{"+json_party+"}"
        return json_final