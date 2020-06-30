import configparser,xlrd

def getDataFromIni(file):
    '''
    从x.ini 文件中读取数据，返回字典格式
    get data from x.ini
    :param file:
    :return:
    '''
    config = configparser.ConfigParser()
    config.read(file)
    d = dict(config._sections)
    for k in d.keys():
        d[k] = dict(d[k])
    return d

def getDataFromProperties(file):
    '''
    从x.properties 文件中读取数据，返回字典格式
    get data from x.propertie file
    :param file:
    :return: dict
    '''
    data = {}
    with open(file,'r',encoding='UTF-8') as fb:
        lines = fb.readlines()
        for line in lines:
            line = line.strip()
            key = line.split('=')[0]
            value = line.split('=')[1]
            if key not in  data.keys():
                data[key] =value
    return data

def getDataFromExcel(file):
    '''
    从x.xlsx或x.xls 文件中读取数据，返回字典格式
    read test data from x.xlsx or x.xls
    :param file: Excel file path
    :param pageMark:sheet index or name
    :return: dict
    '''

    data = {}
    table = xlrd.open_workbook(file)
    names = table.sheet_names()
    for name in names :
        sheet = table.sheet_by_name(name)
        d = {}
        for i in range(sheet.nrows):
            k = sheet.cell_value(i,0)
            if k not in d.keys():
                v = sheet.cell_value(i,1)
                # if

                d[k] = v
        data[name] = d
    return data

def writeDataInExcel(data,file):
    '''
    将字典写入Excel文件
    :param data:
    :return:
    '''
    table = xlwt.Workbook(encoding='utf-8')
    for sheetName in data.keys():
        sheet  = table.add_sheet(sheetname=sheetName)
        row_nummber = 0
        for row_header in data.get(sheetName).keys():
            row_value = data.get(sheetName).get(row_header)
            sheet.write(row_nummber, 0, row_header)
            if 'str'in str(type(row_value))and  len(row_value)!=0:
                sheet.write(row_nummber, 1, row_value)
            elif 'list'in str(type(row_value)) and  len(row_value)!=0:
                col_number =1
                for i in row_value:
                    sheet.write(row_nummber, col_number, row_value)
                    col_number+=1
            row_nummber += 1
    table.save(file)