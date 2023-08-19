from AbstractComponent.AbstractComponent import AbstractComponent
from selenium.webdriver.common.by import By
class RegistrationPage(AbstractComponent):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    FirstName= (By.ID, "input-firstname")
    LastName= (By.ID, "input-lastname")
    Email= (By.ID, "input-email")
    Telephone= (By.ID, "input-telephone")
    Password= (By.ID, "input-password")
    ConfirmPassword= (By.ID, "input-confirm")
    NewsletterYes= (By.CSS_SELECTOR, "input[value='1']")
    NewsletterNo= (By.CSS_SELECTOR, "input[value='0']")
    PrivacyPolicy= (By.TAG_NAME, "b")
    Close= (By.CSS_SELECTOR, "button.close")
    IAgreeCheckBox= (By.CSS_SELECTOR, "input[name='agree']")
    SubmitButton= (By.CSS_SELECTOR, "input.btn.btn-primary")
    def set_first_name(self, fname):
        self.sendText(self.FirstName, fname)

    def set_last_name(self, lname):
        self.sendText(self.LastName, lname)

    def set_email(self, email):
        self.sendText(self.Email, email)

    def set_telephone_number(self, telephone):
        self.sendText(self.Telephone, telephone)

    def set_password(self, password):
        self.sendText(self.Password, password)

    def set_confirm_password(self, cpassword):
        self.sendText(self.ConfirmPassword, cpassword)

    def click_yes_newsletter_subscription(self):
        self.click(self.NewsletterYes)

    def click_no_newsletter_subscription(self):
        self.click(self.NewsletterNo)

    def click_privacy_policy(self):
        self.click(self.PrivacyPolicy)
        self.click(self.Close)

    def click_agree_check_box(self):
        self.click(self.IAgreeCheckBox)

    def click_submit_button(self):
        self.click(self.SubmitButton)
