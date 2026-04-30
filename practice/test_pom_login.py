import pytest
from pages.pom_login_page import LoginPage


@pytest.mark.smoke
def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    inventory_page = login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_loaded()
    #before POM: assert "/inventory.html" in driver.current_url
    
    


@pytest.mark.regression
def test_failed_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wrong_user", "wrong_pass")
    
    assert "Epic sadface" in login_page.get_error_message()

@pytest.mark.smoke
@pytest.mark.regression
def test_failed_login_lockedOut(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")
    
    assert "locked out" in login_page.get_error_message()

@pytest.mark.parametrize("username,password,expected_error",[
    ("locked_out_user", "secret_sauce", "locked out"),
    ("invalid_user", "wrong_pass", "do not match"),
    ("", "secret_sauce", "Username is required"),
])
def test_login_failures(driver, username, password,expected_error):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username,password)

    assert expected_error in login_page.get_error_message()