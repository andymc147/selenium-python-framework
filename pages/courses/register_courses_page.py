from base.basepage import BasePage
import logging
import utilities.custom_logger as cl
from selenium.webdriver.common.by import By
import time

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    ########################
    ####    Locators    ####
    ########################
    # courses page = https://courses.letskodeit.com/courses
    # search box = //input[@id='search']
    _search_box = "//input[@id='search']"
    _search_box_button = "//button[@type='submit']"
    _course = "//h4[contains(text(), '{0}')]"  # the {0} gets replaced by course title
    _all_courses = "//div[contains[@class,'zen-course-title']]"
    _enroll_button = "//button[@class='dynamic-button btn btn-default btn-lg btn-enroll']"
    _cc_num = "cardnumber"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _submit_enroll = "//button[contains(@class, 'sp-buy')]"
    _enroll_error_message = "//span[contains(text(),'Your card number is invalid.')]"
    _cc_frame = "//iframe[@title='Secure card number input frame']"
    _cc_exp_frame = "//iframe[@title='Secure card number input frame']"
    _cc_cvv_frame = "//iframe[@title='Secure CVC input frame']"
    # this site doesn't have an agree to terms checkbox but if it did ...
    _agree_to_terms_checkbox = "agreed_to_terms_checkbox"
    ############# error messages
    # //span[contains(text(), "Your card's expiration date is incomplete.")]
    # //span[contains(text(), "Your card's expiration year is invalid.")]
    # //span[contains(text(), "Your card's security code is incomplete.")]
    # //span[contains(text(),'Your card number is incomplete.')]


    def goToCoursesPage(self, page):
        self.driver.get(page)

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box, locatorType='xpath')
        # have to click on the button after entering the search criteria
        self.elementClick(locator=self._search_box_button, locatorType='xpath')

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType='xpath')

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button, locatorType='xpath')

    def enterCardNum(self, num):
        time.sleep(3)
        self.SwitchFrameByIndex(locator=self._cc_num, locatorType="name")
        self.sendKeys(num, locator=self._cc_num, locatorType="name")
        self.driver.switch_to.default_content()

    def enterCardExp(self, exp):
        self.SwitchFrameByIndex(locator=self._cc_exp, locatorType="name")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        self.driver.switch_to.default_content()

    def enterCardCVV(self, cvv):
        self.SwitchFrameByIndex(locator=self._cc_cvv, locatorType="name")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
        self.driver.switch_to.default_content()

    # this site doesn't have an agree to terms checkbox but if it did ...
    def clickAgreeToTermsCheckbox(self):
        self.elementClick(locator=self._agree_to_terms_checkbox, locatorType="id")


    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType='xpath')

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.scroller("down")
        self.enterCreditCardInformation(num, exp, cvv)
        # this site doesn't have an agree to terms checkbox but if it did ...
        # self.clickAgreeToTermsCheckbox()
        self.clickOnEnrollButton()
        self.screenShot("Payment page")

    def verifyEnrollFailed(self):
        self.driver.switch_to.default_content()
        messageElement = self.waitForElement(self._enroll_error_message, locatorType='xpath')
        result = self.isElementDisplayed(element=messageElement)
        return result

