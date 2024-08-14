def filter_by_state(my_list: list, my_state: str='EXECUTED') -> list:
    """Функция принимает список словарей и опционально значение для ключа
    state (по умолчанию 'EXECUTED'). И возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению"""
    new_list = []
    for sublist in my_list:
        if sublist["state"] == my_state:
            new_list.append(sublist)
        else:
            continue
    return new_list


def sort_by_date(my_list: list, revers: bool) -> list:
    """Функция принимает список словарей
    и возвращакет новый список, отсортированный по дате (по убываюнию)"""
    sorted_my_list = sorted(my_list, key=lambda el: el["date"][:9], reverse=revers)
    return sorted_my_list


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "EXECUTED",
    )
)
print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        True,
    )
)
