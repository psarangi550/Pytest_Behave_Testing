from pytest_bdd import scenarios,given,when,then,scenario,parsers
from selenium import webdriver
from pathlib import Path
import pytest
BASE_DIR=Path(__file__).parent.resolve()
FEATURE_DIR=BASE_DIR.joinpath("features")
FEATURE_FILE=FEATURE_DIR.joinpath("hrm_login.feature")


@pytest.fixture(scope="module")
def Fixture01():
    driver=webdriver.Edge()
    return driver


# @scenario(FEATURE_FILE,"Access the Login page of Orange HRM")
# def test_login_param():
#     pass

scenarios(FEATURE_FILE)


@given("Open Brave Browser",target_fixture="Fixture01")
def open_edge(Fixture01):
    Fixture01.maximize_window()
    return Fixture01


@when("Open the Orange HRM")
def open_hrm_edge(Fixture01):
    Fixture01.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")


@when(parsers.parse('Enter the Username as {user} and Password as {passwd}'))
def open_login(Fixture01,user,passwd):
    Fixture01.find_element_by_id("txtUsername").send_keys(user)
    Fixture01.find_element_by_id("txtPassword").send_keys(passwd)


@when("click the login")
def login_btn_click(Fixture01):
    Fixture01.find_element_by_id("btnLogin").click()


@then("verify dashboard is getting open or not after login")
def verify_dash(Fixture01):
    status=Fixture01.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    assert status == "Dashboard"


@then("close the Brave browser")
def cls_browser(Fixture01):
    Fixture01.close()