"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()

"""


from selenium import webdriver
import traceback

# following imports I added to handle my logging messsages
import logging
import utilities.custom_logger as cl
import time
import inspect


class WebDriverFactory():

    log = cl.customLogger(logging.DEBUG)
    myclass = "WebDriverFactory"

    def __init__(self, browser):
        """
        Inits WebDriverFactory class
        :param browser:

        Returns:
            None
        """

        self.browser = browser
        """
        Set chrome and iexplorer and edge driver based on os
        
        chromedriver = "C:\\...\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        
        PREFERRED: Set the path on the machine where browser will be executed
        """

    def getWebDriverInstance(self):
        """
        Get WebDriver instance based on the browser configuration

        :return:
            'WebDriver Instance'
        """

        defaultBrowser = False

        self.log.info("***************************************************************************************")
        # baseurl = "https://courses.letskodeit.com/"
        baseurl = "https://www.letskodeit.com/"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "edge":
            driver = webdriver.Edge()
        elif self.browser == "safari":
            driver = webdriver.Safari()
        else:
            defaultBrowser = True
            driver = webdriver.Firefox()

        if not defaultBrowser:
            self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": using browser " + self.browser)
        else:
            self.log.warning(self.myclass + ": " + inspect.stack()[0][3] + ": browser " + self.browser + " is unsupported - using Firefox instead")

        # maximize window
        driver.maximize_window()
        # Setting driver Implicit Timeout for an Element
        driver.implicitly_wait(3)
        # Loading browser with App URL
        driver.get(baseurl)

        return driver


