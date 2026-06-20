from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.pom_inventory_page import InventoryPage


class LoginPage:
    URL = "https://www.saucedemo.com"
    
    USERNAME_INPUT = (By.NAME, "user-name")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def load(self):
        self.driver.get(self.URL)
        return self
    
    def enter_username(self, username):
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT)).send_keys(username)
        return self
    
    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT)).send_keys(password)
        return self
    
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        return self
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return InventoryPage(self.driver)
    
    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text
    
    
    #def is_logged_in(self):
        #return "/inventory.html" in self.driver.current_url
    
    