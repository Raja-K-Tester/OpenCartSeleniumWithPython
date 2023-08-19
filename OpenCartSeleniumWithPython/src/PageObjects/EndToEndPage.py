from PageObjects.RegistrationPage import RegistrationPage  # Import the RegistrationPage class
from PageObjects.HomePage import HomePage  # Import the HomePage class
from AbstractComponent.AbstractComponent import AbstractComponent
from Resources.RandomGenerator import RandomGenerator

class EndToEndPage(AbstractComponent):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.rg = RandomGenerator()
        self.firstname = self.rg.random_first_name()
        self.lastname = self.rg.random_last_name()
        self.telephone = self.rg.random_number()
        self.email = RandomGenerator.random_email()  # Note: You may need to adjust this line based on how randomEmail() is defined in your RandomGenerator class
        self.password = RandomGenerator.random_password()  # Note: You may need to adjust this line based on how randomPassword() is defined in your RandomGenerator class

    def registration(self):
        registration = RegistrationPage(self.driver)
        homepage = HomePage(self.driver)

        # Register an Account
        homepage.click_register()
        registration.set_first_name(self.firstname)
        registration.set_last_name(self.lastname)
        registration.set_email(self.email)
        registration.set_telephone_number(self.telephone)
        registration.set_password(self.password)
        registration.set_confirm_password(self.password)
        registration.click_no_newsletter_subscription()
        registration.click_privacy_policy()
        registration.click_agree_check_box()
        registration.click_submit_button()
        self.sleep()
