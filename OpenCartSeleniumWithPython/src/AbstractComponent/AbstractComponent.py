import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class AbstractComponent:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def waitForVisibility(self, element):
        self.wait.until(EC.visibility_of(element))

    def click(self, element):
        self.waitForVisibility(element)
        element.click()

    def sendText(self, element, text):
        self.waitForVisibility(element)
        element.send_keys(text)

    def backspace(self, element):
        element.send_keys(Keys.BACK_SPACE)

    def getText(self, element):
        self.waitForVisibility(element)
        return element.text

    def selectcountrydropdown(self, element, countryname):
        select = Select(element)
        select.select_by_visible_text(countryname)

    def selectstatedropdown(self, element, statename):
        select = Select(element)
        select.select_by_visible_text(statename)

    def selectcolordropdown(self, element, yellow):
        select = Select(element)
        select.select_by_value(yellow)

    def scroll_page(self):
        self.driver.execute_script("window.scrollBy(0,600)")

    def sleep(self):
        time.sleep(5)

    def sleep_with_20_seconds(self):
        time.sleep(20)
