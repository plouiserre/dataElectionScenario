def CleanLineExcel(str_excel):
    data = str_excel
    data = __delete_square_bracket(data)
    data = __replace_forbidden_words(data)
    datas = __separate_str(data)
    datas = __clean_percentage(datas)
    datas = __reput_forbidden_words(datas)
    return datas

def __replace_forbidden_words(data):
    data = data.replace('Côte-d\'Or', "CôtedOr")    
    data = data.replace('Côtes-d\'Armor', "CôtesdArmor")    
    data = data.replace('Val-d\'Oise', "ValdOise")    
    return data

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


def __reput_forbidden_words(datas):
    datas_with_forbidden_words = []
    for data in datas:
        data = data.replace('CôtedOr', 'Côte-d\'Or')    
        data = data.replace('CôtesdArmor', 'Côtes-d\'Armor')   
        data = data.replace('ValdOise', 'Val-d\'Oise')    
        datas_with_forbidden_words.append(data)
    return datas_with_forbidden_words