from traceback import print_stack

# following imports I added to handle my logging messsages
import logging
import utilities.custom_logger as cl
import time
import inspect
from base.selenium_driver import SeleniumDriver

class TestStatus(SeleniumDriver):

    myclass = "TestStatus"
    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        :param driver:
        """
        super(TestStatus, self).__init__(driver)
        self.resultList = []

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:           # Testing for True
                    self.resultList.append("PASS")
                    self.log.info(self.myclass + ": " + inspect.stack()[0][3] + " " +
                                  "### VERIFICATION SUCCESSFUL :: + " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.warning(self.myclass + ": " + inspect.stack()[0][3] + " " +
                                  "### VERIFICATION FAILED :: + " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error(self.myclass + ": " + inspect.stack()[0][3] + " " +
                               "### VERIFICATION FAILED :: + " + resultMessage)
                self.screenShot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error(self.myclass + ": " + inspect.stack()[0][3] + " " +
                          "### EXCEPTION OCCURRED !!! :: + " + resultMessage)
            self.screenShot(resultMessage)
            print_stack()


    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        :param testName:
        :param result:
        :param resultMessage:
        :return:
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        :param testName:
        :param result:
        :param resultMessage:
        :return:
        """
        # self.setResult(result, resultMessage)

        """
        The following code is gonna look at the list we made from each of the mark calls
        And check to see if any of them contain FAIL
        If so then the test will get marked as a failure
        """
        if "FAIL" in self.resultList:
            self.log.error(self.myclass + ": " + inspect.stack()[0][3] + " " +
                           testName + " ### TEST FAILED !!!" )
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(self.myclass + ": " + inspect.stack()[0][3] + " " +
                           testName + " ### TEST SUCCESSFUL !!!")
            self.resultList.clear()
            assert True == True



