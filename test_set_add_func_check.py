from pytest_bdd import scenarios, scenario, given, when, then, parsers
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
FEATURE_DIR = BASE_DIR / "features"
FEATURE_FILE = FEATURE_DIR / "set_manipul.feature"

scenarios(FEATURE_FILE)


@given("i have 3 fruits in the set", target_fixture="my_set")
def set_initialization():
    my_set = {"apple", "oranges", "banana"}
    return my_set


@when("we add elements which are already present")
def similar_calc(my_set):
    my_set.add("apple")


@then("size of the set remain constant")
def total_size(my_set):
    assert len(my_set) == 3


@then("when we add a new unique element")
def add_unique(my_set):
    my_set.add("berry")


@then(parsers.parse("the size of the set will be {count:d}"))
def total_count(my_set,count):
    assert len(my_set) == count

