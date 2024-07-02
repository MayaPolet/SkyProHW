from src.processing import only_state, sorted_date
from src.sorters import list_transactions_sort_search
from src.utils import get_transactions_from_csv, get_transactions_from_excel, get_transactions_from_json
from src.widget import date_format, mask_info


def main() -> None:
    """Обработка данных из файлов с банковскими транзакциями в соответствии с фильтрами,
    установленными пользователем"""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        item_number = input("Введите номер пункта: ")

        if item_number == "1":
            print("Для обработки выбран JSON-файл.")
            list_transactions = get_transactions_from_json("../data/transactions_json.ison")
            break
        elif item_number == "2":
            print("Для обработки выбран CSV-файл.")
            list_transactions = get_transactions_from_csv("../data/transactions.csv")
            break
        elif item_number == "3":
            print("Для обработки выбран XLSX-файл.")
            list_transactions = get_transactions_from_excel("../data/transactions_excel.xlsx")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    filters = []

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            "По умолчанию статус = EXECUTED\n"
        ).upper()
        if status in ["CANCELED", "PENDING", "EXECUTED"]:
            filters.append(("status", status))
            break
        elif not status:
            filters.append(("status", "EXECUTED"))
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    while True:
        sort_date = input("Отсортировать операции по дате?  Да/Нет\n").lower()
        if sort_date == "да":
            sorting_order = input("""Отсортировать от новых к старым? да/нет\n""").lower()
            if sorting_order == "нет":
                filters.append(("date", False))
                break
            else:
                filters.append(("date", True))
                break
        elif sort_date == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    while True:
        sort_code = input("Выводить только рублевые тразакции? Да/Нет\n").lower()
        if sort_code == "да":
            filters.append(("currency", "RUB"))
            break
        elif sort_code == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    while True:
        user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет:\n").lower()
        if user_input == "да":
            search = input("Введите слово для поиска: ")
            filters.append(("description", search))
            break
        elif user_input == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    transactions = list_transactions

    print(f"\nВаши фильтры: {filters}\n")
    # print(f"Первая транзакция в RUB = {transactions[10]}")
    # print(f"Первый вклад в RUB = {transactions[458]}")

    for filter_type, filter_value in filters:
        if filter_type == "status":
            transactions = only_state(transactions, filter_value)
        elif filter_type == "date":
            transactions = sorted_date(transactions, filter_value)
        elif filter_type == "currency":
            transactions = [txn for txn in transactions if txn["currency_code"] == filter_value]
        elif filter_type == "description":
            transactions = list_transactions_sort_search(transactions, filter_value)
    print("Распечатываю итоговый список транзакций...\n")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        # print(f"Всего банковских операций в выборке: {len(transactions)}")

        for transaction in transactions:
            if "from" in transaction:
                from_ = mask_info(transaction["from"])
            else:
                from_ = "0"
            to_ = mask_info(transaction["to"])
            date = date_format(transaction["date"])
            description = transaction["description"]
            amount = transaction["amount"]
            currency = transaction["currency_code"]

            if description == "Открытие вклада":
                print(f"{date} {description}\n{to_}\nСумма: {amount} {currency}\n")
            else:
                print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")
        print(f"Всего банковских операций в выборке: {len(transactions)}")


if __name__ == "__main__":
    main()
