import pytest
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



@pytest.mark.smoke
def test_file_upload(driver):
    url = "https://the-internet.herokuapp.com"
    driver.get(url)
    
    wait = WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"File Upload"))).click()
    assert driver.current_url == "https://the-internet.herokuapp.com/upload"

    file_input = driver.find_element(By.ID, "file-upload")
    file_input.send_keys("C:\\Users\\PC\\Downloads\\test_file.txt")
    wait.until(EC.element_to_be_clickable((By.ID,"file-submit"))).click()


    assert driver.find_element(By.CSS_SELECTOR, "div.example h3").text == "File Uploaded!"
    assert "test_file.txt" in driver.find_element(By.ID, "uploaded-files").text
    


    # missing to do: 
    # Make an API call to verify the file exists on the server
    # Download it back and check the contents
    # Assert file size matches what you uploaded

@pytest.mark.smoke
def test_file_download(driver_download):
    driver, download_dir = driver_download

    url = "https://the-internet.herokuapp.com"
    driver.get(url)
    
    wait = WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"File Download"))).click()
    assert driver.current_url == "https://the-internet.herokuapp.com/download"

    driver.find_element(By.LINK_TEXT, "sample-upload.txt").click()
    file_path = os.path.join(download_dir, "sample-upload.txt")

    for _ in range(10):
        if os.path.exists(file_path):
            break
        time.sleep(2)

    assert os.path.exists(file_path), f"File not downloaded: {file_path}"