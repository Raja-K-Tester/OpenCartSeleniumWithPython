import requests
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
# Header Contact Link
driver.find_element(By.XPATH,"//div[@id='top-links']/ul/li[1]/a").click()
# Enter Details in Contact Form
driver.find_element(By.ID,"input-name").send_keys("ab")
driver.find_element(By.ID,"input-email").send_keys("ab")
driver.find_element(By.ID,"input-enquiry").send_keys("ab")
driver.find_element(By.CSS_SELECTOR,"input.btn.btn-primary").click()

# Go to HomePage
driver.find_element(By.CSS_SELECTOR,"i.fa.fa-home").click()
# Footer Links
footer=driver.find_element(By.TAG_NAME,"footer")
footerlinks=footer.find_elements(By.TAG_NAME,"a")
# Check all the footer links and verify the status code(200-ok,301-moved to new url,302 redirect to same url)
for link in footerlinks :
    url=link.get_attribute('href')
    result=requests.head(url)
    if result.status_code>400:
        print(url +"is broken with status code",result.status_code)
    else:
        print(url,result.status_code)