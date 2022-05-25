from pytest_bdd import scenarios, scenario, given, when, then, parsers
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
FEATURE_DIR = BASE_DIR / "features"
Feature_file = FEATURE_DIR / "tagging.feature"


# scenarios(FEATURE_FILE)
@scenario(Feature_file, "set addition manipulation")
def test_tag():
    pass


@given("i have 3 fruits in the basket", target_fixture="basket")
def initial_state():
    my_set = {'apple', 'banana', 'orange'}
    return my_set


@when("we add similar elements which are already present")
def add_fruit(basket):
    basket.add('apple')
    basket.add('banana')
    basket.add('orange')


@then("size of the set remain same")
def total_fruit(basket):
    assert len(basket) == 3


@then("when we add a unique new element to set")
def add_fruit(basket):
    basket.add('mango')


@then(parsers.parse("the size of the set will be {count:d}"))
def total_fruit(basket, count):
    assert len(basket) == count
