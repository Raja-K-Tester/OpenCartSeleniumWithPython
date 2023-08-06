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
driver.find_element(By.ID,"input-email").send_keys("raja.raman.009@gmail.com")
driver.find_element(By.ID,"input-password").send_keys("rajak1")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
# Go to HomePage
driver.find_element(By.CSS_SELECTOR,"i.fa.fa-home").click()
# Click Cameras Link
driver.find_element(By.LINK_TEXT,"Cameras").click()
#Compare 2 Cameras and Add to Cart
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"compare.add('30');\"]").click()
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"compare.add('31');\"]").click()
driver.find_element(By.CSS_SELECTOR,"a#compare-total").click()
#Click your Product Name Link
time.sleep(5)
driver.find_element(By.XPATH,"//strong[contains(text(),'Nikon D300')]").click()
#Read Description and Click Review Tab
driver.execute_script("window.scrollTo(0,500)")
time.sleep(8)
#driver.find_element(By.LINK_TEXT,"Reviews (0)").click()
time.sleep(8)
#Click and View 5 Images
driver.find_element(By.XPATH,"//ul[@class=\"thumbnails\"]/li[1]").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"button[title='Next (Right arrow key)']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"button[title='Next (Right arrow key)']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"button[title='Next (Right arrow key)']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"button[title='Next (Right arrow key)']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"button[title='Close (Esc)']").click()
driver.find_element(By.CSS_SELECTOR,"button#button-cart").click()
time.sleep(5)
#Click CheckOut
driver.find_element(By.LINK_TEXT,"Checkout").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"input#button-payment-address").click()
driver.find_element(By.ID,"button-shipping-address").click()
driver.find_element(By.ID,"button-shipping-method").click()
time.sleep(2)
driver.find_element(By.NAME,"agree").click()
driver.find_element(By.ID,"button-payment-method").click()
#Confirm order
driver.find_element(By.ID,"button-confirm").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Continue").click()
#Go to My Account and Click Order History and check Order History
driver.find_element(By.CSS_SELECTOR,"span.caret").click()
driver.find_element(By.LINK_TEXT,"Order History").click()
driver.find_element(By.LINK_TEXT,"Logout").click()
#To reload a page
driver.find_element(By.ID,"reload-button").click()
driver.find_element(By.LINK_TEXT,"Continue").click()
driver.close()