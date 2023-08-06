from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service=Service("C:/Grid/chromedriver.exe")
options=webdriver.ChromeOptions()
driver=webdriver.Chrome(service=service,options=options)
driver.delete_all_cookies()
driver.maximize_window()
driver.get("https://thetestingworld.com/shop")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,"span.caret").click()
driver.find_element(By.LINK_TEXT,"Login").click()
time.sleep(5)
driver.find_element(By.ID,"input-email").send_keys("raja.raman.009@gmail.com")
driver.find_element(By.ID,"input-password").send_keys("rajak1")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
# Go to HomePage
driver.find_element(By.CSS_SELECTOR,"i.fa.fa-home").click()
# Change Currency to Pound Sterling
driver.find_element(By.CSS_SELECTOR,"i.fa.fa-caret-down").click()
driver.find_element(By.CSS_SELECTOR,"button[name='GBP']").click()
# Click Desktops Link and Click Mac Link in the dropdown
driver.find_element(By.LINK_TEXT,"Desktops").click()
driver.find_element(By.LINK_TEXT,"Mac (1)").click()
# Add iMac to the Cart
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"cart.add('41', '1');\"]").click()
# Click Checkout
driver.find_element(By.LINK_TEXT,"Checkout").click()
driver.find_element(By.CSS_SELECTOR,"input#button-payment-address").click()
driver.find_element(By.ID,"button-shipping-address").click()
driver.find_element(By.ID,"button-shipping-method").click()
time.sleep(2)
driver.find_element(By.NAME,"agree").click()
driver.find_element(By.ID,"button-payment-method").click()
#Confirm order
driver.find_element(By.ID,"button-confirm").click()
# Take Screenshot after placing order
time.sleep(2)
driver.get_screenshot_as_file("C:/Users/dell/PycharmProjects/OpenCart/Reports/Screenshot2.png")
driver.find_element(By.LINK_TEXT,"Continue").click()
# Go to My Account and Click Order History and check Order History
driver.find_element(By.CSS_SELECTOR,"span.caret").click()
driver.find_element(By.LINK_TEXT,"Order History").click()
driver.find_element(By.LINK_TEXT,"Logout").click()
#To reload a page
driver.find_element(By.ID,"reload-button").click()
driver.find_element(By.LINK_TEXT,"Continue").click()
driver.close()
