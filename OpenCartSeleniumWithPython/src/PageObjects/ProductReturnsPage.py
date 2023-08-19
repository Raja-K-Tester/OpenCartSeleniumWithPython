from selenium.webdriver.common.by import By
from AbstractComponent.AbstractComponent import AbstractComponent

class ProductReturnsPage(AbstractComponent):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    OrderID = (By.ID, "input-order-id")
    OrderDate = (By.ID, "input-date-ordered")
    ProductName = (By.ID, "input-product")
    ProductCode = (By.ID, "input-model")
    Quantity = (By.ID, "input-quantity")
    ReturnReason = (By.XPATH, "//label[normalize-space()='Dead On Arrival']")
    ProductOpenedorNot = (By.XPATH, "//label[@class='radio-inline']/input[@value='1']")
    TextArea = (By.ID, "input-comment")
    Submit = (By.CSS_SELECTOR, "input.btn.btn-primary")

    def return_product(self):
        self.sendText(self.OrderID, "196")
        self.waitForVisibility(self.OrderDate)
        self.sendText(self.OrderDate, "2023-07-28")
        self.waitForVisibility(self.ProductName)
        self.sendText(self.ProductName, "iPhone")
        self.waitForVisibility(self.ProductCode)
        self.sendText(self.ProductCode, "product11")
        self.backspace(self.Quantity)
        self.sendText(self.Quantity, "1")
        self.click(self.ReturnReason)
        self.waitForVisibility(self.ProductOpenedorNot)
        self.click(self.ProductOpenedorNot)
        self.waitForVisibility(self.TextArea)
        self.sendText(self.TextArea, "Need Replacement")
        self.click(self.Submit)
        self.sleep()
