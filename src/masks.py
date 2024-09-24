def get_mask_card_number(card: str) -> str:
    """Функция принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    card_mask  = [num[:6] + " ****" + num[-4:] for num in card]

    return card_mask


print(get_mask_card_number("73654108430135874305"))


def get_mask_account(score: str) -> str:
    """Функция принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX"""
    score_mask = ["**" + num[-4:] for num in score]

    return score_mask


print(get_mask_account("73654108430135874305"))
