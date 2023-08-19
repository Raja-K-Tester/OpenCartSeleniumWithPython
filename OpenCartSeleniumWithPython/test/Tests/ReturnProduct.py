from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

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
# Click Returns link at the footer
driver.find_element(By.LINK_TEXT,"Returns").click()
# Fill all the details and submit request to return
driver.find_element(By.ID,"input-order-id").send_keys("157")
driver.find_element(By.ID,"input-date-ordered").send_keys("2023/07/15")
time.sleep(3)
driver.find_element(By.ID,"input-product").send_keys("iMac")
driver.find_element(By.ID,"input-model").send_keys("Product 14")
driver.find_element(By.ID,"input-quantity").send_keys(Keys.BACK_SPACE)
driver.find_element(By.ID,"input-quantity").send_keys("1")
driver.find_element(By.XPATH,"//fieldset[2]/div[4]/div[1]/div[1]/label[1]").click()
driver.find_element(By.XPATH,"//input[@value='1']").click()
driver.find_element(By.ID,"input-comment").send_keys("Need Replacement")
driver.find_element(By.CSS_SELECTOR,"input.btn.btn-primary").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Returns").click()
driver.find_element(By.LINK_TEXT,"Logout").click()
driver.find_element(By.ID,"reload-button").click()
driver.find_element(By.LINK_TEXT,"Continue").click()
driver.close()