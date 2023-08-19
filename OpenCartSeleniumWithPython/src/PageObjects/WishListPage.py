from selenium.webdriver.common.by import By
from AbstractComponent.AbstractComponent import AbstractComponent

class WishListPage(AbstractComponent):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    MacBookWishList = (By.XPATH, "//button[@onclick=\"wishlist.add('43');\"]")
    MacBookCart = (By.XPATH, "//button[@onclick=\"cart.add('43');\"]")
    IPhoneWishList = (By.XPATH, "//button[@onclick=\"wishlist.add('40');\"]")
    IPhoneCart = (By.XPATH, "//button[@onclick=\"cart.add('40');\"]")
    AppleCinema30WishList = (By.XPATH, "//button[@onclick=\"wishlist.add('42');\"]")
    LargeRadioOption = (By.XPATH, "//div[@id='input-option218']/div[3]/label/input")
    LargeCheckBox = (By.XPATH, "//div[@id='input-option223']/div[4]/label/input")
    SelectYellow = (By.ID, "input-option217")
    TextArea = (By.CSS_SELECTOR, "textarea#input-option209")
    FileUpload = (By.CSS_SELECTOR, "button#button-upload222")
    Date = (By.ID, "input-option219")
    Time = (By.ID, "input-option221")
    AddtoCartButton = (By.CSS_SELECTOR, "button#button-cart")
    AppleCinema30Cart = (By.XPATH, "//button[@onclick=\"cart.add('42');\"]")
    CanonEOS5DWishList = (By.XPATH, "//button[@onclick=\"wishlist.add('30');\"]")
    RemoveCanonEOS5DWishList = (By.XPATH, "//a[@href='https://thetestingworld.com/shop/index.php?route=account/wishlist&remove=30']")

    def add_items_to_wishlist(self):
        self.click(self.MacBookWishList)
        self.waitForVisibility(self.IPhoneWishList)
        self.click(self.IPhoneWishList)
        self.sleep()
        self.click(self.AppleCinema30WishList)
        self.sleep()
        self.click(self.CanonEOS5DWishList)

    def remove_canon_eos_5d_wishlist(self):
        self.click(self.RemoveCanonEOS5DWishList)

    def add_iphone_macbook_cart(self):
        self.click(self.IPhoneCart)
        self.sleep()
        self.click(self.MacBookCart)
        self.sleep()

    def add_apple_cinema(self):
        self.click(self.AppleCinema30Cart)
        self.click(self.LargeRadioOption)
        self.click(self.LargeCheckBox)
        self.selectcolordropdown(self.SelectYellow, "2")
        self.sendText(self.TextArea, "Welcome to my Project. Thanks for your time to test this application")
        self.waitForVisibility(self.FileUpload)
        self.click(self.FileUpload)

    def continue_apple_cinema_cart(self):
        self.sendText(self.Date, "2023/07/28")
        self.waitForVisibility(self.Time)
        self.sendText(self.Time, "11:30")
        self.waitForVisibility(self.AddtoCartButton)
        self.click(self.AddtoCartButton)
