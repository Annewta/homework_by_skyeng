def get_mask_card_number(card: str) -> str:
    """Функция принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    mask_card = card[:4] + ' ' + card[4:6] + '** **** ' + card[-4:]
    return mask_card


print(get_mask_card_number('7000792289606361'))


def get_mask_account(score: list) -> list:
    """Функция принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX"""
    score_mask = "**" + score[-4:]
    return score_mask

print(get_mask_account('73654108430135874305'))
