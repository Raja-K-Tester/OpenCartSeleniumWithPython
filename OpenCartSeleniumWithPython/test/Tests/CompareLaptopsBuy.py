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
# Click Laptops and Noteboks Link
driver.find_element(By.LINK_TEXT,"Laptops & Notebooks").click()
driver.find_element(By.LINK_TEXT,"Show All Laptops & Notebooks").click()
time.sleep(3)
# Compare 4 items and Add all to cart
# Add MacBook
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"compare.add('43');\"]").click()
time.sleep(5)
# Add Sony Notebook
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"compare.add('46');\"]").click()
time.sleep(5)
# Add MacBook Air
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"compare.add('44');\"]").click()
time.sleep(5)
# Add MacBook Pro
driver.find_element(By.CSS_SELECTOR,"button[onclick=\"compare.add('45');\"]").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"a#compare-total").click()
# Add all items to cart
driver.refresh()
clickandopentab=Keys.CONTROL,Keys.ENTER
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[2]/a[1]").send_keys(clickandopentab)
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[3]/a[1]").send_keys(clickandopentab)
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[4]/a[1]").send_keys(clickandopentab)
driver.find_element(By.XPATH,"//tbody[1]/tr[1]/td[5]/a[1]").send_keys(clickandopentab)
windows=driver.window_handles
it=windows.__iter__()
parentid=it.__next__()
macpro=it.__next__()
macair=it.__next__()
notebook=it.__next__()
macbook=it.__next__()
def macandnotebook():
    driver.execute_script("window.scrollTo(0,500)")
    time.sleep(5)
    driver.find_element(By.XPATH, "//ul[@class=\"thumbnails\"]/li[1]").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button[title='Next (Right arrow key)']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button[title='Next (Right arrow key)']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button[title='Next (Right arrow key)']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button[title='Next (Right arrow key)']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button[title='Close (Esc)']").click()
    driver.find_element(By.CSS_SELECTOR, "button#button-cart").click()
    time.sleep(5)
    driver.close()
def airandpro():
    driver.execute_script("window.scrollTo(0,500)")
    time.sleep(5)
    driver.find_element(By.XPATH, "//ul[@class=\"thumbnails\"]/li[1]").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button[title='Next (Right arrow key)']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button[title='Next (Right arrow key)']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button[title='Next (Right arrow key)']").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "button[title='Close (Esc)']").click()
    driver.find_element(By.CSS_SELECTOR, "button#button-cart").click()
    time.sleep(5)
    driver.close()

for win in windows:
    if win==parentid:
        driver.switch_to.window(macpro)
        airandpro()
        driver.switch_to.window(macair)
        airandpro()
        driver.switch_to.window(notebook)
        macandnotebook()
        driver.switch_to.window(macbook)
        macandnotebook()

driver.switch_to.window(parentid)
driver.refresh()
driver.find_element(By.CSS_SELECTOR,"span#cart-total").click()
driver.find_element(By.LINK_TEXT,"View Cart").click()
time.sleep(3)
# Click CheckOut
driver.find_element(By.LINK_TEXT,"Checkout").click()
driver.find_element(By.CSS_SELECTOR,"input#button-payment-address").click()
driver.find_element(By.ID,"button-shipping-address").click()
driver.find_element(By.ID,"button-shipping-method").click()
time.sleep(2)
driver.find_element(By.NAME,"agree").click()
driver.find_element(By.ID,"button-payment-method").click()
# Confirm order
driver.find_element(By.ID,"button-confirm").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Continue").click()
# Go to My Account and Click Order History and check Order History
driver.find_element(By.CSS_SELECTOR,"span.caret").click()
driver.find_element(By.LINK_TEXT,"Order History").click()
driver.find_element(By.LINK_TEXT,"Logout").click()
# To reload a page
driver.find_element(By.ID,"reload-button").click()
driver.find_element(By.LINK_TEXT,"Continue").click()
driver.close()