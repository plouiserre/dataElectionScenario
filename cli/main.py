import pandas as pd


def transform_excel_datas(excel_data) : 
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


print("lecture données")
data = pd.read_excel("C:/Users/ploui/Projects/dataElectionScenario/openDatas/resultats-definitifs-par-circonscription.xlsx")
for excel_data in enumerate(data.values) :
    dataWorked = transform_excel_datas(excel_data[1])
    print(dataWorked)
print("fin lecture")



#packages à installer 
#wheel 
#pandas 
#openpyxl