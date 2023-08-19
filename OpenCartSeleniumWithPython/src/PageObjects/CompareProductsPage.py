from AbstractComponent.AbstractComponent import AbstractComponent
from selenium.webdriver.common.by import By

class CompareProductsPage(AbstractComponent):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    AddCanonEOS5DCompare= (By.CSS_SELECTOR, "button[onclick=\"compare.add('30');\"]")
    AddNikonD300Compare= (By.CSS_SELECTOR, "button[onclick=\"compare.add('31');\"]")
    AddIPodClassicCompare= (By.CSS_SELECTOR, "button[onclick=\"compare.add('48');\"]")
    AddIPodNanoCompare= (By.CSS_SELECTOR, "button[onclick=\"compare.add('36');\"]")
    AddIPodShuffleCompare= (By.CSS_SELECTOR, "button[onclick=\"compare.add('34');\"]")
    AddIPodTouchCompare= (By.CSS_SELECTOR, "button[onclick=\"compare.add('32');\"]")
    AddMacBookCompare= (By.CSS_SELECTOR, "button[onclick=\"compare.add('43');\"]")
    AddMacBookAirCompare= (By.CSS_SELECTOR, "button[onclick=\"compare.add('44');\"]")
    AddMacBookProCompare= (By.CSS_SELECTOR, "button[onclick=\"compare.add('45');\"]")
    AddSonyVAIOCompare= (By.CSS_SELECTOR, "button[onclick=\"compare.add('46');\"]")
    ProductsCompareLink= (By.CSS_SELECTOR, "a#compare-total")


    def add_cameras_to_compare(self):
        self.click(self.AddCanonEOS5DCompare)
        self.click(self.AddNikonD300Compare)
        self.click(self.ProductsCompareLink)

    def add_notebooks_macbooks_to_compare(self):
        self.click(self.AddMacBookCompare)
        self.click(self.AddMacBookAirCompare)
        self.click(self.AddMacBookProCompare)
        self.click(self.AddSonyVAIOCompare)
        self.click(self.ProductsCompareLink)

    def add_mp3_players_to_compare(self):
        self.click(self.AddIPodClassicCompare)
        self.click(self.AddIPodNanoCompare)
        self.click(self.AddIPodShuffleCompare)
        self.click(self.AddIPodTouchCompare)
        self.click(self.ProductsCompareLink)
        self.scroll_page()