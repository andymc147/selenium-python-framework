import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage

@pytest.fixture()
def setUp():        # doesn't need to be called setUp - could be xxxx
    print("Running method level setUp")
    yield           # anything before the yield keyword runs before the method
                    # anything after the yield runs after the method
    print("Running method level tearDown")


# @pytest.fixture(scope="module")   # by default the scope is function - so every function : module means once at beginning and/or end of the module
@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):     # doesn't need to be called oneTimeSetUp - could be xxxx
                                        # added the fixtures of browser and osType that are going to be passed in from the command line
                                        # the actual fixtures here are defined below and they return the values here
    print("Running module level one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("andymc147@yahoo.com", "lkiBl00mers$$00")

    if request.cls is not None:
        request.cls.driver = driver


    yield driver         # anything before the yield keyword runs before the method
                        # anything after the yield runs after the method
                        # the yield will return something to the caller
                        # (not sure if that can be used in the code after the yield as well)

    print("Running module level one time tearDown")




def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
