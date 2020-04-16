
def compareDict(dict1,dict2,keyword = None):
    '''
    比较两个dict1和dict2中的是否有冲突值
    keyword为必校验项，若交集中不包含keyword项，则校验失败
    返回值0：无冲突项，公共key获取的值完全一致，同步返回交集
    返回值1：无冲突项，公共key获取的值存在包含关系，同步返回交集，以包含者的值为准
    返回值-1：有冲突项，公共key获取的值不一致，返回冲突集合，格式为{'expect':值1,'actual':值2}
    返回值-2：无冲突项，但交集中没有keyword，不返回集合
    :param dict1:
    :param dict2:
    :param keyword:the necessary element, if not in sanmeDict,fails to determine the comparison
    :return:result_code: -1,0,1 ,samedict:intersection of two dictionaries
    '''
    dictSame = {}
    ret = 0
    for key in dict1.keys():
        if key in dict2.keys():
            if dict1.get(key) == dict2.get(key):
                dictSame[key] = dict1.get(key)
                continue
            elif dict1.get(key) in dict2.get(key):
                dictSame[key] = dict2.get(key)
                ret = 1
                continue
            elif dict2.get(key) in dict1.get(key):
                dictSame[key] = dict1.get(key)
                ret = 1
                continue
            else:
                return -1,{'expect':dict1.get(key),'actual':dict2.get(key)}
        else:
            continue
    if keyword and (keyword not in dictSame.keys()):
        return -2,None
    return ret,dictSame


def convertDict(dict,rule):
    '''
    将dict中的key值转换，rule为转换规则
    例：dict = {a:1,b:2},rule = {a:A,b:B},则该方法返回{A:1,,B:2}
    :param dict:
    :param rule:
    :return:
    '''
    ret_dict = {}
    for key in dict.keys():
        if key in rule.keys():
            ret_dict[rule.get(key)] = dict.get(key)
    return ret_dict





