from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://www.saucedemo.com")
wait = WebDriverWait(driver,10)

username_field = wait.until(EC.presence_of_element_located((By.NAME, "user-name")))
print(username_field.tag_name)
username_field.send_keys("standard_user")

password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys("secret_sauce")

login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
login_button.click()

# Wait for next page to confirm login worked
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
print(driver.current_url)

driver.quit()
