def get_mask_card_number(card: str) -> str:
    """Функция принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    card_star = card.replace(card[6:12], "******")
    n = 4
    card_mask = " ".join([card_star[i : i + n] for i in range(0, len(card_star), n)])

    return card_mask


print(get_mask_card_number("7000792289606361"))


def get_mask_account(score: str) -> str:
    """Функция принимает на вход номер счета в виде числа
    и возвращает маску номера по правилу **XXXX"""
    score_mask = "**" + score[-4:]

    return score_mask


print(get_mask_account("73654108430135874305"))
