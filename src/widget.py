# mask_info Принимать на вход строку с информацией — тип карты/счета и номер карты/счета.
# Возвращать исходную строку с замаскированным номером карты/счета.
#
from masks import mask_account, mask_card

info1 = "Maestro 1596837868705199"
info2 = "Счет 64686473678894779589"
info3 = "MasterCard 7158300734726758"


def mask_info(text_info: str) -> str:
    """Маскирует номер карты/счета"""
    number_info: str
    mask: str
    info_mask: str

    if text_info[0:4] == "Счет":
        number_info = text_info[-20:]
        mask = mask_account(number_info)
        info_mask = "Счет " + mask
    else:
        number_info = text_info[-16:]
        mask = mask_card(number_info)
        info_mask = text_info[: len(text_info) - 16] + mask
    # print(number_info)
    return info_mask


if __name__ == "__main__":
    print(mask_info(info1))
    print(mask_info(info2))
    print(mask_info(info3))


# date_format  принимает на вход строку вида 2018-07-11T02:26:18.671407
#  и возвращает строку с датой в виде  11.07.2018

date_info1 = "2018-07-11T02:26:18.671407"


def date_format(date_info: str) -> str:
    """Форматирует дату"""
    date_formated = date_info[8:10] + "." + date_info[5:7] + "." + date_info[:4]
    return date_formated


if __name__ == "__main__":
    print(date_format(date_info1))
