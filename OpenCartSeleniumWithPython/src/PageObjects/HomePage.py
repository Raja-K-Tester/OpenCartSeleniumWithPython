from selenium.webdriver.common.action_chains import ActionChains
from AbstractComponent.AbstractComponent import AbstractComponent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class HomePage(AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    MyAccountDropDown= (By.CSS_SELECTOR, "span.caret")
    Register= (By.LINK_TEXT, "Register")
    Login= (By.LINK_TEXT, "Login")
    Logout= (By.LINK_TEXT, "Logout")
    Search= (By.NAME, "search")
    SearchButton= (By.CSS_SELECTOR, "i.fa.fa-search")
    HomePage= (By.CSS_SELECTOR, "i.fa.fa-home")
    CurrencyDropDown= (By.CSS_SELECTOR, "i.fa.fa-caret-down")
    PoundSterling= (By.CSS_SELECTOR, "button[name='GBP']")
    Euro= (By.CSS_SELECTOR, "button[name='EUR']")
    USDollar= (By.CSS_SELECTOR, "button[name='USD']")
    Continue= (By.LINK_TEXT, "Continue")
    ShoppingCart= (By.CSS_SELECTOR, "a[title='Shopping Cart']")
    Checkout= (By.CSS_SELECTOR, "a[title='Checkout']")
    WishList= (By.CSS_SELECTOR, "a#wishlist-total")
    ContactUs= (By.CSS_SELECTOR, "i.fa.fa-phone")
    Returns= (By.LINK_TEXT, "Returns")
    GiftCertificate= (By.LINK_TEXT, "Gift Certificates")
    Desktops= (By.LINK_TEXT, "Desktops")
    Mac= (By.LINK_TEXT, "Mac (1)")
    Tablets= (By.LINK_TEXT, "Tablets")
    Cameras= (By.LINK_TEXT, "Cameras")
    LaptopandNoteBooks= (By.LINK_TEXT, "Laptops & Notebooks")
    ShowAllLapandNoteBooks= (By.LINK_TEXT, "Show All Laptops & Notebooks")
    Mp3Players= (By.LINK_TEXT, "MP3 Players")
    ShowAllMp3Players= (By.LINK_TEXT, "Show All MP3 Players")
    Footer= (By.TAG_NAME, "footer")
    def click_register(self):
        self.click(self.MyAccountDropDown)
        self.click(self.Register)

    def click_login(self):
        self.click(self.MyAccountDropDown)
        self.click(self.Login)

    def click_logout(self):
        self.click(self.MyAccountDropDown)
        self.click(self.Logout)

    def click_home_page(self):
        self.click(self.HomePage)

    def change_to_euro_currency(self):
        self.click(self.CurrencyDropDown)
        self.click(self.Euro)

    def change_to_pound_sterling(self):
        self.click(self.CurrencyDropDown)
        self.click(self.PoundSterling)

    def change_to_us_dollar(self):
        self.click(self.CurrencyDropDown)
        self.click(self.USDollar)

    def search_product(self, search_product):
        self.sendText(self.Search, search_product)
        self.click(self.SearchButton)

    def click_shopping_cart(self):
        self.click(self.ShoppingCart)

    def click_checkout(self):
        self.click(self.Checkout)

    def click_wish_list(self):
        self.click(self.WishList)

    def click_contact_us(self):
        self.click(self.ContactUs)

    def click_returns(self):
        self.click(self.Returns)

    def click_gift_certificate(self):
        self.click(self.GiftCertificate)

    def click_continue(self):
        self.click(self.Continue)

    def click_desktop_and_mac(self):
        self.click(self.Desktops)
        self.waitForVisibility(self.Mac)
        self.click(self.Mac)

    def click_tablets(self):
        self.click(self.Tablets)

    def click_cameras(self):
        self.click(self.Cameras)

    def click_lap_notebook_and_show_all(self):
        self.click(self.LaptopandNoteBooks)
        self.waitForVisibility(self.ShowAllLapandNoteBooks)
        self.click(self.ShowAllLapandNoteBooks)

    def click_mp3_players_and_show_all(self):
        self.click(self.Mp3Players)
        self.waitForVisibility(self.ShowAllMp3Players)
        self.click(self.ShowAllMp3Players)

    def click_footer_links(self):

        footer = self.driver.find_element(*self.Footer)
        footer_links = footer.find_elements(By.TAG_NAME, 'a')
        # Open each link in a new tab using ActionChains
        action = ActionChains(self.driver)
        for link in footer_links[1:]:
            action.key_down(Keys.CONTROL).click(link).perform()
            self.waitForVisibility(link)

            # Switch to each opened tab and print the title
            for handle in self.driver.window_handles:
                self.driver.switch_to.window(handle)
                print(self.driver.title)
