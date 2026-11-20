import pytest
from wallet_withdrawal import withdraw


def test_valid_withdrawal():
    assert withdraw(1000, 200) == 800


def test_withdraw_exact_balance():
    assert withdraw(1000, 1000) == 0


@pytest.mark.parametrize(
    ("balance_cents", "amount_cents"),
    [
        (-1, 100),
        (1000, 0),
        (1000, -1),
        (1000, 1500),
    ],
)
def test_withdraw_value_errors(balance_cents, amount_cents):
    with pytest.raises(ValueError):
        withdraw(balance_cents, amount_cents)


@pytest.mark.parametrize(
    ("balance_cents", "amount_cents"),
    [
        ("1000", 100),
        (1000, "100"),
        (True, 100),
    ],
)
def test_withdraw_type_errors(balance_cents, amount_cents):
    with pytest.raises(TypeError):
        withdraw(balance_cents, amount_cents)