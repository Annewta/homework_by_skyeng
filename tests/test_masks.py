from src.masks import get_mask_card_number
from src.masks import get_mask_account

def test_get_mask_card_number_1():
    '''Тестирование правильности маскирования номера карты'''
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number('7365410843013587') == '7365 41** **** 3587'

def test_get_mask_card_number_2():
    '''Проверка работы функции на различных входных форматах номеров карт,
    включая граничные случаи и нестандартные длины номеров'''
    assert get_mask_card_number('70AB79228960DR61') == '70AB 79** **** DR61'
    assert get_mask_card_number('7365410843013587154132423122') == '7365 41** **** 3587 1541 3242 3122'

def test_get_mask_card_number_3():
    '''Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты'''
    assert get_mask_card_number('') == ''


def test_get_mask_account_1():
    '''Тестирование правильности маскирования номера счета'''
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account('73351653505463512596') == '**2596'


def test_get_mask_account_2():
    '''Проверка работы функции с различными форматами и длинами номеров счето'''
    assert get_mask_card_number('7365410843013587154132423122') == '**3122'
    assert get_mask_card_number('7335165350546351ADCV') == '**ADCV'

def test_get_mask_account_3():
    '''Проверка, что функция корректно обрабатывает входные строки, где номер счета меньше ожидаемой длины'''
    assert get_mask_card_number('123') == ''
    assert get_mask_card_number('') == ''