from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service("C:/Grid/chromedriver.exe")
options=webdriver.ChromeOptions()
driver=webdriver.Chrome(service=service,options=options)
driver.delete_all_cookies()
driver.maximize_window()
driver.get("https://thetestingworld.com/shop")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,"span.caret").click()
driver.find_element(By.LINK_TEXT,"Login").click()
driver.find_element(By.LINK_TEXT,"Forgotten Password").click()
driver.find_element(By.ID,"input-email").send_keys("rajacse71@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
driver.close()