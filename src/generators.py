def filter_by_currency(trans_list: list, curr: str):
    """Фильтрует список транзакций по заданной валюте"""
    for trans in trans_list:
        if trans["operationAmount"]["currency"]["code"] == curr:
            result = trans
        else:
            continue
        yield result


def transaction_descriptions(trans_list: list):
    """Возвращает из списка операций описание каждой операции по очереди"""
    for trans in trans_list:
        result = trans["description"]
        yield result


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
    for i in range(start, finish + 1):
        card_number = format_number(i)
        yield card_number
