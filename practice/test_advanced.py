import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.smoke
def test_dropdown_menu_options(driver):
    
    driver.get("https://the-internet.herokuapp.com/dropdown")
    wait = WebDriverWait(driver,10)

    dropdown_element= driver.find_element(By.ID, "dropdown")
    dropdown = Select(dropdown_element)
    dropdown.select_by_index("1")
    assert dropdown.first_selected_option.text

@pytest.mark.smoke
@pytest.mark.alerts
def test_js_alerts(driver):

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    wait = WebDriverWait(driver,10)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[onclick='jsAlert()']"))).click()
    #jsAlert.click()
    #driver.switch_to.alert  ##switches to check on alerts

    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Alert"
    alert.accept()

@pytest.mark.alerts
def test_js_alerts_dissmiss(driver):

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    wait = WebDriverWait(driver,10)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Click for JS Confirm']"))).click() ## looking + clicking the JS confirmation button

    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Confirm"
    alert.dismiss()
    alert_ans= wait.until(EC.presence_of_element_located((By.ID, "result")))
    assert alert_ans.text == "You clicked: Cancel"
    #alert.accept()

@pytest.mark.alerts
def test_js_alert_prompt(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    wait = WebDriverWait(driver,10)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[onclick='jsPrompt()']"))).click()

    alert = driver.switch_to.alert
    assert alert.text == "I am a JS prompt"
    alert.send_keys("Claude")
    alert.accept()
    alert_input = wait.until(EC.presence_of_element_located((By.ID, "result")))
    assert alert_input.text == "You entered: Claude"

@pytest.mark.alerts
def test_js_alert_prompt_dismmissed(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    wait = WebDriverWait(driver,10)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[onclick='jsPrompt()']"))).click()

    alert = driver.switch_to.alert
    assert alert.text == "I am a JS prompt"
    alert.send_keys("Claude")
    alert.dismiss()
    alert_input = wait.until(EC.presence_of_element_located((By.ID, "result")))
    assert alert_input.text == "You entered: null"

@pytest.mark.deprecated
@pytest.mark.iframe
def test_iframe_text_input(driver):
    driver.get("https://the-internet.herokuapp.com/iframe")
    wait = WebDriverWait(driver,10)

    driver.switch_to.frame("mce_0_ifr")
    body = driver.find_element(By.ID, "tinymce")
    body.clear()
    body.send_keys("Hello iframe")

    body_check = driver.find_element(By.ID, "tinymce")
    assert body_check.text == "Hello iframe"

@pytest.mark.iframe
def test_iframe_switch(driver):
    driver.get("https://the-internet.herokuapp.com/iframe")
    wait = WebDriverWait(driver, 10)
    
    driver.switch_to.frame("mce_0_ifr")
    body = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
    assert body.is_displayed()
    
    driver.switch_to.default_content()
    
    # After switching back, the iframe element should be findable in the main DOM
    iframe = driver.find_element(By.ID, "mce_0_ifr")
    assert iframe.is_displayed()

@pytest.mark.hover
def test_hover_functionality(driver):
    driver.get("https://the-internet.herokuapp.com/hovers")
    wait = WebDriverWait(driver,10)
    
    figures = driver.find_elements(By.CLASS_NAME , "figure")
    first_avatar = figures[0]

    actions = ActionChains(driver)
    actions.move_to_element(first_avatar).perform()

    content = first_avatar.find_element(By.CLASS_NAME, "figcaption")
    assert "user1" in content.text

@pytest.mark.hover
@pytest.mark.robust_version
def test_hover_functionality_robust(driver):
    driver.get("https://the-internet.herokuapp.com/hovers")
    wait = WebDriverWait(driver, 10)
    
    figures = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "figure")))
    first_avatar = figures[0]
    
    actions = ActionChains(driver)
    actions.move_to_element(first_avatar).perform()
    
    caption = first_avatar.find_element(By.CLASS_NAME, "figcaption")
    wait.until(EC.visibility_of(caption))
    
    assert "user1" in caption.text