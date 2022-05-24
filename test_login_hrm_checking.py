import pytest
from selenium import webdriver
from pytest_bdd import scenarios,scenario,given,then,when
from pathlib import Path

Folder_name = "features"
file_name = "login.feature"
BASE_DIR = Path(__file__).resolve().parent  # setting up the BASE_DIR to Parent directory
FEATURE_DIR = BASE_DIR.joinpath(Folder_name).joinpath(
    file_name)  # adding the feature directory to fetch the feature file
# print(FEATURE_DIR)


@scenario(FEATURE_DIR,"Login of HRM Page")
def test_login():
    pass


@given("Launch the Edge Browser",target_fixture="driver")
def launching_browser():
    driver=webdriver.Edge(executable_path="C:\\Users\\611903295\\Downloads\\Pytest_Journey\\msedgedriver.exe")
    return driver


@when("open the  HRM Home Page")
def open_homepage(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")


@when("Enter Username and password")
def login_hrm_browser(driver):
    driver.find_element_by_id("txtUsername").send_keys("admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")


@when("click on the Login Button")
def click_login(driver):
    driver.find_element_by_id("btnLogin").click()


@then("Validate that access to the Dashboard Exist or not and close the browser")
def validate_dashboard(driver):
    status=driver.find_element_by_xpath("//h1[normalize-space()='Dashboard']").text
    assert status == "Dashboard"
    driver.close()
