from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class InventoryPage:

    URL = "https://www.saucedemo.com/inventory.html"
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_loaded(self):
        self.wait.until(EC.presence_of_all_elements_located(self.INVENTORY_LIST))
        return True

    def add_to_cart(self, product_slug):
        """Add a product by its slug, e.g. 'sauce-labs-backpack'"""
        locator = (By.CSS_SELECTOR, f"[data-test='add-to-cart-{product_slug}']")
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    def get_cart_count(self):
        """Returns the number on the cart badge as int, or 0 if no badge"""
        badges = self.driver.find_elements(*self.CART_BADGE)
        if not badges:
            return 0
        return int(badges[0].text)

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_LINK)).click()
        # We'll add CartPage return later