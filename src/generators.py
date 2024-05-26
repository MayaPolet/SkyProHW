transactions = [
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


def filter_by_currency(trans_list: list, curr: str):
    """Фильтрует список транзакций по заданной валюте"""
    filtered_list = filter(lambda trans: trans["operationAmount"]["currency"]["code"] == curr, trans_list)
    return filtered_list


if __name__ == "__main__":
    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(2):
        print(next(usd_transactions)["id"])


def transaction_descriptions(trans_list: list):
    """Возвращает из списка операций описание каждой операции по очереди"""
    for trans in trans_list:
        result = trans["description"]
        yield result


if __name__ == "__main__":
    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        print(next(descriptions))


def format_number(num: int):
    """Преобразует число в строку формата XXXX XXXX XXXX XXXX"""
    number_to_format = "0000000000000000"
    num_str = str(num)
    number_to_format = number_to_format[: 16 - len(num_str)] + num_str
    out = []
    while number_to_format:
        out.append(number_to_format[-4:])
        number_to_format = number_to_format[:-4]
        result = " ".join(out[::-1])
    return result


def card_number_generator(start, finish):
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра,
    в заданном диапазоне (диапазоны передаются как параметры генератора)."""
    card_list = []
    for i in range(start, finish + 1):
        # format_number(i)
        card_list.append(format_number(i))
    return card_list


if __name__ == "__main__":
    for card_number in card_number_generator(101, 105):
        print(card_number)
