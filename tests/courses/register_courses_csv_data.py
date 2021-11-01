from pages.courses.register_courses_page import RegisterCoursesPage
from tests.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVData(unittest.TestCase):
    # cc_num = "1234567890123456"
    # exp_date = "1223"
    # cvv_num = "456"

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()    # this should take us to the ALL COURSES page at beginning of each test

    @pytest.mark.run(order=1)
    @data(*getCSVData("C://Andys Python//pyCharm//pythonProject2//letskodeit//testdata.csv"))
    @unpack
    def testInvalidEnrollment(self, searchValue, courseName, ccNum, ccExp, ccCVV):
        # Need to do this cuz the site takes you to My Courses when you log in
        # self.courses.goToCoursesPage("https://courses.letskodeit.com/courses")
        self.courses.enterCourseName(searchValue)
        time.sleep(1)
        # self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.selectCourseToEnroll(courseName)
        time.sleep(1)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        time.sleep(1)
        result = self.courses.verifyEnrollFailed()
        self.ts.mark(result, "Enrollment Verification")
        # self.ts.markFinal("testInvalidEnrollment")

        #self.courses.goToCoursesPage("https://courses.letskodeit.com/courses")
        # dont think really wanna do this at the end cuz if it fails then either it wont go to ALL COURSES
        # or if it does then you might lose the error message from the failure
        # self.driver.find_element_by_link_text("ALL COURSES").click()
