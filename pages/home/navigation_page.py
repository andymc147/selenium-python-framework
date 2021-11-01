import time

import logging
import utilities.custom_logger as cl
import inspect
from base.basepage import BasePage

class NavigationPage(BasePage):     # every page will now inherit from SeleniumDriver

    myclass = "NavigationnPage"
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)     # initialize the super class (SeleniumDriver) and pass the driver to it
        self.driver = driver

    # locators  -- putting them here means they only need to be hard coded once then used as often as necessary
    # _login_link = "//a[@href='/login']"
    _my_courses = "MY COURSES"
    _all_courses = "ALL COURSES"
    _practice = "PRACTICE"
    _support = "SUPPORT"
    _home = "HOME"
    _community = "COMMUNITY"
    _user_icon = "//button[@id='dropdownMenu1']"


    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="link")

    def navigateToSupport(self):
        self.elementClick(locator=self._support, locatorType="link")

    def navigateToCommunity(self):
        self.elementClick(locator=self._community, locatorType="link")

    def navigateToUserIcon(self):
        self.elementClick(locator=self._user_icon, locatorType="xpath")

    def navigateToHome(self):
        self.elementClick(locator=self._home, locatorType="link")

