"""
@oackage base

base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class LoginPage(BasePage)
"""
import logging
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util
###############
import inspect
class BasePage(SeleniumDriver):

    myclass = "BasePage"
    def __init__(self, driver):
        """
        Inits BasePage class

        :param driver:
        :returns:
            None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        return self.verifyPageTitle("bad page title")   # putting in a phony result in order to force a False result
                                                        # normally put in the correct title of course

