from AbstractComponent.AbstractComponent import AbstractComponent
from selenium.webdriver.common.by import By
from faker import Faker

class CheckoutPage(AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.randomdata=Faker()
        #self.randomdata = RandomGenerator()
        #self.pfname = self.randomdata.random_first_name()
        #self.plname= self.randomdata.random_last_name()
        #self.paddress = self.randomdata.address().fullAddress()
        #self.pcity = self.randomdata.address().city()
        #self.postcode = self.randomdata.address().zipCode()
        #self.pcountry = "India"
        #self.pstate = "Karnataka"

    BillingDetails= (By.CSS_SELECTOR, "input#button-payment-address")
    ExistingAddress= (By.XPATH, "//label[normalize-space()='I want to use an existing address']")
    PaymentFirstName= (By.ID, "input-payment-firstname")
    PaymentLastName= (By.ID, "input-payment-lastname")
    PaymentAddress= (By.ID, "input-payment-address-1")
    PaymentCity= (By.ID, "input-payment-city")
    PostCode= (By.ID, "input-payment-postcode")
    PaymentCountry= (By.ID, "input-payment-country")
    PaymentState= (By.ID, "input-payment-zone")
    DeliveryDetails= (By.ID, "button-shipping-address")
    OrderComments= (By.CSS_SELECTOR, "textarea[name='comment']")
    DeliveryComments= (By.XPATH, "//div[@class='panel-body']/p[3]/textarea")
    DeliveryMethod= (By.ID, "button-shipping-method")
    TermsandConditions= (By.CSS_SELECTOR, "a.agree")
    CloseButton= (By.CSS_SELECTOR, "button.close")
    AgreeCheckBox= (By.NAME, "agree")
    PaymentMethod= (By.ID, "button-payment-method")
    ConfirmOrder= (By.ID, "button-confirm")

    def generate_random_data(self):
        pfname = self.randomdata.first_name()
        plname = self.randomdata.last_name()
        paddress = self.randomdata.address().replace('\n', ', ')
        pcity = self.randomdata.city()
        postcode = self.randomdata.zipcode()
        pcountry = "India"
        pstate = "Karnataka"

        return pfname, plname, paddress, pcity, postcode, pcountry, pstate


    def checkout_and_place_order(self):
        self.click(self.BillingDetails)
        self.waitForVisibility(self.DeliveryDetails)
        self.click(self.DeliveryDetails)
        self.sendText(self.OrderComments, "Make sure the Product you delivered is a high quality product")
        self.waitForVisibility(self.DeliveryMethod)
        self.click(self.DeliveryMethod)
        self.waitForVisibility(self.DeliveryComments)
        self.sendText(self.DeliveryComments, "Urgent! Please deliver it as early as possible")
        self.waitForVisibility(self.TermsandConditions)
        self.click(self.TermsandConditions)
        self.click(self.CloseButton)
        self.click(self.AgreeCheckBox)
        self.click(self.PaymentMethod)
        self.waitForVisibility(self.ConfirmOrder)
        self.click(self.ConfirmOrder)

    def enter_billing_details(self):
        pfname, plname, paddress, pcity, postcode, pcountry, pstate = self.generate_random_data()
        self.sendText(self.PaymentFirstName, pfname)
        self.sendText(self.PaymentLastName, plname)
        self.sendText(self.PaymentAddress, paddress)
        self.sendText(self.PaymentCity, pcity)
        self.sendText(self.PostCode, postcode)
        self.waitForVisibility(self.PaymentCountry)
        self.selectcountrydropdown(self.PaymentCountry, pcountry)
        self.waitForVisibility(self.PaymentState)
        self.selectstatedropdown(self.PaymentState, pstate)
