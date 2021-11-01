
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from pages.home.login_page_version_1 import LoginPage    # This is a class we made up to deal with log ins
from pages.home.login_page import LoginPage
import unittest
import pytest


class LoginTests(unittest.TestCase):

    baseurl = "https://courses.letskodeit.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseurl)
    loginpg = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.loginpg.login("test@email.com", "abcabc")
        result = self.loginpg.verifyLoginSuccessful()

        assert result == True          # if we logged in successfully nothing happens but if not then it throws errors
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseurl)
        self.loginpg.login("test@email.com", "abcabcxxx")
        time.sleep(2)
        result = self.loginpg.verifyLoginFailed()

        assert result == True          # if we didn't log in successfully nothing happens because we are expecting the error message




# krome = LoginTests()
# krome.test_validLogin()
