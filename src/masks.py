def get_mask_card_number(card: str) -> str:
    """Функция принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    if card != '' and len(card) == 16:
        mask_card = card[:4] + ' ' + card[4:6] + '** **** ' + card[-4:]
    elif card == '':
        mask_card = 'Нет данных'
    else:
        mask_card = 'Неверный номер карты'
    return mask_card


print(get_mask_card_number(''))


def get_mask_account(score: list) -> list:
    """Функция принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX"""
    if score != '' and len(score) == 20:
        score_mask = "**" + score[-4:]
    elif score == '':
        score_mask = 'Нет данных'
    else:
        score_mask = 'Неверный номер счета'
    return score_mask

print(get_mask_account(''))
