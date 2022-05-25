import pytest
from pytest_bdd import scenarios,scenario,given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent
FEATURE_DIR=BASE_DIR / "features"
FEATURE_FILE=FEATURE_DIR / "logo.feature"

scenarios(FEATURE_FILE)


@pytest.fixture
def setUp01():
    print("setUp executed")
    driver_loc="C:\\Users\\611903295\\Downloads\\Pytest_BDD_unhashed\\chromedriver.exe"
    yield driver_loc
    print("Tear down Executed")


@given("Open the Edge Browser",target_fixture="driver")
def launch_browser(setUp01):
    options=Options()
    options.binary_location="C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    driver = webdriver.Chrome(options=options,executable_path=setUp01)
    return driver


@when("Open the Orange HRM homepage")
def open_homepage(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")


@when("click on the Logo on thr Top then")
def click_logo(driver):
    driver.find_element(By.XPATH,"//div[@id='divLogo']//img").click()


@then("check the Logo been displayed or not")
def check_logo(driver):
    status=driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True


@then("close the Browser")
def close_browser(driver):
    driver.close()


