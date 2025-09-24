#TODO 
# 1 - je fais marcher l'assert de ces parties pour un candidat 
# 2 - avec tous les candidats d'un district
# 3 - tous les résultats
#1	Ain	101	1ère circonscription	86843	61830	71,20%	25013	28,80%	60495	69,66%	97,84%	929	1,07%	1,50%	406	0,47%	0,66% LR	BRETON	Xavier	MASCULIN	14495	16,69%	23,96%
def AssertCustom(datas, resultDistrict, unitTest):
    data = datas.split('|')
    unitTest.assertEqual(data[2], str(resultDistrict.District.number))
    unitTest.assertEqual(data[3], resultDistrict.District.label)
    unitTest.assertEqual(data[4], str(resultDistrict.District.registered))
    unitTest.assertEqual(data[5], str(resultDistrict.District.voting))
    pass