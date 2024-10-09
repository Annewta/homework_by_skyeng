from src.masks import get_mask_card_number
from src.masks import get_mask_account

def test_get_mask_card_number(fix_mask_card):
    '''Тестирование правильности маскирования номера карты'''
    mask_card = []
    for card_num in fix_mask_card:
        card_masks = get_mask_card_number(card_num)
        mask_card.append(card_masks)
    assert mask_card == ['7000 79** **** 6361', '7365 41** **** 3587', '70AB 79** **** DR61']


def test_get_mask_account(fix_mask_account):
    '''Тестирование правильности маскирования номера счета'''
    mask_score = []
    for num in fix_mask_account:
        score_mask = get_mask_account(num)
        mask_score.append(score_mask)
    assert mask_score == ['**4305', '**2596', '**ADCV']

def test_get_mask_card_number_empty(fix_mask_empty):
    '''Тестирование правильности маскирования пустых входящих данных номера карты'''
    result = get_mask_card_number(fix_mask_empty)
    assert result == 'Нет данных'

def test_get_mask_account_empty(fix_mask_empty):
    '''Тестирование правильности маскирования пустых входящих данных номера счета'''
    result = get_mask_account(fix_mask_empty)
    assert result == 'Нет данных'

def test_get_mask_card_number_error(fix_mask_error):
    '''Тестирование корректности маскирования номера карты'''
    mask_card = []
    for num in fix_mask_error:
        card_masks = get_mask_card_number(num)
        mask_card.append(card_masks)
    assert mask_card == ['Неверный номер карты', 'Неверный номер карты', 'Неверный номер карты']

def test_get_mask_account_error(fix_mask_error):
    '''Тестирование корректности маскирования номера счета'''
    mask_score = []
    for num in fix_mask_error:
        score_mask = get_mask_account(num)
        mask_score.append(score_mask)
    assert mask_score == ['Неверный номер счета', 'Неверный номер счета', 'Неверный номер счета']
