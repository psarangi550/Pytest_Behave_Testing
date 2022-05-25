import pytest
from selenium import webdriver
from pytest_bdd import scenarios,scenario,given,when,then
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import time

BASE_DIR=Path(__file__).parent.resolve()
FEATURE_DIR=BASE_DIR / "feature"
FEATURE_FILE=FEATURE_DIR / "login_about.feature"

scenarios(FEATURE_FILE)


@pytest.fixture
def setup01():
    driver_location = "C:\\Users\\611903295\\Downloads\\Pytest_BDD_unhashed\\chromedriver.exe"
    options=Options()
    options.binary_location="C:\\Users\\611903295\\AppData\\Local\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    driver = webdriver.Chrome(options=options,executable_path=driver_location)
    yield driver
    print("executing the tear_down process")
    driver.quit()


@given("Open the Brave Browser Driver",target_fixture="setup01")
def open_edge_browser(setup01):
    setup01.maximize_window()
    return setup01


@given("Open the Orange HRM homepage")
def open_homepage(setup01):
    setup01.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")


@given("Enter the Username and Password")
def user_auth(setup01):
    setup01.find_element(By.ID,"txtUsername").send_keys("admin")
    setup01.find_element(By.ID,"txtPassword").send_keys("admin123")


@given("click the login Button")
def click_login(setup01):
    setup01.find_element(By.ID, "btnLogin").click()


@then("verify dashboard is getting open or not")
def verify_dashboard(setup01):
    result=setup01.find_element(By.XPATH, "//h1[contains(text(),'Dashboard')]").text
    assert result == "Dashboard"


@then("close or quit the Brave browser")
def close_brave_browser(setup01):
    setup01.close()


@when("click on the Profile Option")
def click_profile(setup01):
    setup01.find_element(By.ID, "welcome").click()
    time.sleep(2)


@when("click on the About option of the Profile")
def click_about(setup01):
    setup01.find_element(By.ID, "aboutDisplayLink").click()


@then("validate the About Page been displayed or not")
def verify_about(setup01):
    status=setup01.find_element(By.XPATH, "//h3[contains(text(),'About')]").text
    assert status == "About"


@then("close or quit the browser")
def close_browser(setup01):
    setup01.close()
