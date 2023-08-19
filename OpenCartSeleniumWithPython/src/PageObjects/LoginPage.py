from selenium.webdriver.common.by import By
from PageObjects.ProductCataloguePage import ProductCatalogue
from AbstractComponent.AbstractComponent import AbstractComponent

class LoginPage(AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ForgotPassword = (By.LINK_TEXT, "Forgotten Password")
    Email = (By.ID, "input-email")
    Password = (By.ID, "input-password")
    SubmitButton = (By.CSS_SELECTOR, "input[type='submit']")
    Logout = (By.LINK_TEXT, "Logout")

    def click_forgot_password(self, email):
        self.click(self.ForgotPassword)
        self.sendText(self.Email, email)
        self.click(self.SubmitButton)

    def enter_login_details(self, email, password):
        self.sendText(self.Email, email)
        self.sendText(self.Password, password)
        self.click(self.SubmitButton)
        product_catalogue = ProductCatalogue(self.driver)
        return product_catalogue

    def click_logout(self):
        self.click(self.Logout)
