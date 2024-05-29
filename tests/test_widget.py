import pytest

from src.widget import date_format, mask_info


@pytest.mark.parametrize(
    "info, expected_mask",
    [
        ("Maestro 1596837868705199", "Maestro 1596 37** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 00** **** 6758"),
    ],
)
def test_mask_info(info, expected_mask):
    assert mask_info(info) == expected_mask


def test_date_format():
    assert date_format("2018-07-11T02:26:18.671407") == "11.07.2018"
