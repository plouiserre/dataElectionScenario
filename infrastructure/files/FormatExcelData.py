class FormatExcelData : 
    def __init__(self):
        self.datas = []

    def format(self, text):
        pass

    def _replace_complexe_words(self, data):
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
        data = data.replace('D\'ANGIO','DANGIO')  
        data = data.replace('D\'AMILLY','DAMILLY')  
        data = data.replace('BASTIDE D\'IZARD','BASTIDE DIZARD')
        data = data.replace('D\'AUBIGNAN', 'DAUBIGNAN')       
        data = data.replace('PROD\'HOMME', 'PRODHOMME')                  
        data = data.replace('D\'ISOARD DE CHENERILLES', 'DISOARD DE CHENERILLES')
        data = data.replace('D\'HONT', 'DHONT')
        data = data.replace('Cindy\'Lee', 'CindyLee')   
        data = data.replace('L\'AMINOT', 'LAMINOT')   
        data = data.replace('N\'DONG', 'NDONG')   
        data = data.replace('BEN M\'BAREK', 'BEN MBAREK')
        return data

    def _delete_square_bracket(self, str_excel):
        data = str_excel
        data = data.replace('[', '')
        data = data.replace(']', '')
        return data


    def _separate_str(self, str_excel):
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

    #TODO put in 2024 format!!!!
    def _clean_percentage(self, datas):
        datas_cleaned = []
        for data in datas : 
            data = self.__update_percentage(data)
            datas_cleaned.append(data)
        return datas_cleaned

    def __update_percentage(self, data) : 
        data_cleaned = data
        if '%' in data : 
            data_cleaned = data.replace(',','.')
        return data_cleaned


    def _reput_forbidden_words(self, datas):
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
            data = data.replace('DANGIO', 'D\'ANGIO')
            data = data.replace('DAMILLY', 'D\'AMILLY')  
            data = data.replace('BASTIDE DIZARD', 'BASTIDE D\'IZARD')
            data = data.replace('DAUBIGNAN', 'D\'AUBIGNAN')       
            data = data.replace('PRODHOMME', 'PROD\'HOMME')                  
            data = data.replace('DISOARD DE CHENERILLES', 'D\'ISOARD DE CHENERILLES')
            data = data.replace('DHONT', 'D\'HONT')
            data = data.replace('CindyLee', 'Cindy\'Lee')   
            data = data.replace('LAMINOT', 'L\'AMINOT')   
            data = data.replace('NDONG', 'N\'DONG')   
            data = data.replace('BEN MBAREK', 'BEN M\'BAREK')
            datas_with_forbidden_words.append(data)
        return datas_with_forbidden_words
