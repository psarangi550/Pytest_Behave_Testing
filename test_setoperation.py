import pytest  # importing the pytest module
from pytest_bdd import scenarios,scenario,given,when,then
from pathlib import Path  # importing the Path class from pathlib module

BASE_DIR = Path(__file__).resolve().parent
FEATURE_DIR = BASE_DIR / "features"
FEATURE_FILE=FEATURE_DIR / "setoperation.feature"


@scenario(FEATURE_FILE,"set manipulation operation")
def test_set_main():
    pass


@given("initialize the set using text_fixture",target_fixture="my_set")
def launch_set():
    my_set={"apple","mango","orange"}
    return my_set


@when("remove one element from the set")
def remove_element(my_set):
    my_set.pop()
    print(my_set)


@then("checking the length of the set")
def check_length(my_set):
    assert len(my_set) ==2