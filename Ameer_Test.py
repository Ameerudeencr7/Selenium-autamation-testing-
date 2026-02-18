from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Open Browser and navigate to Google

driver = webdriver.Chrome()
driver.get("http://www.google.com")

wait = WebDriverWait(driver, 10)

# amazon Search

elem = driver.find_element(By.XPATH,"//*[@id='APjFqb']")
elem.send_keys("Amazon")
elem.send_keys(Keys.RETURN)

time.sleep(15)

# Click on Amazon link

elem = driver.find_element(By.PARTIAL_LINK_TEXT,"Amazon")
elem.click()

time.sleep(15)

#Books search

elem = driver.find_element(By.ID,"twotabsearchtextbox")
elem.send_keys("Books")
elem.send_keys(Keys.RETURN)

#Random click

books = driver.find_elements(By.CSS_SELECTOR,".s-search-results")
time.sleep(4)


if books:
    random_book =driver.execute_script("window.scrollBy(0, 3000)")
    random_book = random.choice(books)
try:
    wait.until(EC.element_to_be_clickable(random_book)).click()
except:
    driver.execute_script("arguments[0].click();", random_book)

time.sleep(5)

#Handle Tab switch

Tab2 = driver.switch_to.window(driver.window_handles[-1])


# Add to cart

try:
    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-button']")))
    add_to_cart.click()
    print("Added to cart successfully ✅")
except:
    print("Add to cart not found ❌")

#Quit the driver

input("Press Enter to Exit...")
driver.quit()