# Пример работы функции, возвращающей маску карты
# 7000792289606361     # входной аргумент
# 7000 79** **** 6361  # выход функции

# Пример работы функции, возвращающей маску счета
# 73654108430135874305  # входной аргумент
# **4305                # выход функции


card_number = "1111222233334444"
account_number = "1111222233334444"


def mask_account(account_number: str) -> str:
    """Маскирует номер счета"""
    account_mask = "**" + account_number[-4:]
    return account_mask


def mask_card(card_number: str) -> str:
    """Маскирует номер карты"""
    card_mask = card_number[0:4] + " " + card_number[5:7]
    card_mask = card_mask + "** **** " + card_number[-4:]
    return card_mask


if __name__ == "__main__":
    print(card_number, account_number, sep=" ")
    print(mask_card(card_number))
    print(mask_account(account_number))
