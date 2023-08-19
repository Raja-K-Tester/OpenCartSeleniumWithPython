import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service=Service("C:/Grid/chromedriver.exe")
options=webdriver.ChromeOptions()
driver=webdriver.Chrome(service=service,options=options)
driver.delete_all_cookies()
driver.maximize_window()
driver.set_page_load_timeout(60)
driver.get("https://thetestingworld.com/shop")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,"span.caret").click()
driver.find_element(By.LINK_TEXT,"Login").click()
driver.find_element(By.ID,"input-email").send_keys("raja.raman.009@gmail.com")
driver.find_element(By.ID,"input-password").send_keys("rajak1")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
# Go to HomePage
driver.find_element(By.CSS_SELECTOR,"i.fa.fa-home").click()
# Change Currency to Euro
driver.find_element(By.CSS_SELECTOR,"i.fa.fa-caret-down").click()
driver.find_element(By.CSS_SELECTOR,"button[name='EUR']").click()
# Add items to WishList
# Add MacBook
driver.find_element(By.XPATH,"//button[@onclick=\"wishlist.add('43');\"]").click()
# Add iPhone
driver.find_element(By.XPATH,"//button[@onclick=\"wishlist.add('40');\"]").click()
# Add Apple Cinema 30
time.sleep(5)
driver.find_element(By.XPATH,"//button[@onclick=\"wishlist.add('42');\"]").click()
#Add Canon EOS 5D
driver.find_element(By.XPATH,"//button[@onclick=\"wishlist.add('30');\"]").click()
#Remove Canon EOS 5D from the WishList
driver.find_element(By.CSS_SELECTOR,"a#wishlist-total").click()
driver.refresh()
driver.find_element(By.CSS_SELECTOR,"a[href=\"https://thetestingworld.com/shop/index.php?route=account/wishlist&remove=30\"]").click()
# Verify Success message
time.sleep(3)
driver.refresh()
#Assert.assertEquals("Success: You have modified your wish list!","Success: You have modified your wish list!")
# Add items to Cart
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"cart.add('43');\"]").click()
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"cart.add('40');\"]").click()
#Add AppleCinema 30
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"cart.add('42');\"]").click()
#Available Options
#large radio button
driver.find_element(By.XPATH,"//div[@id=\"input-option218\"]/div[3]/label/input").click()
# CheckBox
driver.find_element(By.XPATH,"//div[@id=\"input-option223\"]/div[4]/label/input").click()
#Select Color from dropdown
color=Select(driver.find_element(By.ID,"input-option217"))
color.select_by_value("1")
#TextArea
driver.find_element(By.CSS_SELECTOR,"textarea#input-option209").send_keys("Job")
#File Upload
driver.find_element(By.CSS_SELECTOR,"button#button-upload222").click()
time.sleep(40)
subprocess.Popen("C:/eclipse-workspace/Opencart/AutoIT/opencartfileupload1.exe")
time.sleep(40)
driver.switch_to.alert.dismiss()
#Add to Cart
driver.find_element(By.CSS_SELECTOR,"button#button-cart").click()
# CheckOut
driver.find_element(By.LINK_TEXT,"Checkout").click()
driver.find_element(By.CSS_SELECTOR,"input#button-payment-address").click()
driver.find_element(By.ID,"button-shipping-address").click()
#Payment Method-cash on delivery and Comments about your order if any
driver.find_element(By.ID,"button-shipping-method").click()
time.sleep(5)
driver.find_element(By.NAME,"agree").click()
driver.find_element(By.ID,"button-payment-method").click()
time.sleep(5)
#Confirm order
driver.find_element(By.ID,"button-confirm").click()
#Confirmation Message
#Assert.assertEquals("Your order has been placed!", "Your order has been placed!")
#Assert.assertEquals("Your order has been successfully processed!","Your order has been successfully processed!")
time.sleep(5)
#Take Screenshot after placing order
driver.get_screenshot_as_file("C:/Users/dell/PycharmProjects/OpenCart/Reports/Screenshot1.png")
driver.find_element(By.LINK_TEXT,"Continue").click()
#Go to My Account and Click Order History and check Order History
driver.find_element(By.CSS_SELECTOR,"span.caret").click()
driver.find_element(By.LINK_TEXT,"Order History").click()
driver.find_element(By.LINK_TEXT,"Logout").click()
#To reload a page
driver.find_element(By.ID,"reload-button").click()
driver.find_element(By.LINK_TEXT,"Continue").click()
driver.close()