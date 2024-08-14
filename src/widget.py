import masks


def mask_account_card(data_card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    if "Счет" in data_card:
        number_score = "".join(el if el.isdigit() else "" for el in data_card)
        number_score_mask = masks.get_mask_account(number_score)
        name_score = "".join("" if el.isdigit() else el for el in data_card)
        data_mask = name_score + number_score_mask
    else:
        number_card = "".join(el if el.isdigit() else "" for el in data_card)
        number_card_mask = masks.get_mask_card_number(number_card)
        name_card = "".join("" if el.isdigit() else el for el in data_card)
        data_mask = name_card + number_card_mask
    return data_mask


def get_date(card_date: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ")"""
    day = card_date[8:10] + "."
    month = card_date[5:7] + "."
    year = card_date[:4]
    total_date = day + month + year

    return total_date


print(mask_account_card("Счет 64686473678894779589"))

print(get_date("2024-03-11T02:26:18.671407"))
