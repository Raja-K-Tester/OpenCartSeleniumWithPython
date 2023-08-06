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
# Click Gift Certificates link at the footer
driver.find_element(By.LINK_TEXT,"Gift Certificates").click()
#Fill all details and click continue
driver.find_element(By.ID,"input-to-name").send_keys("Raja")
driver.find_element(By.ID,"input-to-email").send_keys("rajacse71@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[value='6']").click()
driver.find_element(By.ID,"input-message").send_keys("Merry Christmas to you and your family!")
driver.find_element(By.ID,"input-amount").send_keys(Keys.BACK_SPACE)
driver.find_element(By.ID,"input-amount").send_keys("1000")
driver.find_element(By.CSS_SELECTOR,"input[name='agree']").click()
driver.find_element(By.CSS_SELECTOR,"input.btn.btn-primary").click()
time.sleep(3)
# Take Screenshot after purchase Gift Certificate
text=driver.find_element(By.XPATH,"//p[contains(text(),'Thank you for purchasing')]")
text.screenshot("C:/Users/dell/PycharmProjects/OpenCart/Reports/Screenshot3.png")
driver.find_element(By.LINK_TEXT,"Continue").click()
driver.find_element(By.CSS_SELECTOR,"button[data-original-title='Remove']").click()
time.sleep(3)
driver.refresh()
driver.find_element(By.CSS_SELECTOR,"span.caret").click()
driver.find_element(By.LINK_TEXT,"Logout").click()
# To reload a page
driver.find_element(By.ID,"reload-button").click()
driver.find_element(By.LINK_TEXT,"Continue").click()
driver.close()