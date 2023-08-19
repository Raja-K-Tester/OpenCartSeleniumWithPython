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
#Search Iphone and add it to cart
driver.find_element(By.NAME,"search").send_keys("iph")
driver.find_element(By.CSS_SELECTOR,"i.fa.fa-search").click()
driver.find_element(By.XPATH,"//span[contains(text(),'Add to Cart')]").click()
#Click cart with Total button at top right corner and click view cart link
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"div#cart").click()
driver.find_element(By.XPATH,"//a/strong/i[@class='fa fa-shopping-cart']").click()
#After verify details click Checkout link
driver.find_element(By.LINK_TEXT,"Checkout").click()
#Checkout Details
driver.find_element(By.CSS_SELECTOR,"input#button-payment-address").click()
"""driver.find_element(By.ID,"input-payment-firstname").send_keys("Raja")
		driver.find_element(By.ID,"input-payment-lastname").send_keys("Krishnan")
		driver.find_element(By.ID,"input-payment-address-1").send_keys("abd")
		driver.find_element(By.ID,"input-payment-city").send_keys("Bangalore")
		driver.find_element(By.ID,"input-payment-postcode").send_keys("560002")
		country=Select(driver.find_element(By.ID,"input-payment-country"))
		country.select_by_visible_text("India")
		region=Select(driver.find_element(By.ID,"input-payment-zone"))
	region.select_by_visible_text("Karnataka") """
# Delivery Details
driver.find_element(By.ID,"button-shipping-address").click()
# Delivery Method-Flat rate and Comments about your order if any
driver.find_element(By.ID,"button-shipping-method").click()
# Payment Method-cash on delivery and Comments about your order if any
time.sleep(2)
driver.find_element(By.NAME,"agree").click()
driver.find_element(By.ID,"button-payment-method").click()
#Confirm order
driver.find_element(By.ID,"button-confirm").click()
# Take Screenshot after placing order
time.sleep(2)
driver.get_screenshot_as_file("C:/Users/dell/PycharmProjects/OpenCart/Reports/Screenshot.png")
driver.find_element(By.LINK_TEXT,"Continue").click()
# Go to My Account and Click Order History and check Order History
driver.find_element(By.CSS_SELECTOR,"span.caret").click()
driver.find_element(By.LINK_TEXT,"Order History").click()
driver.find_element(By.LINK_TEXT,"Logout").click()
#To reload a page
driver.find_element(By.ID,"reload-button").click()
driver.find_element(By.LINK_TEXT,"Continue").click()
driver.close()




