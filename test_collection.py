from pathlib import Path
import pytest
from pytest_bdd import scenarios,scenario,given,when,then

BASE_DIR=Path(__file__).parent.resolve()
FEATURE_DIR=BASE_DIR / "features"
FEATURE_FILE=FEATURE_DIR / "collection.feature"

scenarios(FEATURE_FILE)


@pytest.fixture(scope="module")
def setUp01():
    my_list=["jan","feb","mar","apr","may","jun","jul"]
    yield my_list
    print("executing the TearDown")
    del my_list


@pytest.fixture(scope="module")
def setUp02():
    my_set={"jan","feb","mar","apr","may","jun","jul"}
    yield my_set
    print("executing the TearDown")
    del my_set


@given("initialize List with  Elements",target_fixture="setUp01")
def initialize_list(setUp01):
    if len(setUp01) == 0:
        pytest.xfail("No List Elements")
    else:
        while len(setUp01) > 3:
            setUp01.pop()
    return setUp01


@when("Added 2 elements into it")
def add_elements(setUp01):
    setUp01.extend(["apr","may"])


@then("check the elements list size")
def check_elements(setUp01):
    print(setUp01)
    assert len(setUp01)==5


@given("Set with Elements",target_fixture="setUp02")
def initialize_set(setUp02):
    if len(setUp02)==0:
        pytest.xfail("No Set With Elements")
    else:
        while len(setUp02) > 3:
            setUp02.pop()
    return setUp02


@when("Added 2 Elements into the initialized sets")
def add_set_element(setUp02):
    setUp02.add("apr")
    setUp02.add("may")


@then("check size of the Set Element")
def check_size_element(setUp02):
    assert len(setUp02) == 5
