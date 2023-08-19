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
# Click MP3 Players Link
driver.find_element(By.LINK_TEXT,"MP3 Players").click()
driver.find_element(By.LINK_TEXT,"Show All MP3 Players").click()
time.sleep(3)
# Compare 4 MP3 Players and Add to Cart
# Add iPod Shuffle
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"compare.add('34');\"]").click()
time.sleep(5)
# Add iPod Classic
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"compare.add('48');\"]").click()
time.sleep(5)
# Add iPod Nano
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"compare.add('36');\"]").click()
time.sleep(5)
# Add iPod Touch
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"compare.add('32');\"]").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"a#compare-total").click()
# Add iPod Classic and Touch to cart
driver.refresh()
clickandopentab=Keys.CONTROL,Keys.ENTER
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[3]/a[1]").send_keys(clickandopentab)
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[5]/a[1]").send_keys(clickandopentab)
windows=driver.window_handles
it=windows.__iter__()
parentid=it.__next__()
ipodclassic=it.__next__()
ipodtouch=it.__next__()

driver.switch_to.window(ipodclassic)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(5)
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
driver.find_element(By.CSS_SELECTOR,"button[title='Next (Right arrow key)']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"button[title='Next (Right arrow key)']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"button[title='Close (Esc)']").click()
driver.find_element(By.CSS_SELECTOR,"button#button-cart").click()
time.sleep(5)
driver.close()

driver.switch_to.window(ipodtouch)
driver.execute_script("window.scrollTo(0,500)")
time.sleep(5)
driver.find_element(By.XPATH,"//ul[@class=\"thumbnails\"]/li[1]").click()
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
driver.close()

driver.switch_to.window(parentid)
driver.refresh()
driver.find_element(By.CSS_SELECTOR,"span#cart-total").click()
driver.find_element(By.LINK_TEXT,"View Cart").click()
time.sleep(3)
#Click CheckOut
driver.find_element(By.LINK_TEXT,"Checkout").click()
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



