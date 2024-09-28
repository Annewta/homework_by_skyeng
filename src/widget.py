from src import masks

def mask_account_card(data_card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    if data_card == '' or len(data_card) >= 31 or len(data_card) <= 22:
        raise ValueError("Некорректные входные данные")
    elif "Счет" in data_card:
        number_score = "".join(el if el.isdigit() else "" for el in data_card)
        number_score_mask = masks.get_mask_account(number_score)
        data_mask = f'Счет {number_score_mask}'
    else:
        number_card = "".join(el if el.isdigit() else "" for el in data_card)
        number_card_mask = masks.get_mask_card_number(number_card)
        name_card = "".join("" if el.isdigit() else el for el in data_card)
        data_mask = name_card + number_card_mask
    return data_mask

def get_date(card_date: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ")"""
    if len(card_date)>=10 and card_date[4] == '-' and card_date[7] == '-':
        day = card_date[8:10] + "."
        month = card_date[5:7] + "."
        year = card_date[:4]
        total_date = day + month + year
        return total_date
    else:
        return 'Некорректные данные. Введите дату в формате: ГГГГ-ММ-ДД'


print(mask_account_card('Visa Platinum 7000792289606361'))

print(get_date("2024-03-11T02:26:18.671407"))
