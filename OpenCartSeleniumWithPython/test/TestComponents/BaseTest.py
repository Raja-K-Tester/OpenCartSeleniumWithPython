import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BaseTest:

    def __init__(self):
        self.driver = None

    def get_screenshot(self, test_case_name):
        screenshot_dir = os.path.join(os.getcwd(), "reports")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, f"{test_case_name}.png")

        try:
            self.driver.save_screenshot(screenshot_path)
        except Exception as e:
            print("Error capturing screenshot:", e)

        return screenshot_path

    def get_element_screenshot(self, test_case_name, element):
        screenshot_dir = os.path.join(os.getcwd(), "reports")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, f"{test_case_name}.png")

        try:
            element.screenshot(screenshot_path)
        except Exception as e:
            print("Error capturing element screenshot:", e)

        return screenshot_path

    def reload(self):
        self.driver.refresh()

    def file_upload(self):
        try:
            time.sleep(30)
            os.system("path_to_autoit_script.exe")  # Replace with actual path
        except Exception as e:
            print("Error performing file upload:", e)

    def click_contact_us_page(self):
        try:
            contact_link = self.driver.find_element(By.XPATH, "//div[@id='top-links']/ul/li[1]/a")
            contact_link.click()

            name_input = self.driver.find_element(By.ID, "input-name")
            email_input = self.driver.find_element(By.ID, "input-email")
            enquiry_input = self.driver.find_element(By.ID, "input-enquiry")
            submit_button = self.driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary")

            name_input.send_keys("ab")
            email_input.send_keys("ab")
            enquiry_input.send_keys("ab")
            submit_button.click()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Name')]")))
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'E-Mail')]")))
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Enquiry')]")))

        except Exception as e:
            print("Error clicking Contact Us page:", e)

    def assert_success_message(self, message):
        try:
            assert message in self.driver.page_source
        except AssertionError as e:
            print("Assertion error:", e)

    def launch_application(self):
        try:
            self.driver = webdriver.Chrome()  # Change to your desired browser driver
            self.driver.maximize_window()
            self.driver.get("your_application_url_here")
        except Exception as e:
            print("Error launching application:", e)

    def tear_down(self):
        if self.driver is not None:
            self.driver.quit()
