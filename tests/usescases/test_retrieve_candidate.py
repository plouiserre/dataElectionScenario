import unittest
from tests.utils.assertCustom import AssertCustom
from usecases.RetrieveResultElectionDistrict import RetrieveResultElectionDistrict

class RetrieveResultElectionDistrictTest(unittest.TestCase):
    def test_candidates_are_finded(self):
        retrieveResultElectionDistrict = RetrieveResultElectionDistrict()
                
        candidates = retrieveResultElectionDistrict.Search()

        #self.assertEqual(10,candidates.len)
        AssertCustom('1|Ain|101|1ère circonscription|86843|61830|71,20%|25013|28,80%|60495|69,66%|97,84%|929|1,07%|1,50%|406|0,47%|0,66%', candidates, self)

        #1	Ain	101	1ère circonscription	86843	61830	71,20%	25013	28,80%	60495	69,66%	97,84%	929	1,07%	1,50%	406	0,47%	0,66% LR	BRETON	Xavier	MASCULIN	14495	16,69%	23,96%
        #24	Dordogne	2404	4ème circonscription	89941	65770	73,13%	24171	26,87%	63216	70,29%	96,12%	1483	1,65%	2,25%	1071	1,19%	1,63% 3	UG	PEYTAVIE	Sébastien	MASCULIN	21801	24,24%	34,49%
        #33	Gironde	3310	10ème circonscription	83589	59039	70,63%	24550	29,37%	57167	68,39%	96,83%	1267	1,52%	2,15%	605	0,72%	1,02% 2	ENS	BOUDIÉ	Florent	MASCULIN	17128	20,49%	29,96%
        #33	Gironde	3311	11ème circonscription	99996	67437	67,44%	32559	32,56%	64855	64,86%	96,17%	1778	1,78%	2,64%	804	0,80%	1,19% 2	RN	DIAZ	Edwige	FEMININ	34590	34,59%	53,33%	élu
        #44	Loire-Atlantique	4401	1ère circonscription	77342	56172	72,63%	21170	27,37%	54798	70,85%	97,55%	1193	1,54%	2,12%	181	0,23%	0,32% 4	EXG	DEFRANCE	Hélène	FEMININ	521	0,67%	0,95%
        #59	Nord	5902	2ème circonscription	87355	57238	65,52%	30117	34,48%	55993	64,10%	97,82%	841	0,96%	1,47%	404	0,46%	0,71%  3	DIV	GUENON	Claire	FEMININ	385	0,44%	0,69%
        #60	Oise	6007	7ème circonscription	77118	49953	64,77%	27165	35,23%	48891	63,40%	97,87%	749	0,97%	1,50%	313	0,41%	0,63% 3	DSV	MONGIRAUD	Thomas	MASCULIN	278	0,36%	0,57%
        #66	Pyrénées-Orientales	6601	1ère circonscription	74058	49093	66,29%	24965	33,71%	47821	64,57%	97,41%	768	1,04%	1,56%	504	0,68%	1,03% 6	REG	DANAT	Delphine	FEMININ	790	1,07%	1,65%
        #75	Paris	7512	12ème circonscription	75515	56860	75,30%	18655	24,70%	56268	74,51%	98,96%	406	0,54%	0,71%	186	0,25%	0,33% 10	ECO	BILLAULT HARLE	Alienor	FEMININ	850	1,13%	1,51%
        #92 Hauts-de-Seine	9210	10ème circonscription	80243	59663	74,35%	20580	25,65%	58553	72,97%	98,14%	1034	1,29%	1,73%	76	0,09%	0,13% 7	ENS	ATTAL	Gabriel	MASCULIN	25675	32,00%	43,85%

    # def test_get_two_elections_datas_from_adapters_list_first_rounds(self, mock_dependency, mock_candidate_adapter, mock_result_district_first_round_adapter) :        
    #     helper = HelperTest()
        
    #     mock_candidate_adapter.extracts_datas_from_files.return_value = helper.get_two_elections_data_model()
    #     mock_result_district_first_round_adapter.extracts_datas_from_files.return_value = helper.get_election_data_from_first_round_adapter_two_candidates()             
    #     mock_dependency.get_dependency.return_value = [mock_candidate_adapter, mock_result_district_first_round_adapter]
        
    #     orchestrate = OrchestrateAdapters(mock_dependency)
        
    #     candidates = orchestrate.get_candidates_datas_from_adapters()
        
    #     first_candidate_all_data = candidates[0]        
    #     second_candidates_all_data = candidates[1]
        
    #     self.assertEqual(2, len(candidates))
        
    #     assert_test = AssertTest(self, 1)
        
    #     result_data_check =[2, "Aisne", 4, "4ème circonscription", "Wednesday", "Addams", datetime.datetime(2002,9,27), "Student", "F", False, 3, 5463213, 12.65, 9.24, "Sinclair", "Enid", "F", datetime.datetime(2002, 4, 2),  False, "Completed", 1, 4654321, 56123, 10.5, 3561234, 95.5, 1234, 30.1, 12.15, 123, 1.01, 0.75, 7456, 0.345, 0.042]
    #     assert_test.assert_result_data_model_with_infos_from_list_first_round(result_data_check, first_candidate_all_data)
        
    #     result_data_check =[59, "Nord", 13, "13ème circonscription", "Thomas", "Shelby", datetime.datetime(1976,5,25), "Gangster", "M", True, 6, 614651432, 37.95, 35.57, "Gray", "Polly", "F", datetime.datetime(1968, 8,17),  True, "Completed", 1, 897465143, 561023, 9.5, 857465143, 75.5, 134, 3.01, 9.15, 103, 0.91, 0.65, 6456, 0.245, 0.032]
    #     assert_test.assert_result_data_model_with_infos_from_list_first_round(result_data_check, second_candidates_all_data)