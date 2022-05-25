from pytest_bdd import scenarios, scenario, given, when, then, parsers
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
FEATURE_DIR = BASE_DIR / "features"
FEATURE_FILE = FEATURE_DIR / "scenarioutline.feature"

scenarios(FEATURE_FILE)


@given(parsers.parse("Bank Starting  Balance amount is {start:d}"),target_fixture="account_bal")
def start_balance(start):
    return dict(bal=start)


@when(parsers.parse("A Deposit made with {depo:d} Amount"))
def depo_amount(depo, account_bal):
    account_bal["bal"] += int(depo)


@when(parsers.parse("A withdraw also made with {withdraw:d} Amount"))
def with_amount(withdraw, account_bal):
    account_bal["bal"] -= int(withdraw)


@then(parsers.parse("Total final balance is {final:d}"))
def end_balance(final, account_bal):
    assert account_bal["bal"] == final

