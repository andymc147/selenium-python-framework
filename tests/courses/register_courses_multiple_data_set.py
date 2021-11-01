from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):
    # cc_num = "1234567890123456"
    # exp_date = "1223"
    # cvv_num = "456"

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript", "JavaScript for beginners", "1234567890123456", "1223", "456"), ("Test", "Complete Test Automation Bundle", "1234567890123456", "1223", "456"))
    @unpack
    def testInvalidEnrollment(self, searchValue, courseName, ccNum, ccExp, ccCVV):
        # Need to do this cuz the site takes you to My Courses when you log in
        self.courses.goToCoursesPage("https://courses.letskodeit.com/courses")
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
