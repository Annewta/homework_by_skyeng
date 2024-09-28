from src.masks import get_mask_card_number
from src.masks import get_mask_account

def test_get_mask_card_number(fix_mask_card):
    '''Тестирование правильности маскирования номера карты'''
    mask_card = []
    for card_num in fix_mask_card:
        if len(card_num) == 16:
            card_masks = get_mask_card_number(card_num)
        else:
            card_masks = 'Неверный номер карты'
        mask_card.append(card_masks)
    assert mask_card == ['7000 79** **** 6361', '7365 41** **** 3587', '70AB 79** **** DR61', 'Неверный номер карты', 'Неверный номер карты']


def test_get_mask_account(fix_mask_account):
    '''Тестирование правильности маскирования номера счета'''
    mask_score = []
    for num in fix_mask_account:
        if len(num) == 20:
            score_mask = "**" + num[-4:]
        else:
            score_mask = 'Неверный номер счета'
        mask_score.append(score_mask)
    assert mask_score == ['**4305', '**2596', 'Неверный номер счета', '**ADCV', 'Неверный номер счета', 'Неверный номер счета']