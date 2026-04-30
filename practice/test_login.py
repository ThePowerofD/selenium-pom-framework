import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

##This helps tag the test it can have multiple tags ex:
#@pytest.mark.tagNumber1
#@pytest.mark.tagNumber2
@pytest.mark.smoke
def test_successfull_login(driver):

    driver.get("https://www.saucedemo.com")
    wait = WebDriverWait(driver,10)

    wait.until(EC.presence_of_element_located((By.NAME, "user-name"))).send_keys("standard_user")
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_list")))
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

@pytest.mark.regression
def test_failed_login(driver):
    driver.get("https://www.saucedemo.com")
    wait = WebDriverWait(driver ,10)

    wait.until(EC.presence_of_element_located((By.NAME, "user-name"))).send_keys("standard_user")
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("password")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    
    error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    assert "Epic sadface" in error.text
    assert driver.current_url == "https://www.saucedemo.com/"