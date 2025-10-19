from infrastructure.adapter.AdaptParty import AdaptParty

class AdaptParties():
    def __init__(self):
        pass

    def to_json(self, parties):
        parties_json = "\"parties\":{"
        count = 0
        for year, parties_year in parties.items():
            parties_json +="\"{year}\":[".format(year = year)
            for i, party in enumerate(parties_year):
                adapt_party = AdaptParty()
                json_party = adapt_party.to_json(party)
                if(i == len(parties_year) - 1):
                    parties_json += json_party
                else :                 
                    parties_json += json_party + ','   
            if count == len(parties) - 1 :
                parties_json += "]"
            else :
                parties_json += "],"
            count += 1
        parties_json += "}"
        return parties_json