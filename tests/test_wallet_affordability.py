import pytest
from wallet_affordability import can_afford


def test_balance_greater_than_price():
    assert can_afford(1000, 500) is True


def test_balance_equals_price():
    assert can_afford(1000, 1000) is True


def test_balance_less_than_price():
    assert can_afford(500, 1000) is False


def test_zero_price():
    assert can_afford(1000, 0) is True


def test_zero_balance_and_zero_price():
    assert can_afford(0, 0) is True
#Several test cases use the same logic with different input values.
#@pytest.mark.parametrize reduces duplicate code and improves maintainability.

@pytest.mark.parametrize(
    ("balance_cents", "price_cents"),
    [
        (-1, 100),
        (100, -1),
    ],
)
def test_affordability_value_errors(balance_cents, price_cents):
    with pytest.raises(ValueError):
        can_afford(balance_cents, price_cents)


@pytest.mark.parametrize(
    ("balance_cents", "price_cents"),
    [
        ("1000", 500),
        (1000, "500"),
        (True, 500),
    ],
)
def test_affordability_type_errors(balance_cents, price_cents):
    with pytest.raises(TypeError):
        can_afford(balance_cents, price_cents)
#python -m pytest --cov=.