import pytest  # importing the pytest module
from pytest_bdd import scenarios, scenario, given, then, when
from pathlib import Path  # importing the Path class from pathlib module

# from pytest_bdd.types import FEATURE
Folder_name = "features"
file_name = "basic.feature"
BASE_DIR = Path(__file__).resolve().parent  # setting up the BASE_DIR to Parent directory
FEATURE_DIR = BASE_DIR.joinpath(Folder_name).joinpath(
    file_name)  # adding the feature directory to fetch the feature file
print(FEATURE_DIR)


def pytest_configure():  # defining the global variable to deal with the pytest.amount
    pytest.amount = 0  # setting the amount as 100 globally


@scenario(FEATURE_DIR, 'Testing Banking withdraw application')
def test_withdraw_ap():
    print("Test execute after all the Steps i.e Given, When, Then and And ")
    pass


@given("setting the balance to 100 Dollar")
def stable_balance():
    print("Accessing the balance as 100 Dollar")
    print(pytest.amount)  # this will throw the error because we can't access the global variable of pytest
    pytest.amount = 100


@when("when withdraw 30 Dollar")
def withdraw():
    pytest.amount = pytest.amount - 30


@then("Remaining balance is 70 Dollar")
def output_val():
    assert pytest.amount == 70
