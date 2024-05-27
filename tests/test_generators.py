import pytest

from src.generators import card_number_generator, filter_by_currency, format_number, transaction_descriptions

transactions_to_test = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def test_filter_by_currency_usd():
    expected_result = [939719570, 142264268]
    result = filter_by_currency(transactions_to_test, "USD")
    for i in range(2):
        assert next(result)["id"] == expected_result[i]


def test_filter_by_currency_rub():
    expected_result = [873106923, 594226727]
    result = filter_by_currency(transactions_to_test, "RUB")
    for i in range(2):
        assert next(result)["id"] == expected_result[i]


def test_transaction_descriptions():
    expected_result = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    result = transaction_descriptions(transactions_to_test)
    for i in range(5):
        assert next(result) == expected_result[i]


def test_format_number():
    result = format_number(111122223333)
    assert result == "0000 1111 2222 3333"


@pytest.mark.parametrize(
    "start, finish, expected_result", [(101, 101, "0000 0000 0000 0101"), (103, 103, "0000 0000 0000 0103")]
)
def test_card_number_generator(start, finish, expected_result):
    result = card_number_generator(start, finish)
    assert next(result) == expected_result
