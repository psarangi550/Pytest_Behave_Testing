from pytest_bdd import scenarios,scenario,given,when,then,parsers
from pathlib import Path


BASE_DIR=Path(__file__).parent.resolve()
FEATURE_DIR=BASE_DIR / "features"
FEATURE_FILE=FEATURE_DIR / "fruits.feature"

scenarios(FEATURE_FILE)


@given(parsers.parse("I have {count:d} Fruites"),target_fixture="start_fruit")
def beg_fruit(count):
    start_fruit={"start":count,"eat":0}
    return start_fruit


@when(parsers.parse("I eat {eat:d} Fruites"))
def cal_fruit(start_fruit,eat):
    start_fruit["eat"] += eat


@then(parsers.parse("I have now {left:d} Fruites in the basket"))
def left_fruit(start_fruit,left,count):
    assert start_fruit["start"] == count
    assert start_fruit["start"]-start_fruit["eat"]==left
