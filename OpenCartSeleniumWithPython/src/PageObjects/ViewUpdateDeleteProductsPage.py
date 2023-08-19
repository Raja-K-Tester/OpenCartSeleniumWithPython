from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from AbstractComponent.AbstractComponent import AbstractComponent


class ViewUpdateDeleteProductsPage(AbstractComponent):
    click_and_open_tab = [Keys.CONTROL, Keys.ENTER]

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    Quantity = (By.XPATH, "//div[@class='input-group btn-block']/input")
    Update = (By.CSS_SELECTOR, "button[data-original-title='Update']")
    Remove = (By.CSS_SELECTOR, "button[data-original-title='Remove']")
    NikonD300Product = (By.XPATH, "//strong[contains(text(),'Nikon D300')]")
    Reviews = (By.LINK_TEXT, "Reviews (0)")
    Image = (By.XPATH, "//ul[@class='thumbnails']/li[1]")
    RightArrowKey = (By.CSS_SELECTOR, "button[title='Next (Right arrow key)']")
    Close = (By.CSS_SELECTOR, "button[title='Close (Esc)']")
    AddtoCartButton = (By.CSS_SELECTOR, "button#button-cart")
    MacBookProductLink = (By.XPATH, "//tbody[1]/tr[1]/td[2]/a[1]")
    MacBookAirLink = (By.XPATH, "//tbody[1]/tr[1]/td[3]/a[1]")
    MacBookProLink = (By.XPATH, "//tbody[1]/tr[1]/td[4]/a[1]")
    SonyVAIOProductLink = (By.XPATH, "//tbody[1]/tr[1]/td[5]/a[1]")
    iPodClassicLink = (By.LINK_TEXT, "iPod Classic")
    iPodTouchLink = (By.LINK_TEXT, "iPod Touch")

    def galaxy_tab_update_remove(self):
        self.backspace(self.Quantity)
        self.sendText(self.Quantity, "4")
        self.click(self.Update)
        self.click(self.Remove)

    def click_nikon_d300(self):

        self.sleep()
        self.click(self.NikonD300Product)
        self.scroll_page()
        self.sleep_with_20_seconds()
        self.click(self.Reviews)
        self.sleep()
        self.click(self.Image)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.Close)
        self.sleep()
        self.click(self.AddtoCartButton)
        self.sleep()

    def window_handles_for_mac_notebook(self):

        self.sendText(self.MacBookProductLink, self.click_and_open_tab)
        self.sendText(self.MacBookAirLink, self.click_and_open_tab)
        self.sendText(self.MacBookProLink, self.click_and_open_tab)
        self.sendText(self.SonyVAIOProductLink, self.click_and_open_tab)
        windows = self.driver.window_handles
        parent_id = windows[0]
        notebook = windows[1]
        mac_pro = windows[2]
        mac_air = windows[3]
        mac_book = windows[4]

        for win in windows:
            if win == parent_id:
                self.driver.switch_to.window(notebook)
                self.mac_and_notebook()
                self.driver.switch_to.window(mac_pro)
                self.air_and_pro()
                self.driver.switch_to.window(mac_air)
                self.air_and_pro()
                self.driver.switch_to.window(mac_book)
                self.mac_and_notebook()

        self.driver.switch_to.window(parent_id)

    def mac_and_notebook(self):
        self.scroll_page()
        self.sleep()
        self.click(self.Image)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.Close)
        self.click(self.AddtoCartButton)
        self.sleep()

    def air_and_pro(self):
        self.scroll_page()
        self.sleep()
        self.click(self.Image)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.Close)
        self.click(self.AddtoCartButton)
        self.sleep()

    def window_handles_for_mp3_players(self):
        self.sendText(self.iPodClassicLink, self.click_and_open_tab)
        self.sendText(self.iPodTouchLink, self.click_and_open_tab)
        windows = self.driver.window_handles
        parent_id = windows[0]
        ipod_touch = windows[1]
        ipod_classic = windows[2]

        for win in windows:
            if win == parent_id:
                self.driver.switch_to.window(ipod_touch)
                self.iPodTouch()
                self.driver.switch_to.window(ipod_classic)
                self.iPodClassic()

        self.driver.switch_to.window(parent_id)

    def iPodTouch(self):
        self.scroll_page()
        self.sleep()
        self.click(self.Image)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.Close)
        self.click(self.AddtoCartButton)
        self.sleep()

    def iPodClassic(self):
        self.scroll_page()
        self.sleep()
        self.click(self.Image)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.RightArrowKey)
        self.sleep()
        self.click(self.Close)
        self.click(self.AddtoCartButton)
        self.sleep()

    def remove_gift_certificate(self):
        self.click(self.Remove)
        self.sleep()
