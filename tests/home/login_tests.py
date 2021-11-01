import pytest
from selenium import webdriver

import time
#from pages.home.login_page_version_1 import LoginPage    # This is a class we made up to deal with log ins
from pages.home.login_page import LoginPage
import unittest
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        # we dont need to do logout here because this set of tests will do valid logins
        self.lp.login("andymc147@yahoo.com", "lkiBl00mers$$00")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Validating Title")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.mark(result2, "Testing an element existed on the page")
        # I like to do the Final test by itself just so it is cleaner
        self.ts.markFinal("test_validLogin")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()   # need to do this the first time because we need to be on a screen where we can log in
                            # because the setUp stuff is gonna log us in - so need to log back out here because this is
                            # the first test we will run after setup
        self.lp.login("test@email.com", "abcabcxxx")
        result = self.lp.verifyLoginFailed()
        self.ts.mark(result, "Testing invalid password")
        self.ts.markFinal("test_invalidLogin")
        assert result == True          # if we didn't log in successfully nothing happens because we are expecting the error message




# krome = LoginTests()
# krome.test_validLogin()
