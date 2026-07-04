import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser): #this is addoption pytest logic a staple
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run Chrome in headless mode locally"
    )

    parser.addoption(
        "--screenshot",        # the flag name — what you type in the terminal
        action="store_true",   # means: if flag is present, value is True. If absent, value is False
        default=False,         # value when flag is NOT passed
        help="Take screenshot on test failure"  # shows up in pytest --help
    )
 
def get_chrome_options(request):
    options = Options()
    headless = os.getenv("CI") == "true" or request.config.getoption("--headless")
    
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    
    return options

@pytest.fixture
def driver(request):
    options = get_chrome_options(request)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def driver_download(request): 
    options = get_chrome_options(request)
    download_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "downloads")
    os.makedirs(download_dir, exist_ok=True)
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver, download_dir
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        if item.config.getoption("--screenshot"):
            driver = item.funcargs.get("driver")
            if driver:
                os.makedirs("screenshots", exist_ok=True)
                screenshot_path = f"screenshots/{item.name}.png"
                driver.save_screenshot(screenshot_path)
                print(f"\nScreenshot saved: {screenshot_path}")

    # @pytest.fixture
# def driver():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     driver.quit()

