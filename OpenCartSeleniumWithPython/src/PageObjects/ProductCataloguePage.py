from selenium.webdriver.common.by import By
from AbstractComponent.AbstractComponent import AbstractComponent
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from Resources.RandomGenerator import RandomGenerator


class ProductCatalogue(AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.hp = HomePage(driver)
        self.lp = LoginPage(driver)
        self.randomdata = RandomGenerator()
        self.Name = self.randomdata.random_first_name()
        self.Email = self.randomdata.random_email()

    IphoneAddtoCart = (By.CSS_SELECTOR, "button[onclick=\"cart.add('40', '1');\"]")
    IMacAddtoCart = (By.CSS_SELECTOR, "button[onclick=\"cart.add('41', '1');\"]")
    SamsungTabAddtoCart = (By.CSS_SELECTOR, "button[onclick=\"cart.add('49', '1');\"]")
    CartTotal = (By.CSS_SELECTOR, "span#cart-total")
    ViewCart = (By.XPATH, "//strong[contains(text(),'Cart')]")
    RecipientName = (By.ID, "input-to-name")
    RecipientEmail = (By.ID, "input-to-email")
    GiftCertificateTheme = (By.CSS_SELECTOR, "input[value='6']")
    Message = (By.ID, "input-message")
    Amount = (By.ID, "input-amount")
    Agree = (By.CSS_SELECTOR, "input[name='agree']")
    ContinueButton = (By.CSS_SELECTOR, "input.btn.btn-primary")
    Text = (By.XPATH, "//p[contains(text(),'Thank you for purchasing')]")

    def add_iphone(self):
        self.click(self.IphoneAddtoCart)
        self.click(self.CartTotal)
        self.click(self.ViewCart)

    def click_cart_total_and_view_cart(self):
        self.click(self.CartTotal)
        self.click(self.ViewCart)

    def add_imac(self):
        self.click(self.IMacAddtoCart)
        self.click(self.CartTotal)
        self.click(self.ViewCart)

    def add_samsung_galaxy_tab(self):
        self.click(self.SamsungTabAddtoCart)
        self.click(self.CartTotal)
        self.click(self.ViewCart)

    def buy_gift_certificate(self):
        self.sendText(self.RecipientName,self.Name)
        self.sendText(self.RecipientEmail,self.Email)
        self.click(self.GiftCertificateTheme)
        self.sendText(self.Message, "Merry Christmas to you and your family!")
        self.backspace(self.Amount)
        self.sendText(self.Amount, "1")
        self.click(self.Agree)
        self.click(self.ContinueButton)
        self.sleep()
