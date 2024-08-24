from src.widget import mask_account_card
from src.widget import get_date

def test_mask_account_card(mask_account_card_fix):
    '''Тесты для проверки, что функция корректно распознает
    и применяет нужный тип маскировки в зависимости от типа входных данных
    (карта или счет)'''
    assert mask_account_card(mask_account_card_fix) == ('Счет **9589', 'Visa Platinum 7000 79** **** 6361', 'Счет **5560')

def test_mask_account_card_type(mask_account_card_fix):
    '''Параметризованные тесты с разными типами карт и счетов
    для проверки универсальности функции'''
    assert mask_account_card(mask_account_card_fix) == ('Счет **9589', 'Visa Platinum 7000 79** **** 6361', 'Maestro 7000 79** **** 6361', 'MasterCard 7158 30** **** 6758', 'Счет **5560')

def test_mask_account_card_error(mask_account_card_fix):
    '''Тестирование функции на обработку некорректных входных данных
    и проверка ее устойчивости к ошибкам'''
    assert mask_account_card(mask_account_card_fix) == 'Некорректные входные данные'

def test_get_date(get_date_fix):
    '''Тестирование правильности преобразования даты'''
    assert get_date(get_date_fix) == ('11.03.2024','11.12.2025', '11.03.2024', '11.03.2024', 'Некорректные данные. Введите дату в формате: ГГГГ-ММ-ДД', '', 'Некорректные данные. Введите дату в формате: ГГГГ-ММ-ДД')