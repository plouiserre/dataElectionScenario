def CleanLineExcel(str_excel):
    data = str_excel
    data = __delete_square_bracket(data)
    datas = __separate_str(data)
    datas = __clean_percentage(datas)
    return datas


def __delete_square_bracket(str_excel):
    data = str_excel
    data = data.replace('[', '')
    data = data.replace(']', '')
    return data


def __separate_str(str_excel):
    results = []
    is_apostrophe = False
    is_space = False
    str_element = ''
    for caracter in str_excel : 
        if caracter == '\'' and is_apostrophe == False:
            is_apostrophe = True
        elif caracter == '\'' and is_apostrophe == True:
            is_apostrophe = False      
            if str_element != '':
                if(str_element != 'nan'):
                    results.append(str_element)
                str_element = ''
        elif caracter == ' ' and is_space == False:
            is_space = True
        elif caracter == ' ' and is_space and is_apostrophe == False:            
            if str_element != '':
                if(str_element != 'nan'):
                    results.append(str_element)
                str_element = ''   
        else :
            str_element += caracter
    return results

def __clean_percentage(datas):
    datas_cleaned = []
    for data in datas : 
        data = __update_percentage(data)
        datas_cleaned.append(data)
    return datas_cleaned

def __update_percentage(data) : 
    data_cleaned = data
    if '%' in data : 
        data_cleaned = data.replace(',','.')
    return data_cleaned
# def __separate_str(str_excel):
#     pass