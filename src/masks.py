# Пример работы функции, возвращающей маску карты
# 7000792289606361     # входной аргумент
# 7000 79** **** 6361  # выход функции

# Пример работы функции, возвращающей маску счета
# 73654108430135874305  # входной аргумент
# **4305                # выход функции
from logers import log2

card_number = "1111222233334444"
account_number = "1111222233334444"
info_account = "Счет 69086868315648596195"
info_card = "American Express 1368443024115273"


def mask_account(account_number: str) -> str:
    """Маскирует номер счета"""
    account_mask = "**" + account_number[-4:]
    return account_mask


def mask_card(card_number: str) -> str:
    """Маскирует номер карты"""
    card_mask = card_number[0:4] + " " + card_number[5:7]
    card_mask = card_mask + "** **** " + card_number[-4:]
    return card_mask


def mask_info(info: str) -> str:
    """Маскирует номер карты или счета"""
    info_length = len(info)
    if info_length == 21:
        info_masked = mask_account(info[-16:])
    else:
        info_masked = mask_card(info[-16:])
    result = info[:-15] + info_masked
    return result


if __name__ == "__main__":
    print(mask_info(info_account))
    print(mask_info(info_card))


if __name__ == "__main__":
    log2.debug(card_number)
    log2.debug(account_number)
    # log2.debug(card_number, account_number, sep=" ")
    log2.debug(mask_card(card_number))
    log2.debug(mask_account(account_number))
