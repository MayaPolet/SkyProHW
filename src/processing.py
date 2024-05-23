def only_state(info_list: list, state_only: str = "EXECUTED") -> list:
    """возвращает список словарей с заданным ключом 'state'"""
    new_list: list = []
    for info in info_list:
        if info["state"] == state_only:
            new_list.append(info)
    return new_list


def sorted_date(info_list: list, flow: bool = True) -> list:
    """сортирует список словарей по ключу 'date' в заданном порядке"""
    new_list = sorted(info_list, key=lambda x: x["date"], reverse=flow)
    return new_list
