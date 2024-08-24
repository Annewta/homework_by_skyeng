from src.masks import get_mask_card_number
from src.masks import get_mask_account

def test_get_mask_card_number(mask_card):
    '''Тестирование правильности маскирования номера карты'''
    assert get_mask_card_number(mask_card) == ['7000 79** **** 6361', '7365 41** **** 3587', '70AB 79** **** DR61', '7365 41** **** 3587 1541 3242 3122', '']


def test_get_mask_account(mask_account):
    '''Тестирование правильности маскирования номера счета'''
    assert get_mask_account(mask_account) == ['**4305', '**2596', '**3122', '**ADCV', '', '']