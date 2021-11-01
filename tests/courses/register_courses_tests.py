from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    cc_num = "1234567890123456"
    exp_date = "1223"
    cvv_num = "456"

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def testInvalidEnrollment(self):
        # Need to do this cuz the site takes you to My Courses when you log in
        #self.courses.goToCoursesPage("https://courses.letskodeit.com/courses")
        
        time.sleep(3)
        # self.courses.enterCourseName("Javascript")
        self.courses.enterCourseName("Selenium")
        time.sleep(3)
        # self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.selectCourseToEnroll("Selenium WebDriver Advanced")
        time.sleep(3)
        self.courses.enrollCourse(num=self.cc_num, exp=self.exp_date, cvv=self.cvv_num)
        time.sleep(3)
        result = self.courses.verifyEnrollFailed()
        self.ts.mark(result, "Enrollment Verification")
        self.ts.markFinal("testInvalidEnrollment")
