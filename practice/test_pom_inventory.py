import pytest
from pages.pom_login_page import LoginPage


@pytest.mark.smoke
def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.load()
    inventory_page = login_page.login("standard_user", "secret_sauce")
    
    assert inventory_page.is_loaded()
    assert inventory_page.get_cart_count() == 0
    
    inventory_page.add_to_cart("sauce-labs-backpack")
    
    assert inventory_page.get_cart_count() == 1

