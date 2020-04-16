import HTMLTestRunner
import os
import traceback
from framework.logger.logger import logger
class Exexutor():
    '''
    unittest-based test suite executor
    '''

    def __init__(self):
        self.case_path = None
        self.discover = None
        self.report_file = None
        self.report_title = None
        self.report_description = None

    def setDiscover(self):
        '''
        selecting case sets
        user-defined selection method
        :return:
        '''
        pass

    def setReportPath(self):
        '''
        user-defined test report file path
        :return:
        '''
        pass

    def executeSuite(self):
        '''
        execution test suite
        :return:0
        '''

        try:
            self.setDiscover()
            self.setReportPath()
            if os.path.exists(self.report_file):
                os.remove(self.report_file)

            with open(self.report_file, 'wb') as fb:
                runner = HTMLTestRunner.HTMLTestRunner(stream=fb,
                                                       title=self.report_title,
                                                       description=self.report_description)
                runner.run(self.discover)
        except Exception as e:
            traceback.print_exc()
            logger.error(e)
        finally:
            pass










