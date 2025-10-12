import pandas as pd

class ExcelElection :
    def __init__(self):
        pass

    def Load(self):
        datas = []
        data = pd.read_excel("C:/Users/ploui/Projects/dataElectionScenario/openDatas/2024-circonscriptions.xlsx")
        for excel_data in enumerate(data.values) :
            dataWorked = self.__transform_excel_datas(excel_data[1])
            datas.append(dataWorked)
        return datas
    
    def __transform_excel_datas(self, excel_data) : 
        data_clean = '['
        for i in range(0, len(excel_data)) :
            data = str(excel_data[i])
            is_int_acceptable = data.isdigit() and i != 0
            if i == 0 : 
                if is_int_acceptable : 
                    data_clean += data
                else : 
                    data_clean += "\'"+data+"\'"
            else :
                if is_int_acceptable : 
                    data_clean += " "+data
                else : 
                    data_clean += " \'"+data+"\'"
        data_clean += ']'
        return data_clean
