import time

import logging
import utilities.custom_logger as cl
import inspect
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage

class LoginPage(BasePage):     # every page will now inherit from SeleniumDriver

    myclass = "LoginPage"
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)     # initialize the super class (SeleniumDriver) and pass the driver to it
        self.driver = driver
        self.nav = NavigationPage(driver)


    # locators  -- putting them here means they only need to be hard coded once then used as often as necessary
    _login_link2 = "//a[@href='/login']"
    _login_link1 = "//div[@class='ast-button']"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.XPATH, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.XPATH, self._login_button)

    def clickLoginLink(self):
        if self.isElementPresent(locator=self._login_link1, locatorType='xpath'):
            self.elementClick(self._login_link1, locatorType="xpath")
        elif self.isElementPresent(locator=self._login_link2, locatorType='xpath'):
            self.elementClick(self._login_link2, locatorType="xpath")
        else:
            print("In clickLogIn and can't find the link/button for Sign in")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)  # normally this would have locatorType but default is id

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)  # normally this would have locatorType but default is id

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickLoginLink()
        time.sleep(3)
        self.clearFields()
        time.sleep(3)
        self.enterEmail(email)
        time.sleep(3)
        self.enterPassword(password)
        time.sleep(3)
        self.clickLoginButton()
        self.

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//a[@href='/community']", locatorType="xpath")
        self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Result = " + str(result))
        print(self.myclass + ": " + inspect.stack()[0][3] + ": Result = " + str(result))
        print("verifyLoginSuccessful")
        time.sleep(3)
        return result

    def verifyLoginFailed(self):
        # result = self.isElementPresent("//span[contains(text(),'Your username or password is invalid. Please try again.')]", locatorType="xpath")
        result = self.isElementPresent("//span[@class='dynamic-text help-block']", locatorType="xpath")
        self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Result = " + str(result))
        return result

    def verifyLoginTitle(self):

        if "My Courses xxxxx" in self.getTitle():
            return True
        else:
            return False

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(Locator="//div[@id='navbar']//a[@href='/sign-out']",
                                                locatorType='xpath', pollFrequency=1)
        #self.elementClick(element=logoutLinkElement)
        self.elementClick(locator="//div[@id='navbar']//a[@href=/sign-out']", locatorType='xpath')

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def logout(self):
        self.nav.navigateToUserIcon()
        time.sleep(2)
        self.elementClick(locator="//a[@href='/logout']", locatorType='xpath')
        time.sleep(2)

