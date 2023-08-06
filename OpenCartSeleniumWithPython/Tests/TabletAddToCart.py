from selenium import webdriver
from selenium.webdriver import Keys
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
driver.find_element(By.ID,"input-email").send_keys("raja.raman.009@gmail.com")
driver.find_element(By.ID,"input-password").send_keys("rajak1")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
# Go to HomePage
driver.find_element(By.CSS_SELECTOR,"i.fa.fa-home").click()
# Click Tablets Link
driver.find_element(By.LINK_TEXT,"Tablets").click()
# Add Samsung Galaxy Tab to Cart
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"cart.add('49', '1');\"]").click()
# Verify item added to cart or not
#Assert.assertEquals("Success: You have added Samsung Galaxy Tab 10.1 to your shopping cart!","Success: You have added Samsung Galaxy Tab 10.1 to your shopping cart!");
time.sleep(5)
#Click cart with Total button at top right corner and click view cart link
driver.find_element(By.CSS_SELECTOR,"div#cart").click()
driver.find_element(By.XPATH,"//a/strong/i[@class='fa fa-shopping-cart']").click()
#After verify the order,update and delete quantity from the cart
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='input-group btn-block']/input").send_keys(Keys.BACK_SPACE)
driver.find_element(By.XPATH,"//div[@class='input-group btn-block']/input").send_keys("2")
driver.find_element(By.CSS_SELECTOR,"button[data-original-title='Update']").click()
#Assert.assertEquals("Success: You have modified your shopping cart!","Success: You have modified your shopping cart!");
driver.find_element(By.CSS_SELECTOR,"button[data-original-title='Remove']").click()
driver.refresh()
#actualmessage=driver.find_element(By.XPATH,"//div[@id='content']/p").text
#Assert.assertEquals(actualmessage,"Your shopping cart is empty!");
driver.find_element(By.LINK_TEXT,"Continue").click()
driver.find_element(By.CSS_SELECTOR,"span.caret").click()
driver.find_element(By.LINK_TEXT,"Logout").click()
#To reload a page
driver.find_element(By.ID,"reload-button").click()
driver.find_element(By.LINK_TEXT,"Continue").click()
driver.close()