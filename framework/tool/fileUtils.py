import os

def findFileinDir(file_name,dir):
    '''
    遍历文件夹及其子文件夹检索文件，检索成功返回文件完整路径，检索失败返回None
    :param file_name:
    :param dir:
    :return:
    '''
    if not os.path.isfile(os.path.join(dir,file_name)):
        for subFile in os.listdir(dir):
            if os.path.isdir(os.path.join(dir,subFile)) and findFileinDir(file_name,os.path.join(dir,subFile)):
                return findFileinDir(file_name,os.path.join(dir,subFile))
    else:
        return os.path.join(dir,file_name)
    return None

def findAllSubFile(dir):
    '''
    遍历检索文件夹中所有文件，以及子文件夹中的文件，不包含子文件夹，返回文件列表list
    :param dir:
    :return:
    '''
    fileList = []
    for subFile in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, subFile)):
            fileList.append(os.path.join(dir, subFile))
        else:
            subFileList = findAllSubFile(os.path.join(dir, subFile))
            fileList += subFileList
    return fileList