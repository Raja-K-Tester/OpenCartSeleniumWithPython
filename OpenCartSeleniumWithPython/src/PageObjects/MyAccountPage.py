from selenium.webdriver.common.by import By
from AbstractComponent import AbstractComponent

class MyAccountPage(AbstractComponent):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    MyAccountDropDown = (By.CSS_SELECTOR, "span.caret")
    MyAccountLink = (By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='My Account']")
    OrderHistory = (By.LINK_TEXT, "View your order history")
    WishlistModify = (By.LINK_TEXT, "Modify your wish list")
    ReturnRequest = (By.LINK_TEXT, "View your return requests")
    ContinueButton = (By.LINK_TEXT, "Continue")

    def my_account(self):
        self.click(self.MyAccountDropDown)
        self.wait_for_visibility(self.MyAccountLink)
        self.click(self.MyAccountLink)

    def modify_wish_list(self):
        self.click(self.WishlistModify)

    def view_order_history(self):
        self.click(self.OrderHistory)

    def view_return_request(self):
        self.click(self.ReturnRequest)