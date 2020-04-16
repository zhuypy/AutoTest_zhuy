import framework.driver.htmlTool
from framework.driver.driver import DR
from framework.logger.logger import *
import framework.tool.dataUtils
import os
class JcwCase():
    '''
    excution steps :
        1>envInit
            a>initParam
            b>initBrowser
        2>excuteTest
            a>custom_step
        3>envRecovery
            # a>DR.quit()  # do not excute this step in a single use case
    '''

    def initParam(self):
        self.className = str(self.__class__.__name__)
        # self.data_path = DATA_PATH + '\\' +self.className +'.xlsx'
        self.data_path =findFileinDir(self.className +'.xlsx',DATA_PATH)
        
        self.report_path = REPORT_PATH
        self.picture_path = self.report_path + '\\' + self.className
        if not os.path.exists(self.picture_path):
            os.makedirs(self.picture_path)
        self.log_path = self.picture_path
        self.log_file = self.log_path+'\\' + self.className+'.log'
        self.data = getDataFromExcel(self.data_path)

        if os.path.isfile(self.log_file):
            os.remove(self.log_file)

        logger.setLogFileLocation(self.log_file)
        logger.mark('envInit START ,time is %s'%(getCurrentTime()))
        logger.mark('initParam START')
        logger.info('className is :%s'%self.className)
        logger.info('report_path is :%s'%self.report_path)
        logger.info('picture_path is :%s'%self.picture_path)
        logger.info('log_path is :%s'%self.log_path)
        logger.info('log_file is :%s'%self.log_file)
        logger.info('test data is %s'%(self.data))
        logger.mark('initParam END')

    def initBrowser(self):
        logger.mark('initBrowser START')
        DR.get(LOGIN_ADDRESS)
        logger.mark('initBrowser END')

    def envInit(self):
        self.initParam()
        self.initBrowser()
        self.custom_setUp()
        logger.mark('envInit END')
        
    def executeTest(self):
        logger.mark('executeTest START')
        try:
            result = self.custom_step()
            if not result:
                self.screenshot()
                logger.mark(logger.NG)
            else:
                logger.mark(logger.OK)
            self.assertEqual(result, True)
        except Exception as e:
            logger.error(e)
            logger.mark(logger.NG)
            self.screenshot()
            raise e
        logger.mark('executeTest END')

    def custom_setUp(self):
        pass

    def custom_step(self):
        '''
        must ne rewritten
        :return:
        '''
        pass

    def custom_tearDown(self):
        pass

    def envRecovery(self):
        logger.mark('envRecovery START')
        self.custom_tearDown()
        logger.mark('envRecovery END')

    def screenshot(self):
        currentTime = getCurrentTime()
        picture_file = os.path.join(self.picture_path,self.className + '_' + currentTime + '.png')
        framework.driver.htmlTool.screenshot(picture_file)

    def get_page(self,url):
        DR.get(url)


