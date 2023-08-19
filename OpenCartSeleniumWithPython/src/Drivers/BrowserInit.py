import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

URL = "https://thetestingworld.com/shop"
TIMEOUT = 15


class BrowserInit:
    def initializeDriver(self):
        global driver
        config = configparser.RawConfigParser(allow_no_value=True)
        config.read("config.ini")

        browserName = config.get("browser_config", "browser", fallback="chrome")
        isHeadless = config.getboolean("browser_config", "headless", fallback=False)

        if "chrome" in browserName:
            options = ChromeOptions()
            if isHeadless:
                options.add_argument("--headless")
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        elif browserName.lower() == "firefox":
            options = FirefoxOptions()
            if isHeadless:
                options.add_argument("--headless")
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        elif "edge" in browserName:
            options = EdgeOptions()
            if isHeadless:
                options.add_argument("--headless")
            driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(), options=options)

        driver.set_window_size(1440, 900)
        driver.delete_all_cookies()
        driver.get(URL)
        driver.implicitly_wait(TIMEOUT)
        return driver
