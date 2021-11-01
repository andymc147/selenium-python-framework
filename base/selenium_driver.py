from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import inspect
import os
import time
from selenium import webdriver

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)
    myclass = "SeleniumDriver"

    def __init__(self, driver):
        self.driver = driver

    def screenShot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        :param resultMessage:
        :return:
            None
        """
        fileName = resultMessage + "." + str(round(time.time() * 10000)) + ".png"
        screenshotDirectory = "..\\screenshots\\"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)      # gets the path name for the current file
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info(self.myclass + ": " + inspect.stack()[0][3] +
                          ": screenshot saved to directory: " + destinationFile)
        except:
            self.log.error(self.myclass + ": " + inspect.stack()[0][3] +
                           ": exception occurred while trying to save screenshot to: " + destinationFile)
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": locatorType: " + locatorType)
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Locator type " + locatorType + " is not supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            by_type = self.getByType(locatorType)
            element = self.driver.find_element(by_type, locator)
            self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Element found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Element not found with locator: " + locator + " and locatorType: " + locatorType)
        return element      # Note  since element initialized to None, this will return None if the element not found

    def getElementList(self, locator, locatorType="id"):
        """
        NEW METHOD
        Get list of elements

        :param locator:
        :param locatorType:
        :return: element list
        """

        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)    # notice find_elements instead of find_element
            self.log.info("Element list found with locator " + locator +
                          " and locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator " + locator +
                          " and locatorType: " + locatorType)
        return element

    def elementClick(self, locator="", locatorType="id", element=None):
        """
        Click on an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        :param locator:
        :param locatorType:
        :return:
        """
        try:
            if locator:       # this means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Cannot click on element with locator: " + locator + " locatorType: " + locatorType)
            self.log.info(print_stack())    # I added this to see if stack would go in log
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):
        """
        Either provide element or a combination of locator and locatorType
        :param data:
        :param locator:
        :param locatorType:
        :param element:
        :return: N/A
        """
        try:
            if locator:  # this means if locator is not empty
                print("locator = " + locator)
                element = self.getElement(locator, locatorType)
                if element is not None:
                    print("got a hit on element")
            element.click()
            element.send_keys(data)
            self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Sent " + data + " to element with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Cannot send " + data + " to element with locator: " + locator + " and locatorType: " + locatorType)
            # self.log.info(print_stack())
            print_stack

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        NEW METHOD
        Get Text on an element
        Either provide element or a combination of locator and locatorType
        :param locator:
        :param locatorType:
        :param element:
        :param info:
        :return: text
        """

        try:
            if locator:  # this means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'" )
                text = text.strip()
        except:
            self.log.info("Failed to get text on element :: " + info)
            self.log.info(print_stack())
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        MODIFIED
        :param locator:
        :param locatorType:
        :return: True or False on element presence
        """
        try:
            if locator:  # this means if locator is not empty
                print("IsElementPresent - locator = " + locator + ", locatorType = " + locatorType)
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present based on locator: " + locator +
                              " locatorType: " + locatorType)
                print("Element present based on locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element NOT present based on locator: " + locator +
                              " locatorType: " + locatorType)
                print("Element NOT present based on locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            self.log.info("Exception occurred while checking based on locator: " + locator +
                          " locatorType: " + locatorType)
            print("Exception occurred while checking based on locator: " + locator +
                          " locatorType: " + locatorType)
            return False

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType

        :param locator:
        :param locatorType:
        :param element:
        :return: True or False based on whether element is displayed
        """
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.isDisplayed()
                self.log.info("Element is displayed based on locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element is NOT displayed based on locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            self.log.info("Exception occurred while checking whether element is displayed based on locator: " +
                          locator + " locatorType: " + locatorType)
            return False

    def elementPresenceCheck(self, locator, byType):
        try:   # normally this should not throw exception even if element not found but....
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Element found - len = " + str(len(elementList)))
                return True
            else:
                self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Element not found")
                return False
        except:
            self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Exception happened")
            return False

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=.5):

        element = None
        try:
            # if you have implicit wait set on the driver but you need a longer wait for 1 or 2 elements
            # turn the implicit wait off by setting it to 0 before using the explicit timeout
            # then at the end of this routine turn the implicit wait back on by resetting the value - see below
            byType = self.getByType(locatorType)
            self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be visible")
            # Notice in following line of code driver is changed to self.driver !!
            # Notice the timeout value is being taken from the timeout variable in the method statement
            # Notice the poll_frequency value is being taken from the timeout variable in the method statement
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])

            # Notice the By.ID or By.XPATH etc value is being taken from the byTYpe variable that was populated
            # by calling the getByTYpe function of the HandyWrappers class
            # Notice the element we are looking for is replaced by the locator value passed in to the routine
            # Pay CLOSE ATTENTION to the parens here !!
            element = wait.until(EC.visibility_of_element_located((byType, locator)))

            self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Element appeared on the web page")
        except:
            self.log.info(self.myclass + ": " + inspect.stack()[0][3] + ": Element did not appear on the web page")
            self.log.info(print_stack())

            # Here is where you reset the value for impicitly wait
        self.driver.implicitly_wait(2)
        return element

    def scroller(self, direction="up"):
        """
        NEW METHOD
        Scroll the page
        :param direction: up, down, left, right
        :return: N/A
        """

        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        elif direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")
        elif direction == "left":
            self.driver.execute_script("window.scrollBy(1000, 0);")
        elif direction == "right":
            self.driver.execute_script("window.scrollBy(-1000, 0);")

    def switchToFrame(self, id="", name="", index=None):
        """
        Switch to iframe using element locator inside iframe

        Parameters:
            Required:
                None
            Optional:
                :param fid: - id of the iframe
                :param name: - name of the iframe
                :param index: - index of the iframe
        :return:
            N/A

        Exception:
            N/A
        """

        if id:
            print("id")
            self.driver.switch_to.frame(id)
        elif name:
            print("name")
            self.driver.switch_to.frame(name)
        else:
            print("index")
            self.driver.switch_to.frame(index)

    def switchToDefaultContent(self):
        """
        Switch to default content
        Parameters:
            None
        Returns:
            N/A
        Exceptions:
            N/A
        """

        self.driver.switch_to.default_content()

    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType=""):
        """
        Get the value of an attribute of an element

        Parameters:
            Required:
                attribute - attribute whose value to find

            Optional:
                element - Element whose attribute is to be checked
                locator - Locator of the element
                locatorType - Locator Type to find the element

        Returns:
            The value of the attribute

        Exceptions:
            N/A
        """

        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            Required:
                locator - locator of the element to check
            Optional:
                locatorType - id, xpath, css, className, linkText
                info - Information about the element, label/name of the element

        Returns:
            Boolean

        Exception:
            log an error
        """

        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeVakue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeVakue is not None:
                enabled = element.is_enabled
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not("disabled" in value)
            if enabled:
                self.log.info("Element :: " + info + " is enabled")
            else:
                self.log.info("Element :: " + info + " is not enabled")
        except:
            self.log.error("Element :: " + info + " state could not be found")
        return enabled

    def SwitchFrameByIndex(self, locator, locatorType):
        """
        Get the iframe index using element locator insode iframe

        Parameters
            Required:
                locator - locator of the element to check
                locatorType - id, xpath, css, className, linkText
            Optional:
                N/A

            Returns:
                index of the iframe

            Exception:
                log an error
        """
        result = False
        try:
            iframe_list = self.getElementList("//iframe", locatorType='xpath')
            self.log.info("Length of iframe list: " + str(len(iframe_list)))
            print(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                print("i = " + str(i))
                self.switchToFrame(index=iframe_list[i])
                #self.switchToFrame(index=str(i))
                result = self.isElementPresent(locator, locatorType)
                if result:
                    print("y")
                    self.log.info("iframe index is: " + str(i))
                    break
                self.switchToDefaultContent()
            return result
        except:
            print("iframe index not found for locator " + locator + " and locatorType " + locatorType)
            self.log.error("iframe index not found for locator " + locator + " and locatorType " + locatorType)
