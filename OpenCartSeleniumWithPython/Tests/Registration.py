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
driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.ID,"input-firstname").send_keys("Raja")
driver.find_element(By.ID,"input-lastname").send_keys("Krishnan")
driver.find_element(By.ID,"input-email").send_keys("krish.wobble@gmail.com")
driver.find_element(By.ID,"input-telephone").send_keys("123")
driver.find_element(By.ID,"input-password").send_keys("rajakrishnan1")
driver.find_element(By.ID,"input-confirm").send_keys("rajakrishnan1")
#For Yes Radio Button
#driver.find_element()(.IDxpath("//label[@class='radio-inline']/input[@value='1']")).click()
#For No Radio Button
#driver.find_element()(.IDcssselector("input[value='0']")).click()
driver.find_element(By.CSS_SELECTOR,"input[name='agree']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
driver.find_element(By.LINK_TEXT,"Continue").click()
driver.find_element(By.LINK_TEXT,"Logout").click()
#To reload a page
driver.find_element(By.ID,"reload-button").click()
driver.find_element(By.LINK_TEXT,"Continue").click()
driver.close()
