# Напишите функцию, которая принимает на вход список словарей и значение для ключа
# state  (опциональный параметр со значением по умолчанию EXECUTED ) и возвращает новый список,
# содержащий только те словари, у которых ключ
# state  содержит переданное в функцию значение

# Вход функции
info_list1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Выход функции со статусом по умолчанию EXECUTED
# [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
# [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
# Пишите свой код ниже


def only_state(info_list: list, state_only: str = "EXECUTED") -> list:
    new_list: list = []
    for info in info_list:
        # print(info)
        if info["state"] == state_only:
            new_list.append(info)
    return new_list


if __name__ == "__main__":
    print(only_state(info_list1))

# Напишите функцию, которая принимает на вход список словарей и возвращает новый список,
# в котором исходные словари отсортированы по убыванию даты (ключ date ).
# Функция принимает два аргумента, второй необязательный задает порядок сортировки (убывание, возрастание).

# Вход функции
info_list2 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]


def sorted_date(info_list: list, flow: bool = True) -> list:
    new_list: list = []
    # flow: bool
    if flow is True:
        new_list = sorted(info_list, key=lambda x: x["date"], reverse=True)
    else:
        new_list = sorted(info_list, key=lambda x: x["date"], reverse=False)

    return new_list


if __name__ == "__main__":
    print(sorted_date(info_list2, False))
