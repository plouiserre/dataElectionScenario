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
    data = data.replace('Val-d\'Oise', "ValdOise")        
    data = data.replace('MOREL A L\'HUISSIER', "MOREL A LHUISSIER")    
    data = data.replace('PRUD\'HOMME', "PRUDHOMME")    
    data = data.replace('D\'ORSANNE', "DORSANNE")
    data = data.replace('D\'INTORNI', "DINTORNI")
    data = data.replace('D\'ORGEVILLE', "DORGEVILLE")
    data = data.replace('L\'HUILLIER', "LHUILLIER")
    data = data.replace('L\'HOMMEDET', "LHOMMEDET")
    data = data.replace('GUIVARC\'H', 'GUIVARCH')
    data = data.replace('M\'Hamed', 'MHamed')
    data = data.replace('D\'AUTRYVE', 'DAUTRYVE')
    data = data.replace('CUIGNACHE D\'APREVAL', 'CUIGNACHE DAPREVAL')
    data = data.replace('N\'Cho Xavier', 'NCho Xavier')
    data = data.replace('GISCARD D\'ESTAING', 'GISCARD DESTAING')

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
        data = data.replace('MOREL A LHUISSIER', 'MOREL A L\'HUISSIER')    
        data = data.replace('PRUDHOMME','PRUD\'HOMME')
        data = data.replace('DORSANNE', 'D\'ORSANNE') 
        data = data.replace('DINTORNI', 'D\'INTORNI')        
        data = data.replace('DORGEVILLE', 'D\'ORGEVILLE')
        data = data.replace('LHUILLIER', 'L\'HUILLIER')
        data = data.replace('LHOMMEDET', 'L\'HOMMEDET')
        data = data.replace('GUIVARCH', 'GUIVARC\'H')
        data = data.replace('MHamed', 'M\'Hamed')
        data = data.replace('DAUTRYVE', 'D\'AUTRYVE')
        data = data.replace('CUIGNACHE DAPREVAL', 'CUIGNACHE D\'APREVAL')
        data = data.replace('NCho Xavier', 'N\'Cho Xavier')
        data = data.replace('GISCARD DESTAING', 'GISCARD D\'ESTAING')
        datas_with_forbidden_words.append(data)
    return datas_with_forbidden_words