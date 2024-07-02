# 12.1 Реализуйте функцию, которая принимает на вход путь до JSON-файла и возвращает список словарей
# с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
# функция возвращает пустой список. Функцию поместите в модуль # utils

# 13.1 Реализовать считывание финансовых операций из CSV - и XLSX - файлов.

import csv
import json

import pandas as pd
from dotenv import load_dotenv

# from logers import log1
from src.external_api import currency_conversion

load_dotenv()


def get_transactions_from_json(path: str) -> list[dict]:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            try:
                json_data = json.load(file)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    if len(json_data) == 0 or type(json_data) is not list:
        return []
    else:
        # result = [operation.get("operationAmount") for operation in json_data]
        result = json_data
        return result


if __name__ == "__main__":
    # path_to_json = "../data/operations.json"
    path_to_json = "../data/transactions_json.ison"
    trans_list = get_transactions_from_json(path_to_json)
    number_of_trans = len(trans_list)
    print(f"В ПЕЧАТИ json: Сформировано {number_of_trans} из json")
    print(f"В ПЕЧАТИ json: Список словарей- первый {trans_list[:1]}")
    log1.debug(f"Сформировано {number_of_trans} записей с транзакциями")



def get_transactions_from_csv(path: str) -> list[dict]:
    """Принимает на вход путь до CSV-файла и возвращает список словарей с данными о финансовых транзакциях."""
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        result = []
        for row in reader:
            row_dict = dict()
            for idx, item in enumerate(header):
                row_dict[item] = row[idx]
            result.append(row_dict)
    return result


if __name__ == "__main__":
    path_to_csv = "../data/transactions.csv"
    number_of_trans = len(get_transactions_from_csv(path_to_csv))
    print(f"Первая транзакция из csv = {get_transactions_from_csv(path_to_csv)[:1]}")
    with open("../data/transactions_json.ison", "w", encoding="utf-8") as file:
        tr_list = get_transactions_from_csv(path_to_csv)
        json.dump(tr_list, file, ensure_ascii=False)
    print(f"Сформировано {number_of_trans} записей с транзакциями")


def get_transactions_from_excel(path: str) -> list[dict]:
    """Принимает на вход путь до Excell-файла и возвращает список словарей с данными о финансовых транзакциях."""

    res = pd.read_excel(path).to_json(orient="records", indent=4, force_ascii=False)
    return json.loads(res)


if __name__ == "__main__":
    path_to_xls = "../data/transactions_excel.xlsx"
    number_of_trans = len(get_transactions_from_excel(path_to_xls))
    print(f"Первая транзакция из  xls = {get_transactions_from_excel(path_to_xls)[:1]}")
    print(f"Сформировано {number_of_trans} записей с транзакциями")


def get_amount(transaction: dict) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    if transaction["currency"]["code"] == "RUB":
        result = float(transaction["amount"])
        # print(f"Получена транзакция на сумму {result} руб.")
    else:
        # print(transaction["currency"]["code"],transaction["amount"] )
        result = currency_conversion(transaction["currency"]["code"], float(transaction["amount"]))
        # print(f"Получена транзакция на сумму {result} руб.")
    return result


# if __name__ == "__main__":
#     pass_to_json = "../data/operations.json"
#     transactions = get_transactions_from_json(pass_to_json)
#     for transaction in transactions:
#         trans_amount = get_amount(transaction)
#         user_input = input("Введите 'exit', чтобы выйти: ")
#         if user_input == "exit":
#             break
#         else:
#             continue
